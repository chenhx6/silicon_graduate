/*
Extracted ROOT v5-22-00 method expressions.
TH1: Copyright (C) 1995-2000, Rene Brun and Fons Rademakers. All rights reserved.
TSpectrum: Author Miroslav Morhac, repackaged by R. Brun.
See ROOT v5-22-00 LICENSE and README/CREDITS at the pinned source repository.
Source commit a365d2fa4cdc4fea91420c400280dc9fc7c64214.
Diagnostic adapter and fixture by this Wiki run; current ROOT helpers, not old full binary.
*/
// Diagnostic extraction of ROOT v5-22-00 methods; ROOT copyright retained in source manifests.
// Hybrid fixture: original method expressions, current ROOT histogram/TMath/TString helpers.
#include <TH1D.h>
#include <TMath.h>
#include <TString.h>
#include <TList.h>
#include <TVirtualPad.h>
#include <TROOT.h>
#include <iostream>
#include <iomanip>
#include <vector>
class LegacyHist: public TH1D {public: using TH1D::TH1D; void SmoothOld(Int_t ntimes=1,Option_t* option=(Option_t*)"");};
class LegacySpectrum: public TObject {public:
 enum {kBackOrder2=0,kBackOrder4=1,kBackOrder6=2,kBackOrder8=3,kBackIncreasingWindow=0,kBackDecreasingWindow=1,kBackSmoothing3=3,kBackSmoothing5=5,kBackSmoothing7=7,kBackSmoothing9=9,kBackSmoothing11=11,kBackSmoothing13=13,kBackSmoothing15=15};
 TH1* Background(const TH1*,int,Option_t*);
 const char* Background(float*,int,int,int,int,bool,int,bool);
};
void  legacy_smooth_array(Int_t nn, Double_t *xx, Int_t ntimes)
{
   // smooth array xx, translation of Hbook routine hsmoof.F
   // based on algorithm 353QH twice presented by J. Friedman
   // in Proc.of the 1974 CERN School of Computing, Norway, 11-24 August, 1974.

   Int_t ii, jj, ik, jk, kk, nn2;
   Double_t hh[6] = {0,0,0,0,0,0};
   Double_t *yy = new Double_t[nn];
   Double_t *zz = new Double_t[nn];
   Double_t *rr = new Double_t[nn];

   for (Int_t pass=0;pass<ntimes;pass++) {
      // first copy original data into temp array

      for (ii = 0; ii < nn; ii++) {
         yy[ii] = xx[ii];
      }

      //  do 353 i.e. running median 3, 5, and 3 in a single loop
      for  (kk = 1; kk <= 3; kk++)  {
         ik = 0;
         if  (kk == 2)  ik = 1;
         nn2 = nn - ik - 1;
         // do all elements beside the first and last point for median 3
         //  and first two and last 2 for median 5
         for  (ii = ik + 1; ii < nn2; ii++)  {
            for  (jj = 0; jj < 3; jj++)   {
               hh[jj] = yy[ii + jj - 1];
            }
            zz[ii] = TMath::Median(3 + 2*ik, hh);
         }

         if  (kk == 1)  {   // first median 3
            // first point
            hh[0] = 3*yy[1] - 2*yy[2];
            hh[1] = yy[0];
            hh[2] = yy[1];
            zz[0] = TMath::Median(3, hh);
            // last point
            hh[0] = yy[nn - 2];
            hh[1] = yy[nn - 1];
            hh[2] = 3*yy[nn - 2] - 2*yy[nn - 3];
            zz[nn - 1] = TMath::Median(3, hh);
         }
         if  (kk == 2)  {   //  median 5
            //  first point remains the same
            zz[0] = yy[0];
            for  (ii = 0; ii < 3; ii++) {
               hh[ii] = yy[ii];
            }
            zz[1] = TMath::Median(3, hh);
            // last two points
            for  (ii = 0; ii < 3; ii++) {
               hh[ii] = yy[nn - 3 + ii];
            }
            zz[nn - 2] = TMath::Median(3, hh);
            zz[nn - 1] = yy[nn - 1];
         }
      }

      // quadratic interpolation for flat segments
      for (ii = 2; ii < (nn - 2); ii++) {
         if  (zz[ii - 1] != zz[ii]) continue;
         if  (zz[ii] != zz[ii + 1]) continue;
         hh[0] = zz[ii - 2] - zz[ii];
         hh[1] = zz[ii + 2] - zz[ii];
         if  (hh[0] * hh[1] < 0) continue;
         jk = 1;
         if  ( TMath::Abs(hh[1]) > TMath::Abs(hh[0]) ) jk = -1;
         yy[ii] = -0.5*zz[ii - 2*jk] + zz[ii]/0.75 + zz[ii + 2*jk] /6.;
         yy[ii + jk] = 0.5*(zz[ii + 2*jk] - zz[ii - 2*jk]) + zz[ii];
      }

      // running means
      for  (ii = 1; ii < nn - 1; ii++) {
         rr[ii] = 0.25*yy[ii - 1] + 0.5*yy[ii] + 0.25*yy[ii + 1];
      }
      rr[0] = yy[0];
      rr[nn - 1] = yy[nn - 1];

      // now do the same for residuals

      for  (ii = 0; ii < nn; ii++)  {
         yy[ii] = xx[ii] - rr[ii];
      }

      //  do 353 i.e. running median 3, 5, and 3 in a single loop
      for  (kk = 1; kk <= 3; kk++)  {
         ik = 0;
         if  (kk == 2)  ik = 1;
         nn2 = nn - ik - 1;
         // do all elements beside the first and last point for median 3
         //  and first two and last 2 for median 5
         for  (ii = ik + 1; ii < nn2; ii++)  {
            for  (jj = 0; jj < 3; jj++) {
               hh[jj] = yy[ii + jj - 1];
            }
            zz[ii] = TMath::Median(3 + 2*ik, hh);
         }

         if  (kk == 1)  {   // first median 3
            // first point
            hh[0] = 3*yy[1] - 2*yy[2];
            hh[1] = yy[0];
            hh[2] = yy[1];
            zz[0] = TMath::Median(3, hh);
            // last point
            hh[0] = yy[nn - 2];
            hh[1] = yy[nn - 1];
            hh[2] = 3*yy[nn - 2] - 2*yy[nn - 3];
            zz[nn - 1] = TMath::Median(3, hh);
         }
         if  (kk == 2)  {   //  median 5
            //  first point remains the same
            zz[0] = yy[0];
            for  (ii = 0; ii < 3; ii++) {
               hh[ii] = yy[ii];
            }
            zz[1] = TMath::Median(3, hh);
            // last two points
            for  (ii = 0; ii < 3; ii++) {
               hh[ii] = yy[nn - 3 + ii];
            }
            zz[nn - 2] = TMath::Median(3, hh);
            zz[nn - 1] = yy[nn - 1];
         }
      }

      // quadratic interpolation for flat segments
      for (ii = 2; ii < (nn - 2); ii++) {
         if  (zz[ii - 1] != zz[ii]) continue;
         if  (zz[ii] != zz[ii + 1]) continue;
         hh[0] = zz[ii - 2] - zz[ii];
         hh[1] = zz[ii + 2] - zz[ii];
         if  (hh[0] * hh[1] < 0) continue;
         jk = 1;
         if  ( TMath::Abs(hh[1]) > TMath::Abs(hh[0]) ) jk = -1;
         yy[ii] = -0.5*zz[ii - 2*jk] + zz[ii]/0.75 + zz[ii + 2*jk]/6.;
         yy[ii + jk] = 0.5*(zz[ii + 2*jk] - zz[ii - 2*jk]) + zz[ii];
      }

      // running means
      for  (ii = 1; ii < (nn - 1); ii++) {
         zz[ii] = 0.25*yy[ii - 1] + 0.5*yy[ii] + 0.25*yy[ii + 1];
      }
      zz[0] = yy[0];
      zz[nn - 1] = yy[nn - 1];

      //  add smoothed xx and smoothed residuals

      for  (ii = 0; ii < nn; ii++) {
         if (xx[ii] < 0) xx[ii] = rr[ii] + zz[ii];
         else            xx[ii] = TMath::Abs(rr[ii] + zz[ii]);
      }
   }
   delete [] yy;
   delete [] zz;
   delete [] rr;
}


