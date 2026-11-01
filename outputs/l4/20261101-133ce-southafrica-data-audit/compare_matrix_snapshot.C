#include <TFile.h>
#include <TH2I.h>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

void compare_pair(std::ostream &output, const std::string &root_name,
                  const std::string &object_name, const std::string &matrix_name) {
  const std::string base = "raw/data/SouthAfrica/133Ce_iThemba2019/mat/";
  TFile input((base + "root/" + root_name).c_str(), "READ");
  auto *histogram = dynamic_cast<TH2I *>(input.Get(object_name.c_str()));
  std::ifstream matrix(base + matrix_name, std::ios::binary | std::ios::ate);
  output << "{\"root_file\":\"" << base + "root/" + root_name
         << "\",\"object\":\"" << object_name
         << "\",\"matrix_file\":\"" << base + matrix_name << "\"";
  if (!histogram || !matrix) {
    output << ",\"status\":\"input-unavailable\"}";
    return;
  }
  const int columns = histogram->GetNbinsX();
  const int rows = histogram->GetNbinsY();
  const std::size_t expected = std::size_t(columns) * rows * sizeof(std::int32_t);
  if (matrix.tellg() != std::streampos(expected) || columns != rows) {
    output << ",\"status\":\"size-or-shape-mismatch\"}";
    return;
  }
  matrix.seekg(0);
  std::vector<std::int32_t> values(std::size_t(columns) * rows);
  matrix.read(reinterpret_cast<char *>(values.data()), expected);
  if (!matrix) {
    output << ",\"status\":\"short-read\"}";
    return;
  }
  const auto *bins = histogram->GetArray();
  std::uint64_t direct_mismatch = 0;
  std::uint64_t transpose_mismatch = 0;
  std::uint64_t zero_based_mismatch = 0;
  std::uint64_t zero_based_transpose_mismatch = 0;
  std::int64_t binary_sum = 0;
  std::int64_t regular_bin_sum = 0;
  std::uint64_t nonzero_binary = 0;
  for (int row = 0; row < rows; ++row) {
    for (int column = 0; column < columns; ++column) {
      const auto forward = values[std::size_t(row) * columns + column];
      const auto transposed = values[std::size_t(column) * columns + row];
      const auto regular = bins[std::size_t(row + 1) * (columns + 2) + column + 1];
      const auto zero_based = bins[std::size_t(row) * (columns + 2) + column];
      direct_mismatch += regular != forward;
      transpose_mismatch += regular != transposed;
      zero_based_mismatch += zero_based != forward;
      zero_based_transpose_mismatch += zero_based != transposed;
      binary_sum += forward;
      regular_bin_sum += regular;
      nonzero_binary += forward != 0;
    }
  }
  output << ",\"status\":\"compared\",\"bins_compared\":" << std::size_t(columns) * rows
         << ",\"direct_mismatches\":" << direct_mismatch
         << ",\"transpose_mismatches\":" << transpose_mismatch
         << ",\"zero_based_mismatches\":" << zero_based_mismatch
         << ",\"zero_based_transpose_mismatches\":" << zero_based_transpose_mismatch
         << ",\"binary_sum\":" << binary_sum
         << ",\"root_regular_bin_sum\":" << regular_bin_sum
         << ",\"nonzero_binary_bins\":" << nonzero_binary
         << ",\"root_entries\":" << histogram->GetEntries()
         << ",\"interpretation\":\"Export-content comparison only; not event provenance or independent counts.\"}";
}

void compare_matrix_snapshot() {
  std::ofstream output("outputs/l4/20261101-133ce-southafrica-data-audit/matrix-content-audit.json");
  output << std::setprecision(17);
  output << "{\"schema_version\":1,\"integer_format\":\"native-int32-little-endian\","
            "\"comparisons\":[";
  struct Candidate {
    const char *root_file;
    const char *object;
    const char *binary;
  };
  const std::vector<Candidate> candidates = {
      {"g45allmatprompt.root", "g45allmatprompt", "m4b/g45allmatprompt.m4b"},
      {"g90allmatprompt.root", "g90allmatprompt", "m4b/g90allmatprompt.m4b"},
      {"gg.root", "hroot", "ggmatprompt.m4b"},
      {"gg.root", "hroot", "m4b/ggmat.m4b"},
      {"hgg.root", "hgg", "m4b/hggmatprompt.m4b"},
      {"hgg.root", "hgg", "m4b/hggmat.m4b"},
      {"vgg.root", "vgg", "m4b/vggmatprompt.m4b"},
      {"vgg.root", "vgg", "m4b/vggmat.m4b"},
  };
  bool first = true;
  for (const auto &candidate : candidates) {
    if (!first)
      output << ",";
    compare_pair(output, candidate.root_file, candidate.object, candidate.binary);
    first = false;
  }
  output << "]}\n";
  std::cout << "Wrote private matrix-content-audit.json with "
            << candidates.size() << " content comparisons" << std::endl;
}