// ------------------------------------------------------------------------
void  LegacyHist::SmoothOld(Int_t ntimes, Option_t *option)
{
   // Smooth bin contents of this histogram.
   // if option contains "R" smoothing is applied only to the bins
   // defined in the X axis range (default is to smooth all bins)
   // Bin contents are replaced by their smooth values.
   // Errors (if any) are not modified.
   // the smoothing procedure is repeated ntimes (default=1)

   if (fDimension != 1) {
      Error("Smooth","Smooth only supported for 1-d histograms");
      return;
   }
   Int_t nbins = fXaxis.GetNbins();
   Int_t firstbin = 1, lastbin = nbins;
   TString opt = option;
   opt.ToLower();
   if (opt.Contains("r")) {
      firstbin= fXaxis.GetFirst();
      lastbin  = fXaxis.GetLast();
   }
   nbins = lastbin - firstbin + 1;
   Double_t *xx = new Double_t[nbins];
   Double_t nent = fEntries;
   Int_t i;
   for (i=0;i<nbins;i++) {
      xx[i] = GetBinContent(i+firstbin);
   }

   legacy_smooth_array(nbins,xx,ntimes);

   for (i=0;i<nbins;i++) {
      SetBinContent(i+firstbin,xx[i]);
   }
   fEntries = nent;
   delete [] xx;

   if (gPad) gPad->Modified();
}


// ------------------------------------------------------------------------
TH1 *LegacySpectrum::Background(const TH1 * h, int numberIterations, Option_t * option)
{
//   ONE-DIMENSIONAL BACKGROUND ESTIMATION FUNCTION
//   This function calculates the background spectrum in the input histogram h.
//   The background is returned as a histogram.
//
//   Function parameters:
//   -h: input 1-d histogram
//   -numberIterations, (default value = 20)
//      Increasing numberIterations make the result smoother and lower.
//   -option: may contain one of the following options
//      - to set the direction parameter
//        "BackIncreasingWindow". By default the direction is BackDecreasingWindow
//      - filterOrder-order of clipping filter,  (default "BackOrder2"
//                  -possible values= "BackOrder4"
//                                    "BackOrder6"
//                                    "BackOrder8"
//      - "nosmoothing"- if selected, the background is not smoothed
//           By default the background is smoothed.
//      - smoothWindow-width of smoothing window, (default is "BackSmoothing3")
//                  -possible values= "BackSmoothing5"
//                                    "BackSmoothing7"
//                                    "BackSmoothing9"
//                                    "BackSmoothing11"
//                                    "BackSmoothing13"
//                                    "BackSmoothing15"
//      - "Compton" if selected the estimation of Compton edge
//                  will be included.
//      - "same" : if this option is specified, the resulting background
//                 histogram is superimposed on the picture in the current pad.
//
//  NOTE that the background is only evaluated in the current range of h.
//  ie, if h has a bin range (set via h->GetXaxis()->SetRange(binmin,binmax),
//  the returned histogram will be created with the same number of bins
//  as the input histogram h, but only bins from binmin to binmax will be filled
//  with the estimated background.

   if (h == 0) return 0;
   Int_t dimension = h->GetDimension();
   if (dimension > 1) {
      Error("Search", "Only implemented for 1-d histograms");
      return 0;
   }
   TString opt = option;
   opt.ToLower();

   //set options
   Int_t direction = kBackDecreasingWindow;
   if (opt.Contains("backincreasingwindow")) direction = kBackIncreasingWindow;
   Int_t filterOrder = kBackOrder2;
   if (opt.Contains("backorder4")) filterOrder = kBackOrder4;
   if (opt.Contains("backorder6")) filterOrder = kBackOrder6;
   if (opt.Contains("backorder8")) filterOrder = kBackOrder8;
   Bool_t smoothing = kTRUE;
   if (opt.Contains("nosmoothing")) smoothing = kFALSE;
   Int_t smoothWindow = kBackSmoothing3;
   if (opt.Contains("backsmoothing5"))  smoothWindow = kBackSmoothing5;
   if (opt.Contains("backsmoothing7"))  smoothWindow = kBackSmoothing7;
   if (opt.Contains("backsmoothing9"))  smoothWindow = kBackSmoothing9;
   if (opt.Contains("backsmoothing11")) smoothWindow = kBackSmoothing11;
   if (opt.Contains("backsmoothing13")) smoothWindow = kBackSmoothing13;
   if (opt.Contains("backsmoothing15")) smoothWindow = kBackSmoothing15;
   Bool_t compton = kFALSE;
   if (opt.Contains("compton")) compton = kTRUE;

   Int_t first = h->GetXaxis()->GetFirst();
   Int_t last  = h->GetXaxis()->GetLast();
   Int_t size = last-first+1;
   Int_t i;
   Float_t * source = new float[size];
   for (i = 0; i < size; i++) source[i] = h->GetBinContent(i + first);

   //find background (source is input and in output contains the background
   Background(source,size,numberIterations, direction, filterOrder,smoothing,smoothWindow,compton);

   //create output histogram containing backgound
   //only bins in the range of the input histogram are filled
   Int_t nch = strlen(h->GetName());
   char *hbname = new char[nch+20];
   sprintf(hbname,"%s_background",h->GetName());
   TH1 *hb = (TH1*)h->Clone(hbname);
   hb->Reset();
   hb->GetListOfFunctions()->Delete();
   hb->SetLineColor(2);
   for (i=0; i< size; i++) hb->SetBinContent(i+first,source[i]);
   hb->SetEntries(size);

   //if option "same is specified, draw the result in the pad
   if (opt.Contains("same")) {
      if (gPad) delete gPad->GetPrimitive(hbname);
      hb->Draw("same");
   }
   delete [] source;
   delete [] hbname;
   return hb;
}

//______________________________________________________________________________
const char *LegacySpectrum::Background(float *spectrum, int ssize,
                                          int numberIterations,
                                          int direction, int filterOrder,
                                          bool smoothing,int smoothWindow,
                                          bool compton)
{
/////////////////////////////////////////////////////////////////////////////
//        ONE-DIMENSIONAL BACKGROUND ESTIMATION FUNCTION - GENERAL FUNCTION
//
//        This function calculates background spectrum from source spectrum.
//        The result is placed in the vector pointed by spe1945ctrum pointer.
//
//        Function parameters:
//        spectrum-pointer to the vector of source spectrum
//        ssize-length of the spectrum vector
//        numberIterations-maximal width of clipping window,
//        direction- direction of change of clipping window
//               - possible values=kBackIncreasingWindow
//                                 kBackDecreasingWindow
//        filterOrder-order of clipping filter,
//                  -possible values=kBackOrder2
//                                   kBackOrder4
//                                   kBackOrder6
//                                   kBackOrder8
//        smoothing- logical variable whether the smoothing operation
//               in the estimation of background will be included
//             - possible values=kFALSE
//                               kTRUE
//        smoothWindow-width of smoothing window,
//                  -possible values=kBackSmoothing3
//                                   kBackSmoothing5
//                                   kBackSmoothing7
//                                   kBackSmoothing9
//                                   kBackSmoothing11
//                                   kBackSmoothing13
//                                   kBackSmoothing15
//         compton- logical variable whether the estimation of Compton edge
//                  will be included
//             - possible values=kFALSE
//                               kTRUE
//
///////////////////////////////////////////////////////////////////////////////
//
//Begin_Html <!--
/* -->

<div class=Section1>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:20.0pt'>Background
estimation</span></b></p>

<p class=MsoNormal style='text-align:justify'><i><span style='font-size:18.0pt'>&nbsp;</span></i></p>

<p class=MsoNormal style='text-align:justify'><i><span style='font-size:18.0pt'>Goal:
Separation of useful information (peaks) from useless information (background)</span></i><span
style='font-size:18.0pt'> </span></p>

<p class=MsoNormal style='margin-left:36.0pt;text-indent:-18.0pt'><span
style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>method is based on Sensitive
Nonlinear Iterative Peak (SNIP) clipping algorithm</span></p>

<p class=MsoNormal style='margin-left:36.0pt;text-indent:-18.0pt'><span
style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'> new value in the channel i is
calculated</span></p>

<p class=MsoNormal>

<table cellpadding=0 cellspacing=0 align=left>
 <tr>
  <td width=53 height=23></td>
 </tr>
 <tr>
  <td></td>
  <td><img width=486 height=72 src="gif/TSpectrum_Background.gif"></td>
 </tr>
</table>

<span style='font-size:16.0pt'>&nbsp;</span></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<br clear=ALL>

<p class=MsoNormal style='text-align:justify'><span style='font-size:16.0pt'>where
p = 1, 2,
, numberIterations. In fact it represents second order difference
filter (-1,2,-1).</span></p>

<p class=MsoNormal><i><span style='font-size:18.0pt'>&nbsp;</span></i></p>

<p class=MsoNormal><i><span style='font-size:18.0pt'>Function:</span></i></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:18.0pt'>const
<a href="http://root.cern.ch/root/html/ListOtransTypes.html#char" target="_parent">char</a>*
<a
href="http://root.cern.ch/root/html/src/TSpectrum.cxx.html#TSpectrum:Background1General"
target="_parent">Background</a>(<a
href="http://root.cern.ch/root/html/ListOtransTypes.html#float" target="_parent">float</a>
*spectrum, <a href="http://root.cern.ch/root/html/ListOtransTypes.html#int"
target="_parent">int</a> ssize, <a
href="http://root.cern.ch/root/html/ListOtransTypes.html#int" target="_parent">int</a>
numberIterations, <a href="http://root.cern.ch/root/html/ListOtransTypes.html#int"
target="_parent">int</a> direction, <a
href="http://root.cern.ch/root/html/ListOtransTypes.html#int" target="_parent">int</a>
filterOrder,  <a href="http://root.cern.ch/root/html/ListOtransTypes.html#bool"
target="_parent">bool</a> smoothing,  <a
href="http://root.cern.ch/root/html/ListOtransTypes.html#int" target="_parent">int</a>
smoothingWindow, <a href="http://root.cern.ch/root/html/ListOtransTypes.html#bool"
target="_parent">bool</a> compton)  </span></b></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal style='text-align:justify'><span style='font-size:16.0pt'>This
function calculates background spectrum from the source spectrum.  The result
is placed in the vector pointed by spectrum pointer.  One can also change the
direction of the change of the clipping window, the order of the clipping
filter, to include smoothing, to set width of smoothing window and to include
the estimation of Compton edges.</span><span style='font-size:18.0pt'> </span><span
style='font-size:16.0pt'>On successful completion it returns 0. On error it
returns pointer to the string describing error.</span></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><i><span style='font-size:16.0pt;color:red'>Parameters:</span></i></p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>spectrum</span></b>-pointer
to the vector of source spectrum                  </p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>ssize</span></b>-length
of the spectrum vector                                 </p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>numberIterations</span></b>-maximal
width of clipping window,                                 </p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>direction</span></b>-
direction of change of clipping window                  </p>

<p class=MsoNormal>               - possible
values=kBackIncreasingWindow                      </p>

<p class=MsoNormal>                                            kBackDecreasingWindow
</p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>filterOrder</span></b>-order
of clipping filter,                              </p>

<p class=MsoNormal>                  -possible
values=kBackOrder2                              </p>

<p class=MsoNormal>                                              kBackOrder4
</p>

<p class=MsoNormal>                                              kBackOrder6
</p>

<p class=MsoNormal>                                              kBackOrder8
</p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>smoothing</span></b>-
logical variable whether the smoothing operation in the estimation of </p>

<p class=MsoNormal>               background will be included              </p>

<p class=MsoNormal>             - possible
values=kFALSE                        </p>

<p class=MsoNormal>                                          kTRUE
             </p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>smoothWindow</span></b>-width
of smoothing window,                            </p>

<p class=MsoNormal>                  -possible
values=kBackSmoothing3                          </p>

<p class=MsoNormal>                                             kBackSmoothing5
</p>

<p class=MsoNormal>                                             kBackSmoothing7
</p>

<p class=MsoNormal>                                             kBackSmoothing9
</p>

<p class=MsoNormal>                                             kBackSmoothing11
   </p>

<p class=MsoNormal>                                             kBackSmoothing13
</p>

<p class=MsoNormal>                                             kBackSmoothing15
</p>

<p class=MsoNormal>        <b><span style='font-size:14.0pt'>compton</span></b>-
logical variable whether the estimation of Compton edge   will be
included                                           </p>

<p class=MsoNormal>             - possible
values=kFALSE                          </p>

<p class=MsoNormal>                                          kTRUE
</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><b><i><span style='font-size:18.0pt'>References:</span></i></b></p>

<p class=MsoNormal style='text-align:justify'><span style='font-size:16.0pt'>[1]
C. G Ryan et al.: SNIP, a statistics-sensitive background treatment for the
quantitative analysis of PIXE spectra in geoscience applications. NIM, B34
(1988), 396-402.</span></p>

<p class=MsoNormal style='text-align:justify'><span style='font-size:16.0pt'>[2]
</span><span lang=SK style='font-size:16.0pt'> M. Morhá&#269;, J. Kliman, V.
Matouek, M. Veselský, I. Turzo</span><span style='font-size:16.0pt'>.:
Background elimination methods for multidimensional gamma-ray spectra. NIM,
A401 (1997) 113-132.</span></p>

<p class=MsoNormal style='text-align:justify'><span style='font-size:16.0pt'>[3]
D. D. Burgess, R. J. Tervo: Background estimation for gamma-ray spectroscopy.
NIM 214 (1983), 431-434. </span></p>

</div>

<!-- */
// --> End_Html
//Begin_Html <!--
/* -->
<div class=Section2>

<p class=MsoNormal><i><span style='font-size:18.0pt'>Example 1 script
Background_incr.c :</span></i></p>

<p class=MsoNormal><img width=601 height=407
src="gif/TSpectrum_Background_incr.jpg"></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt'>Figure
1 Example of the estimation of background for number of iterations=6. Original
spectrum is shown in black color, estimated background in red color.</span></b></p>

<p class=MsoNormal><b><span style='font-size:14.0pt;color:green'>&nbsp;</span></b></p>

<p class=MsoNormal><b><span style='font-size:16.0pt;color:green'>Script:</span></b></p>

<p class=MsoNormal>// Example to illustrate the background estimator (class
TSpectrum).</p>

<p class=MsoNormal>// To execute this example, do</p>

<p class=MsoNormal>// root &gt; .x Background_incr.C</p>

<p class=MsoNormal>#include &lt;TSpectrum&gt; </p>

<p class=MsoNormal>void Background_incr() {</p>

<p class=MsoNormal>   Int_t i;</p>

<p class=MsoNormal>   Double_t nbins = 256;</p>

<p class=MsoNormal>   Double_t xmin  = 0;</p>

<p class=MsoNormal>   Double_t xmax  = (Double_t)nbins;</p>

<p class=MsoNormal>   Float_t * source = new float[nbins];</p>

<p class=MsoNormal>   TH1F *back = new
TH1F(&quot;back&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d = new
TH1F(&quot;d&quot;,&quot;&quot;,nbins,xmin,xmax);      </p>

<p class=MsoNormal>   TFile *f = new
TFile(&quot;spectra\\TSpectrum.root&quot;);</p>

<p class=MsoNormal>   back=(TH1F*) f-&gt;Get(&quot;back1;1&quot;);</p>

<p class=MsoNormal>   TCanvas *Background = gROOT-&gt;GetListOfCanvases()-&gt;FindObject(&quot;Background&quot;);</p>

<p class=MsoNormal>   if (!Background) Background = new
TCanvas(&quot;Background&quot;,&quot;Estimation of background with increasing
window&quot;,10,10,1000,700);</p>

<p class=MsoNormal>   back-&gt;Draw(&quot;L&quot;);</p>

<p class=MsoNormal>   TSpectrum *s = new TSpectrum();</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) source[i]=back-&gt;GetBinContent(i
+ 1); </p>

<p class=MsoNormal>   s-&gt;Background(source,nbins,6,kBackIncreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d-&gt;SetLineColor(kRed);</p>

<p class=MsoNormal>   d-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   }</p>

</div>

<!-- */
// --> End_Html
//Begin_Html <!--
/* -->
<div class=Section3>

<p class=MsoNormal><i><span style='font-size:18.0pt'>Example 2  script
Background_decr.c :</span></i></p>

<p class=MsoNormal style='text-align:justify'><span style='font-size:16.0pt'>In
Figure 1. one can notice that at the edges of the peaks the estimated
background goes under the peaks. An alternative approach is to decrease the
clipping window from a given value numberIterations to the value of one, which
is presented in this example. </span></p>

<p class=MsoNormal><img width=601 height=407
src="gif/TSpectrum_Background_decr.jpg"></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt'>Figure
2 Example of the estimation of background for numberIterations=6 using
decreasing clipping window algorithm. Original spectrum is shown in black
color, estimated background in red color.</span></b></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><b><span style='font-size:16.0pt;color:#339966'>Script:</span></b></p>

<p class=MsoNormal>// Example to illustrate the background estimator (class
TSpectrum).</p>

<p class=MsoNormal>// To execute this example, do</p>

<p class=MsoNormal>// root &gt; .x Background_decr.C</p>

<p class=MsoNormal>#include &lt;TSpectrum&gt;   </p>

<p class=MsoNormal>void Background_decr() {</p>

<p class=MsoNormal>   Int_t i;</p>

<p class=MsoNormal>   Double_t nbins = 256;</p>

<p class=MsoNormal>   Double_t xmin  = 0;</p>

<p class=MsoNormal>   Double_t xmax  = (Double_t)nbins;</p>

<p class=MsoNormal>   Float_t * source = new float[nbins];</p>

<p class=MsoNormal>   TH1F *back = new
TH1F(&quot;back&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d = new
TH1F(&quot;d&quot;,&quot;&quot;,nbins,xmin,xmax);      </p>

<p class=MsoNormal>   TFile *f = new TFile(&quot;spectra\\TSpectrum.root&quot;);</p>

<p class=MsoNormal>   back=(TH1F*) f-&gt;Get(&quot;back1;1&quot;);</p>

<p class=MsoNormal>   TCanvas *Background =
gROOT-&gt;GetListOfCanvases()-&gt;FindObject(&quot;Background&quot;);</p>

<p class=MsoNormal>   if (!Background) Background = new
TCanvas(&quot;Background&quot;,&quot;Estimation of background with decreasing
window&quot;,10,10,1000,700);</p>

<p class=MsoNormal>   back-&gt;Draw(&quot;L&quot;);</p>

<p class=MsoNormal>   TSpectrum *s = new TSpectrum();</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=back-&gt;GetBinContent(i + 1); </p>

<p class=MsoNormal>   s-&gt;Background(source,nbins,6,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d-&gt;SetLineColor(kRed);</p>

<p class=MsoNormal>   d-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   }</p>

</div>

<!-- */
// --> End_Html
//Begin_Html <!--
/* -->
<div class=Section4>

<p class=MsoNormal><i><span style='font-size:18.0pt'>Example 3  script
Background_width.c :</span></i></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>the question is how to choose the
width of the clipping window, i.e.,  numberIterations   parameter. The
influence of this parameter on the estimated background is illustrated in
Figure 3.</span></p>

<p class=MsoNormal><img width=601 height=407
src="gif/TSpectrum_Background_width.jpg"></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt'>Figure
3 Example of the influence of clipping window width on the estimated background
for numberIterations=4 (red line), 6 (blue line) 8 (green line) using
decreasing clipping window algorithm.</span></b></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:18.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><i><span style='font-size:18.0pt'>in general one should set this
parameter so that the value 2*numberIterations+1 was greater than the widths
of preserved objects (peaks).</span></i></p>

<p class=MsoNormal style='text-align:justify'>&nbsp;</p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt;
color:#339966'>Script:</span></b></p>

<p class=MsoNormal>// Example to illustrate the influence of the clipping
window width on the estimated background</p>

<p class=MsoNormal>// To execute this example, do</p>

<p class=MsoNormal>// root &gt; .x Background_width.C</p>

<p class=MsoNormal>#include &lt;TSpectrum&gt;</p>

<p class=MsoNormal>void Background_width() {</p>

<p class=MsoNormal>   Int_t i;</p>

<p class=MsoNormal>   Double_t nbins = 256;</p>

<p class=MsoNormal>   Double_t xmin  = 0;</p>

<p class=MsoNormal>   Double_t xmax  = (Double_t)nbins;</p>

<p class=MsoNormal>   Float_t * source = new float[nbins];</p>

<p class=MsoNormal>   TH1F *h = new
TH1F(&quot;h&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d1 = new
TH1F(&quot;d1&quot;,&quot;&quot;,nbins,xmin,xmax);      </p>

<p class=MsoNormal>   TH1F *d2 = new
TH1F(&quot;d2&quot;,&quot;&quot;,nbins,xmin,xmax);         </p>

<p class=MsoNormal>   TH1F *d3 = new
TH1F(&quot;d3&quot;,&quot;&quot;,nbins,xmin,xmax);         </p>

<p class=MsoNormal>   TFile *f = new
TFile(&quot;spectra\\TSpectrum.root&quot;);</p>

<p class=MsoNormal>   h=(TH1F*) f-&gt;Get(&quot;back1;1&quot;);      </p>

<p class=MsoNormal>   TCanvas *background = gROOT-&gt;GetListOfCanvases()-&gt;FindObject(&quot;background&quot;);</p>

<p class=MsoNormal>   if (!background) background = new
TCanvas(&quot;background&quot;,&quot;Influence of clipping window width on the
estimated background&quot;,10,10,1000,700);</p>

<p class=MsoNormal>   h-&gt;Draw(&quot;L&quot;);</p>

<p class=MsoNormal>   TSpectrum *s = new TSpectrum();</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) source[i]=h-&gt;GetBinContent(i
+ 1);   </p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,4,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d1-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d1-&gt;SetLineColor(kRed);</p>

<p class=MsoNormal>   d1-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,6,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d2-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d2-&gt;SetLineColor(kBlue);</p>

<p class=MsoNormal>   d2-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,8,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d3-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d3-&gt;SetLineColor(kGreen);</p>

<p class=MsoNormal>   d3-&gt;Draw(&quot;SAME L&quot;);         </p>

<p class=MsoNormal>}</p>

</div>

<!-- */
// --> End_Html
//Begin_Html <!--
/* -->
<div class=Section5>

<p class=MsoNormal><i><span style='font-size:18.0pt'>Example 4  script
Background_width2.c :</span></i></p>

<p class=MsoNormal style='margin-left:36.0pt;text-indent:-18.0pt'><span
style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>another example for very complex
spectrum is given in Figure 4.</span></p>

<p class=MsoNormal><img width=601 height=407
src="gif/TSpectrum_Background_width2.jpg"></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt'>Figure
4 Example of the influence of clipping window width on the estimated background
for numberIterations=10 (red line), 20 (blue line), 30 (green line) and 40
(magenta line) using decreasing clipping window algorithm.</span></b></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><b><span style='font-size:16.0pt;color:#339966'>Script:</span></b></p>

<p class=MsoNormal>// Example to illustrate the influence of the clipping
window width on the estimated background</p>

<p class=MsoNormal>// To execute this example, do</p>

<p class=MsoNormal>// root &gt; .x Background_width2.C</p>

<p class=MsoNormal>#include &lt;TSpectrum&gt;  </p>

<p class=MsoNormal>void Background_width2() {</p>

<p class=MsoNormal>   Int_t i;</p>

<p class=MsoNormal>   Double_t nbins = 4096;</p>

<p class=MsoNormal>   Double_t xmin  = 0;</p>

<p class=MsoNormal>   Double_t xmax  = (Double_t)4096;</p>

<p class=MsoNormal>   Float_t * source = new float[nbins];</p>

<p class=MsoNormal>   TH1F *h = new
TH1F(&quot;h&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d1 = new TH1F(&quot;d1&quot;,&quot;&quot;,nbins,xmin,xmax);
</p>

<p class=MsoNormal>   TH1F *d2 = new
TH1F(&quot;d2&quot;,&quot;&quot;,nbins,xmin,xmax);         </p>

<p class=MsoNormal>   TH1F *d3 = new
TH1F(&quot;d3&quot;,&quot;&quot;,nbins,xmin,xmax);         </p>

<p class=MsoNormal>   TH1F *d4 = new
TH1F(&quot;d4&quot;,&quot;&quot;,nbins,xmin,xmax);            </p>

<p class=MsoNormal>   TFile *f = new
TFile(&quot;spectra\\TSpectrum.root&quot;);</p>

<p class=MsoNormal>   h=(TH1F*) f-&gt;Get(&quot;back2;1&quot;);   </p>

<p class=MsoNormal>   TCanvas *background =
gROOT-&gt;GetListOfCanvases()-&gt;FindObject(&quot;background&quot;);</p>

<p class=MsoNormal>   if (!background) background = new
TCanvas(&quot;background&quot;,&quot;Influence of clipping window width on the
estimated background&quot;,10,10,1000,700);</p>

<p class=MsoNormal>   h-&gt;SetAxisRange(0,1000);</p>

<p class=MsoNormal>   h-&gt;SetMaximum(20000);</p>

<p class=MsoNormal>   h-&gt;Draw(&quot;L&quot;);</p>

<p class=MsoNormal>   TSpectrum *s = new TSpectrum();</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);   </p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,10,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
    </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d1-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d1-&gt;SetLineColor(kRed);</p>

<p class=MsoNormal>   d1-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>   s-&gt;Background(source,nbins,20,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d2-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d2-&gt;SetLineColor(kBlue);</p>

<p class=MsoNormal>   d2-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,30,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d3-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d3-&gt;SetLineColor(kGreen);</p>

<p class=MsoNormal>   d3-&gt;Draw(&quot;SAME L&quot;);         </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,10,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d4-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d4-&gt;SetLineColor(kMagenta);</p>

<p class=MsoNormal>   d4-&gt;Draw(&quot;SAME L&quot;);            </p>

<p class=MsoNormal>}</p>

</div>

<!-- */
// --> End_Html
//Begin_Html <!--
/* -->
<div class=Section6>

<p class=MsoNormal><i><span style='font-size:18.0pt'>Example 5  script
Background_order.c :</span></i></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>second order difference filter
removes linear (quasi-linear) background and preserves symmetrical peaks.</span></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>however if the shape of the
background is more complex one can employ higher-order clipping filters (see
example in Figure 5)</span></p>

<p class=MsoNormal><img width=601 height=407
src="gif/TSpectrum_Background_order.jpg"></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt'>Figure
5 Example of the influence of clipping filter difference order on the estimated
background for fNnumberIterations=40, 2-nd order red line, 4-th order blue
line, 6-th order green line and 8-th order magenta line, and using decreasing
clipping window algorithm.</span></b></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><b><span style='font-size:16.0pt;color:#339966'>Script:</span></b></p>

<p class=MsoNormal>// Example to illustrate the influence of the clipping
filter difference order on the estimated background</p>

<p class=MsoNormal>// To execute this example, do</p>

<p class=MsoNormal>// root &gt; .x Background_order.C</p>

<p class=MsoNormal>#include &lt;TSpectrum&gt;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>void Background_order() {</p>

<p class=MsoNormal>   Int_t i;</p>

<p class=MsoNormal>   Double_t nbins = 4096;</p>

<p class=MsoNormal>   Double_t xmin  = 0;</p>

<p class=MsoNormal>   Double_t xmax  = (Double_t)4096;</p>

<p class=MsoNormal>   Float_t * source = new float[nbins];</p>

<p class=MsoNormal>   TH1F *h = new
TH1F(&quot;h&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d1 = new
TH1F(&quot;d1&quot;,&quot;&quot;,nbins,xmin,xmax);      </p>

<p class=MsoNormal>   TH1F *d2 = new
TH1F(&quot;d2&quot;,&quot;&quot;,nbins,xmin,xmax);         </p>

<p class=MsoNormal>   TH1F *d3 = new
TH1F(&quot;d3&quot;,&quot;&quot;,nbins,xmin,xmax);         </p>

<p class=MsoNormal>   TH1F *d4 = new
TH1F(&quot;d4&quot;,&quot;&quot;,nbins,xmin,xmax);            </p>

<p class=MsoNormal>   TFile *f = new
TFile(&quot;spectra\\TSpectrum.root&quot;);</p>

<p class=MsoNormal>   h=(TH1F*) f-&gt;Get(&quot;back2;1&quot;);</p>

<p class=MsoNormal>   TCanvas *background =
gROOT-&gt;GetListOfCanvases()-&gt;FindObject(&quot;background&quot;);</p>

<p class=MsoNormal>   if (!background) background = new
TCanvas(&quot;background&quot;,&quot;Influence of clipping filter difference
order on the estimated background&quot;,10,10,1000,700);</p>

<p class=MsoNormal>   h-&gt;SetAxisRange(1220,1460);</p>

<p class=MsoNormal>   h-&gt;SetMaximum(11000);</p>

<p class=MsoNormal>   h-&gt;Draw(&quot;L&quot;);</p>

<p class=MsoNormal>   TSpectrum *s = new TSpectrum();</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);   </p>

<p class=MsoNormal>   s-&gt;Background(source,nbins,40,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
    </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d1-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d1-&gt;SetLineColor(kRed);</p>

<p class=MsoNormal>   d1-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>   s-&gt;Background(source,nbins,40,kBackDecreasingWindow,kBackOrder4,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d2-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d2-&gt;SetLineColor(kBlue);</p>

<p class=MsoNormal>   d2-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,40,kBackDecreasingWindow,kBackOrder6,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d3-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d3-&gt;SetLineColor(kGreen);</p>

<p class=MsoNormal>   d3-&gt;Draw(&quot;SAME L&quot;);         </p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);</p>

<p class=MsoNormal>   s-&gt;Background(source,nbins,40,kBackDecreasingWindow,kBackOrder8,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d4-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d4-&gt;SetLineColor(kMagenta);</p>

<p class=MsoNormal>   d4-&gt;Draw(&quot;SAME L&quot;);            </p>

<p class=MsoNormal>}</p>

</div>

</div>
<!-- */
// --> End_Html
//Begin_Html <!--
/* -->
<div class=Section7>

<p class=MsoNormal><i><span style='font-size:16.0pt'>Example 6  script
Background_smooth.c :</span></i></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>the estimate of the background can
be influenced by noise present in the spectrum. We proposed  the algorithm of
the background estimate with simultaneous smoothing</span></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>in the original algorithm without
smoothing, the estimated background snatches the lower spikes in the noise.
Consequently, the areas of peaks are biased by this error. </span></p>

<p class=MsoNormal style='text-indent:5.7pt'><img width=554 height=104
src="gif/TSpectrum_Background_smooth1.jpg"></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt'>Figure
7 Principle of background estimation algorithm with  simultaneous smoothing</span></b></p>

<p class=MsoNormal><img width=601 height=407
src="gif/TSpectrum_Background_smooth2.jpg"></p>

<p class=MsoNormal><b><span style='font-size:16.0pt'>Figure 8 Illustration of
non-smoothing (red line) and smoothing algorithm of background estimation (blue
line).</span></b></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><b><span style='font-size:16.0pt;color:#339966'>Script:</span></b></p>

<p class=MsoNormal>// Example to illustrate the background estimator (class
TSpectrum) including Compton edges.</p>

<p class=MsoNormal>// To execute this example, do</p>

<p class=MsoNormal>// root &gt; .x Background_smooth.C</p>

<p class=MsoNormal>#include &lt;TSpectrum&gt;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>void Background_smooth() {</p>

<p class=MsoNormal>   Int_t i;</p>

<p class=MsoNormal>   Double_t nbins = 4096;</p>

<p class=MsoNormal>   Double_t xmin  = 0;</p>

<p class=MsoNormal>   Double_t xmax  = (Double_t)nbins;</p>

<p class=MsoNormal>   Float_t * source = new float[nbins];</p>

<p class=MsoNormal>   TH1F *h = new
TH1F(&quot;h&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d1 = new TH1F(&quot;d1&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d2 = new
TH1F(&quot;d2&quot;,&quot;&quot;,nbins,xmin,xmax);                  </p>

<p class=MsoNormal>   TFile *f = new
TFile(&quot;spectra\\TSpectrum.root&quot;);</p>

<p class=MsoNormal>   h=(TH1F*) f-&gt;Get(&quot;back4;1&quot;);</p>

<p class=MsoNormal>   TCanvas *background =
gROOT-&gt;GetListOfCanvases()-&gt;FindObject(&quot;background&quot;);</p>

<p class=MsoNormal>   if (!background) background = new
TCanvas(&quot;background&quot;,&quot;Estimation of background with
noise&quot;,10,10,1000,700);</p>

<p class=MsoNormal>   h-&gt;SetAxisRange(3460,3830);   </p>

<p class=MsoNormal>   h-&gt;Draw(&quot;L&quot;);</p>

<p class=MsoNormal>   TSpectrum *s = new TSpectrum();</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);   </p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,6,kBackDecreasingWindow,kBackOrder2,kFALSE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d1-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d1-&gt;SetLineColor(kRed);</p>

<p class=MsoNormal>   d1-&gt;Draw(&quot;SAME L&quot;);</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);   </p>

<p class=MsoNormal>
s-&gt;Background(source,nbins,6,kBackDecreasingWindow,kBackOrder2,kTRUE,kBackSmoothing3,kFALSE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d2-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d2-&gt;SetLineColor(kBlue);</p>

<p class=MsoNormal>   d2-&gt;Draw(&quot;SAME L&quot;);      </p>

<p class=MsoNormal>}</p>

</div>

<!-- */
// --> End_Html
//Begin_Html <!--
/* -->
<div class=Section8>

<p class=MsoNormal><i><span style='font-size:16.0pt'>Example 8  script
Background_compton.c :</span></i></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>sometimes it is necessary to
include also the Compton edges into the estimate of the background. In Figure 8
we present the example of the synthetic spectrum with Compton edges. </span></p>

<p class=MsoNormal style='margin-left:36.0pt;text-align:justify;text-indent:
-18.0pt'><span style='font-size:16.0pt'><span style='font:7.0pt "Times New Roman"'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span><span style='font-size:16.0pt'>the background was estimated using
the 8-th order filter with the estimation of the Compton edges using decreasing
clipping window algorithm (numberIterations=10) with smoothing (
smoothingWindow=5).</span></p>

<p class=MsoNormal><img width=601 height=407
src="gif/TSpectrum_Background_compton.jpg"></p>

<p class=MsoNormal style='text-align:justify'><b><span style='font-size:16.0pt'>Figure
8 Example of the estimate of the background with Compton edges (red line) for
numberIterations=10, 8-th order difference filter, using decreasing clipping
window algorithm and smoothing (smoothingWindow=5).</span></b></p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal><b><span style='font-size:16.0pt;color:#339966'>Script:</span></b></p>

<p class=MsoNormal>// Example to illustrate the background estimator (class
TSpectrum) including Compton edges.</p>

<p class=MsoNormal>// To execute this example, do</p>

<p class=MsoNormal>// root &gt; .x Background_compton.C</p>

<p class=MsoNormal>#include &lt;TSpectrum&gt;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>void Background_compton() {</p>

<p class=MsoNormal>   Int_t i;</p>

<p class=MsoNormal>   Double_t nbins = 512;</p>

<p class=MsoNormal>   Double_t xmin  = 0;</p>

<p class=MsoNormal>   Double_t xmax  = (Double_t)nbins;</p>

<p class=MsoNormal>   Float_t * source = new float[nbins];</p>

<p class=MsoNormal>   TH1F *h = new
TH1F(&quot;h&quot;,&quot;&quot;,nbins,xmin,xmax);</p>

<p class=MsoNormal>   TH1F *d1 = new
TH1F(&quot;d1&quot;,&quot;&quot;,nbins,xmin,xmax);      </p>

<p class=MsoNormal>   TFile *f = new
TFile(&quot;spectra\\TSpectrum.root&quot;);</p>

<p class=MsoNormal>   h=(TH1F*) f-&gt;Get(&quot;back3;1&quot;);</p>

<p class=MsoNormal>   TCanvas *background =
gROOT-&gt;GetListOfCanvases()-&gt;FindObject(&quot;background&quot;);</p>

<p class=MsoNormal>   if (!background) background = new
TCanvas(&quot;background&quot;,&quot;Estimation of background with Compton edges under peaks&quot;,10,10,1000,700);</p>

<p class=MsoNormal>   h-&gt;Draw(&quot;L&quot;);</p>

<p class=MsoNormal>   TSpectrum *s = new TSpectrum();</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++)
source[i]=h-&gt;GetBinContent(i + 1);   </p>

<p class=MsoNormal>   s-&gt;Background(source,nbins,10,kBackDecreasingWindow,kBackOrder8,kTRUE,kBackSmoothing5,,kTRUE);
</p>

<p class=MsoNormal>   for (i = 0; i &lt; nbins; i++) d1-&gt;SetBinContent(i +
1,source[i]);   </p>

<p class=MsoNormal>   d1-&gt;SetLineColor(kRed);</p>

<p class=MsoNormal>   d1-&gt;Draw(&quot;SAME L&quot;);   </p>

<p class=MsoNormal>}</p>

</div>

<!-- */
// --> End_Html

   int i, j, w, bw, b1, b2, priz;
   float a, b, c, d, e, yb1, yb2, ai, av, men, b4, c4, d4, e4, b6, c6, d6, e6, f6, g6, b8, c8, d8, e8, f8, g8, h8, i8;
   if (ssize <= 0)
      return "Wrong Parameters";
   if (numberIterations < 1)
      return "Width of Clipping Window Must Be Positive";
   if (ssize < 2 * numberIterations + 1)
      return "Too Large Clipping Window";
   if (smoothing == kTRUE && smoothWindow != kBackSmoothing3 && smoothWindow != kBackSmoothing5 && smoothWindow != kBackSmoothing7 && smoothWindow != kBackSmoothing9 && smoothWindow != kBackSmoothing11 && smoothWindow != kBackSmoothing13 && smoothWindow != kBackSmoothing15)
      return "Incorrect width of smoothing window";
   float *working_space = new float[2 * ssize];
   for (i = 0; i < ssize; i++){
      working_space[i] = spectrum[i];
      working_space[i + ssize] = spectrum[i];
   }
   bw=(smoothWindow-1)/2;
   if (direction == kBackIncreasingWindow)
      i = 1;
   else if(direction == kBackDecreasingWindow)
      i = numberIterations;
   if (filterOrder == kBackOrder2) {
      do{
         for (j = i; j < ssize - i; j++) {
            if (smoothing == kFALSE){
               a = working_space[ssize + j];
               b = (working_space[ssize + j - i] + working_space[ssize + j + i]) / 2.0;
               if (b < a)
                  a = b;
               working_space[j] = a;
            }

            else if (smoothing == kTRUE){
               a = working_space[ssize + j];
               av = 0;
               men = 0;
               for (w = j - bw; w <= j + bw; w++){
                  if ( w >= 0 && w < ssize){
                     av += working_space[ssize + w];
                     men +=1;
                  }
               }
               av = av / men;
               b = 0;
               men = 0;
               for (w = j - i - bw; w <= j - i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     b += working_space[ssize + w];
                     men +=1;
                  }
               }
               b = b / men;
               c = 0;
               men = 0;
               for (w = j + i - bw; w <= j + i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     c += working_space[ssize + w];
                     men +=1;
                  }
               }
               c = c / men;
               b = (b + c) / 2;
               if (b < a)
                  av = b;
               working_space[j]=av;
            }
         }
         for (j = i; j < ssize - i; j++)
            working_space[ssize + j] = working_space[j];
         if (direction == kBackIncreasingWindow)
            i+=1;
         else if(direction == kBackDecreasingWindow)
            i-=1;
      }while((direction == kBackIncreasingWindow && i <= numberIterations) || (direction == kBackDecreasingWindow && i >= 1));
   }

   else if (filterOrder == kBackOrder4) {
      do{
         for (j = i; j < ssize - i; j++) {
            if (smoothing == kFALSE){
               a = working_space[ssize + j];
               b = (working_space[ssize + j - i] + working_space[ssize + j + i]) / 2.0;
               c = 0;
               ai = i / 2;
               c -= working_space[ssize + j - (int) (2 * ai)] / 6;
               c += 4 * working_space[ssize + j - (int) ai] / 6;
               c += 4 * working_space[ssize + j + (int) ai] / 6;
               c -= working_space[ssize + j + (int) (2 * ai)] / 6;
               if (b < c)
                  b = c;
               if (b < a)
                  a = b;
               working_space[j] = a;
            }

            else if (smoothing == kTRUE){
               a = working_space[ssize + j];
               av = 0;
               men = 0;
               for (w = j - bw; w <= j + bw; w++){
                  if ( w >= 0 && w < ssize){
                     av += working_space[ssize + w];
                     men +=1;
                  }
               }
               av = av / men;
               b = 0;
               men = 0;
               for (w = j - i - bw; w <= j - i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     b += working_space[ssize + w];
                     men +=1;
                  }
               }
               b = b / men;
               c = 0;
               men = 0;
               for (w = j + i - bw; w <= j + i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     c += working_space[ssize + w];
                     men +=1;
                  }
               }
               c = c / men;
               b = (b + c) / 2;
               ai = i / 2;
               b4 = 0, men = 0;
               for (w = j - (int)(2 * ai) - bw; w <= j - (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     b4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               b4 = b4 / men;
               c4 = 0, men = 0;
               for (w = j - (int)ai - bw; w <= j - (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     c4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               c4 = c4 / men;
               d4 = 0, men = 0;
               for (w = j + (int)ai - bw; w <= j + (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     d4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               d4 = d4 / men;
               e4 = 0, men = 0;
               for (w = j + (int)(2 * ai) - bw; w <= j + (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     e4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               e4 = e4 / men;
               b4 = (-b4 + 4 * c4 + 4 * d4 - e4) / 6;
               if (b < b4)
                  b = b4;
               if (b < a)
                  av = b;
               working_space[j]=av;
            }
         }
         for (j = i; j < ssize - i; j++)
            working_space[ssize + j] = working_space[j];
         if (direction == kBackIncreasingWindow)
            i+=1;
         else if(direction == kBackDecreasingWindow)
            i-=1;
      }while((direction == kBackIncreasingWindow && i <= numberIterations) || (direction == kBackDecreasingWindow && i >= 1));
   }

   else if (filterOrder == kBackOrder6) {
      do{
         for (j = i; j < ssize - i; j++) {
            if (smoothing == kFALSE){
               a = working_space[ssize + j];
               b = (working_space[ssize + j - i] + working_space[ssize + j + i]) / 2.0;
               c = 0;
               ai = i / 2;
               c -= working_space[ssize + j - (int) (2 * ai)] / 6;
               c += 4 * working_space[ssize + j - (int) ai] / 6;
               c += 4 * working_space[ssize + j + (int) ai] / 6;
               c -= working_space[ssize + j + (int) (2 * ai)] / 6;
               d = 0;
               ai = i / 3;
               d += working_space[ssize + j - (int) (3 * ai)] / 20;
               d -= 6 * working_space[ssize + j - (int) (2 * ai)] / 20;
               d += 15 * working_space[ssize + j - (int) ai] / 20;
               d += 15 * working_space[ssize + j + (int) ai] / 20;
               d -= 6 * working_space[ssize + j + (int) (2 * ai)] / 20;
               d += working_space[ssize + j + (int) (3 * ai)] / 20;
               if (b < d)
                  b = d;
               if (b < c)
                  b = c;
               if (b < a)
                  a = b;
               working_space[j] = a;
            }

            else if (smoothing == kTRUE){
               a = working_space[ssize + j];
               av = 0;
               men = 0;
               for (w = j - bw; w <= j + bw; w++){
                  if ( w >= 0 && w < ssize){
                     av += working_space[ssize + w];
                     men +=1;
                  }
               }
               av = av / men;
               b = 0;
               men = 0;
               for (w = j - i - bw; w <= j - i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     b += working_space[ssize + w];
                     men +=1;
                  }
               }
               b = b / men;
               c = 0;
               men = 0;
               for (w = j + i - bw; w <= j + i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     c += working_space[ssize + w];
                     men +=1;
                  }
               }
               c = c / men;
               b = (b + c) / 2;
               ai = i / 2;
               b4 = 0, men = 0;
               for (w = j - (int)(2 * ai) - bw; w <= j - (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     b4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               b4 = b4 / men;
               c4 = 0, men = 0;
               for (w = j - (int)ai - bw; w <= j - (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     c4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               c4 = c4 / men;
               d4 = 0, men = 0;
               for (w = j + (int)ai - bw; w <= j + (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     d4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               d4 = d4 / men;
               e4 = 0, men = 0;
               for (w = j + (int)(2 * ai) - bw; w <= j + (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     e4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               e4 = e4 / men;
               b4 = (-b4 + 4 * c4 + 4 * d4 - e4) / 6;
               ai = i / 3;
               b6 = 0, men = 0;
               for (w = j - (int)(3 * ai) - bw; w <= j - (int)(3 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     b6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               b6 = b6 / men;
               c6 = 0, men = 0;
               for (w = j - (int)(2 * ai) - bw; w <= j - (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     c6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               c6 = c6 / men;
               d6 = 0, men = 0;
               for (w = j - (int)ai - bw; w <= j - (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     d6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               d6 = d6 / men;
               e6 = 0, men = 0;
               for (w = j + (int)ai - bw; w <= j + (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     e6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               e6 = e6 / men;
               f6 = 0, men = 0;
               for (w = j + (int)(2 * ai) - bw; w <= j + (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     f6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               f6 = f6 / men;
               g6 = 0, men = 0;
               for (w = j + (int)(3 * ai) - bw; w <= j + (int)(3 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     g6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               g6 = g6 / men;
               b6 = (b6 - 6 * c6 + 15 * d6 + 15 * e6 - 6 * f6 + g6) / 20;
               if (b < b6)
                  b = b6;
               if (b < b4)
                  b = b4;
               if (b < a)
                  av = b;
               working_space[j]=av;
            }
         }
         for (j = i; j < ssize - i; j++)
            working_space[ssize + j] = working_space[j];
         if (direction == kBackIncreasingWindow)
            i+=1;
         else if(direction == kBackDecreasingWindow)
            i-=1;
      }while((direction == kBackIncreasingWindow && i <= numberIterations) || (direction == kBackDecreasingWindow && i >= 1));
   }

   else if (filterOrder == kBackOrder8) {
      do{
         for (j = i; j < ssize - i; j++) {
            if (smoothing == kFALSE){
               a = working_space[ssize + j];
               b = (working_space[ssize + j - i] + working_space[ssize + j + i]) / 2.0;
               c = 0;
               ai = i / 2;
               c -= working_space[ssize + j - (int) (2 * ai)] / 6;
               c += 4 * working_space[ssize + j - (int) ai] / 6;
               c += 4 * working_space[ssize + j + (int) ai] / 6;
               c -= working_space[ssize + j + (int) (2 * ai)] / 6;
               d = 0;
               ai = i / 3;
               d += working_space[ssize + j - (int) (3 * ai)] / 20;
               d -= 6 * working_space[ssize + j - (int) (2 * ai)] / 20;
               d += 15 * working_space[ssize + j - (int) ai] / 20;
               d += 15 * working_space[ssize + j + (int) ai] / 20;
               d -= 6 * working_space[ssize + j + (int) (2 * ai)] / 20;
               d += working_space[ssize + j + (int) (3 * ai)] / 20;
               e = 0;
               ai = i / 4;
               e -= working_space[ssize + j - (int) (4 * ai)] / 70;
               e += 8 * working_space[ssize + j - (int) (3 * ai)] / 70;
               e -= 28 * working_space[ssize + j - (int) (2 * ai)] / 70;
               e += 56 * working_space[ssize + j - (int) ai] / 70;
               e += 56 * working_space[ssize + j + (int) ai] / 70;
               e -= 28 * working_space[ssize + j + (int) (2 * ai)] / 70;
               e += 8 * working_space[ssize + j + (int) (3 * ai)] / 70;
               e -= working_space[ssize + j + (int) (4 * ai)] / 70;
               if (b < e)
                  b = e;
               if (b < d)
                  b = d;
               if (b < c)
                  b = c;
               if (b < a)
                  a = b;
               working_space[j] = a;
            }

            else if (smoothing == kTRUE){
               a = working_space[ssize + j];
               av = 0;
               men = 0;
               for (w = j - bw; w <= j + bw; w++){
                  if ( w >= 0 && w < ssize){
                     av += working_space[ssize + w];
                     men +=1;
                  }
               }
               av = av / men;
               b = 0;
               men = 0;
               for (w = j - i - bw; w <= j - i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     b += working_space[ssize + w];
                     men +=1;
                  }
               }
               b = b / men;
               c = 0;
               men = 0;
               for (w = j + i - bw; w <= j + i + bw; w++){
                  if ( w >= 0 && w < ssize){
                     c += working_space[ssize + w];
                     men +=1;
                  }
               }
               c = c / men;
               b = (b + c) / 2;
               ai = i / 2;
               b4 = 0, men = 0;
               for (w = j - (int)(2 * ai) - bw; w <= j - (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     b4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               b4 = b4 / men;
               c4 = 0, men = 0;
               for (w = j - (int)ai - bw; w <= j - (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     c4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               c4 = c4 / men;
               d4 = 0, men = 0;
               for (w = j + (int)ai - bw; w <= j + (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     d4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               d4 = d4 / men;
               e4 = 0, men = 0;
               for (w = j + (int)(2 * ai) - bw; w <= j + (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     e4 += working_space[ssize + w];
                     men +=1;
                  }
               }
               e4 = e4 / men;
               b4 = (-b4 + 4 * c4 + 4 * d4 - e4) / 6;
               ai = i / 3;
               b6 = 0, men = 0;
               for (w = j - (int)(3 * ai) - bw; w <= j - (int)(3 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     b6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               b6 = b6 / men;
               c6 = 0, men = 0;
               for (w = j - (int)(2 * ai) - bw; w <= j - (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     c6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               c6 = c6 / men;
               d6 = 0, men = 0;
               for (w = j - (int)ai - bw; w <= j - (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     d6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               d6 = d6 / men;
               e6 = 0, men = 0;
               for (w = j + (int)ai - bw; w <= j + (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     e6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               e6 = e6 / men;
               f6 = 0, men = 0;
               for (w = j + (int)(2 * ai) - bw; w <= j + (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     f6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               f6 = f6 / men;
               g6 = 0, men = 0;
               for (w = j + (int)(3 * ai) - bw; w <= j + (int)(3 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     g6 += working_space[ssize + w];
                     men +=1;
                  }
               }
               g6 = g6 / men;
               b6 = (b6 - 6 * c6 + 15 * d6 + 15 * e6 - 6 * f6 + g6) / 20;
               ai = i / 4;
               b8 = 0, men = 0;
               for (w = j - (int)(4 * ai) - bw; w <= j - (int)(4 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     b8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               b8 = b8 / men;
               c8 = 0, men = 0;
               for (w = j - (int)(3 * ai) - bw; w <= j - (int)(3 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     c8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               c8 = c8 / men;
               d8 = 0, men = 0;
               for (w = j - (int)(2 * ai) - bw; w <= j - (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     d8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               d8 = d8 / men;
               e8 = 0, men = 0;
               for (w = j - (int)ai - bw; w <= j - (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     e8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               e8 = e8 / men;
               f8 = 0, men = 0;
               for (w = j + (int)ai - bw; w <= j + (int)ai + bw; w++){
                  if (w >= 0 && w < ssize){
                     f8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               f8 = f8 / men;
               g8 = 0, men = 0;
               for (w = j + (int)(2 * ai) - bw; w <= j + (int)(2 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     g8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               g8 = g8 / men;
               h8 = 0, men = 0;
               for (w = j + (int)(3 * ai) - bw; w <= j + (int)(3 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     h8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               h8 = h8 / men;
               i8 = 0, men = 0;
               for (w = j + (int)(4 * ai) - bw; w <= j + (int)(4 * ai) + bw; w++){
                  if (w >= 0 && w < ssize){
                     i8 += working_space[ssize + w];
                     men +=1;
                  }
               }
               i8 = i8 / men;
               b8 = ( -b8 + 8 * c8 - 28 * d8 + 56 * e8 - 56 * f8 - 28 * g8 + 8 * h8 - i8)/70;
               if (b < b8)
                  b = b8;
               if (b < b6)
                  b = b6;
               if (b < b4)
                  b = b4;
               if (b < a)
                  av = b;
               working_space[j]=av;
            }
         }
         for (j = i; j < ssize - i; j++)
            working_space[ssize + j] = working_space[j];
         if (direction == kBackIncreasingWindow)
            i += 1;
         else if(direction == kBackDecreasingWindow)
            i -= 1;
      }while((direction == kBackIncreasingWindow && i <= numberIterations) || (direction == kBackDecreasingWindow && i >= 1));
   }

   if (compton == kTRUE) {
      for (i = 0, b2 = 0; i < ssize; i++){
         b1 = b2;
         a = working_space[i], b = spectrum[i];
         j = i;
         if (TMath::Abs(a - b) >= 1) {
            b1 = i - 1;
            if (b1 < 0)
               b1 = 0;
            yb1 = working_space[b1];
            for (b2 = b1 + 1, c = 0, priz = 0; priz == 0 && b2 < ssize; b2++){
               a = working_space[b2], b = spectrum[b2];
               c = c + b - yb1;
               if (TMath::Abs(a - b) < 1) {
                  priz = 1;
                  yb2 = b;
               }
            }
            if (b2 == ssize)
               b2 -= 1;
            yb2 = working_space[b2];
            if (yb1 <= yb2){
               for (j = b1, c = 0; j <= b2; j++){
                  b = spectrum[j];
                  c = c + b - yb1;
               }
               if (c > 1){
                  c = (yb2 - yb1) / c;
                  for (j = b1, d = 0; j <= b2 && j < ssize; j++){
                     b = spectrum[j];
                     d = d + b - yb1;
                     a = c * d + yb1;
                     working_space[ssize + j] = a;
                  }
               }
            }

            else{
               for (j = b2, c = 0; j >= b1; j--){
                  b = spectrum[j];
                  c = c + b - yb2;
               }
               if (c > 1){
                  c = (yb1 - yb2) / c;
                  for (j = b2, d = 0;j >= b1 && j >= 0; j--){
                     b = spectrum[j];
                     d = d + b - yb2;
                     a = c * d + yb2;
                     working_space[ssize + j] = a;
                  }
               }
            }
            i=b2;
         }
      }
   }

   for (j = 0; j < ssize; j++)
      spectrum[j] = working_space[ssize + j];
   delete[]working_space;
   return 0;
}


//_______________________________________________________________________________

void arr(const TH1& h,bool error){std::cout<<"[";for(int i=1;i<=h.GetNbinsX();i++){if(i>1)std::cout<<",";std::cout<<(error?h.GetBinError(i):h.GetBinContent(i));}std::cout<<"]";}
int main(){gROOT->SetBatch(true);std::cout<<std::setprecision(17)<<"{\"ROOT_helper_version\":\""<<gROOT->GetVersion()<<"\",\"cases\":[";
 for(int stored=0;stored<2;stored++){TH1::SetDefaultSumw2(stored);LegacyHist h((std::string("h")+std::to_string(stored)).c_str(),"design",21,0,21);for(int i=1;i<=21;i++)h.SetBinContent(i,10+(i%5)*3+(i==11?60:0));if(stored)for(int i=1;i<=21;i++)h.SetBinError(i,2+i*.1);if(stored)std::cout<<",";std::cout<<"{\"stored\":"<<stored<<",\"before_content\":";arr(h,false);std::cout<<",\"before_error\":";arr(h,true);h.SmoothOld();std::cout<<",\"after_smooth_content\":";arr(h,false);std::cout<<",\"after_smooth_error\":";arr(h,true);LegacySpectrum s;TH1* b=s.Background(&h,2,(Option_t*)"");std::cout<<",\"background_sumw2N\":"<<b->GetSumw2N()<<",\"background_content\":";arr(*b,false);std::cout<<",\"background_error\":";arr(*b,true);delete b;std::cout<<"}";}std::cout<<"]}\n";return 0;}
