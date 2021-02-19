% University of Georgia Linguistics document class ============================
%
%   Written by Jonathan Crum, UGA Dept. of Linguistics
%
%   Based on the Semantics & Pragmatics document class (sp.cls)
%    by Kai von Fintel, Christopher Potts, and Chung-chieh Shan
%
% =============================================================================

% Changelog ===================================================================
%
% 2021-01-18: v1.0, UGA Linguistics document class started


% Outline =====================================================================
%
%   Option Declarations
%   Required Packages
%   Metadata
%   Page Dimensions
%   Title
%   Running Headers
%   Frontmatter
%   Sectioning
%   Footnotes
%   Bibliography
%   Backmatter
%   Other Environments
%   Useful Macros


% =============================================================================
\NeedsTeXFormat{LaTeX2e}[1994/06/01]
\ProvidesClass{ugaling}[2021/01/18 v.1.0 Class for UGA Linguistics]
% =============================================================================


% Option Declarations =========================================================

\newif \if@lucida   \@lucidafalse
\newif \if@cm       \@cmtrue
\newif \if@times    \@timestrue
\newif \if@final    \@finalfalse
\newif \if@biblatex \@biblatexfalse
\newif \if@linguex  \@linguexfalse
\newif \if@expex    \@expexfalse

\DeclareOption*[\PassOptionsToClass{\CurrentOption}{article}]

\newcommand{\@sizeoption@err}{\ClassError{ugaling}
    {Cannot use size option \CurrentOption}
    {The UGA Linguistics style requires (and automatically loads) 12pt text}}

\DeclareOption{10pt}{\@sizeoption@err}
\DeclareOption{11pt}{\@sizeoption@err}

%               Pass in     Set...
\DeclareOption{ lucida   }{ \@lucidatrue   \@timesfalse \@cmfalse }
\DeclareOption{ times    }{ \@lucidafalse  \@timestrue  \@cmfalse }
\DeclareOption{ cm       }{ \@lucidafalse  \@timesfalse \@cmtrue  }
\DeclareOption{ final    }{ \@finaltrue                           }
\DeclareOption{ biblatex }{ \@biblatextrue                        }
\DeclareOption{ linguex  }{ \@linguextrue                         }
\DeclareOption{ expex    }{ \@expextrue                           }

% Execute the default option
\ExecuteOptions{times}
\ProcessOptions\relax
\LoadClass[12pt,twoside]{article}

% Check that we're using Lucida.
\if@lucida
    \IfFileExists{lucimatx.sty}{
        % Do nothing
    }{
        % Else...
        \ClassWarning{ugaling.cls}{
            Lucida requested but cannot find font; falling back to Times.
        }
        \@lucidafalse \@timestrue
    }
\fi

% If we are using Lucida...
\if@lucida
    \RequirePackage[
        romanfamily=bright-osf,
        scale=0.9,
        stdmathdigits=true
    ]{lucimatx}
    \linespread{1.05}
    \let\llbracket\ldbrack
    \let\rrbracket\rdbrack
    % The default textbullet is too small.
    \DeclareTextCommand{\textbullet}{\encodingdefault}{\UseTextSymbol{OMS}\textbullet}
    % The default, 103, is too short.
    \DeclareMathSymbol{\nLeftrightarrow}{\mathrel}{\arrows}{105}

% Otherwise...
\else
    \IfFileExists{stmaryrd.sty}{\RequirePackage{stmaryrd}}{
        \ClassWarning{ugaling.cls}{
            stmaryrd required but not available; double brackets may be rendered incorrectly.
        }
        % If we can't render the actual double brackets, we'll hack it.
        % Using [\![ ... ]\!] reduces the space between the two brackets to roughly
        % mimic the double brackets.
        \newcommand{\llbracket}{\ensuremath{\left [\!\left [}}
        \newcommand{\rrbracket}{\ensuremath{\right ]\!\right ]}}
    }
    \RequirePackage{textcomp}   % Text Companion fonts
    \RequirePackage{amssymb}    % Part of amsfonts - extended fonts for mathematics
\fi

% If we end up falling back to Times, use a different math package.
\if@times
    \RequirePackage{mathptmx}
\fi

% Strong widow and orphan control
% ... sounds like the plot to a Charles Dickens novel.
\clubpenalty10000
\widowpenalty10000

% French spacing
\frenchspacing

% Requires Packages ===========================================================
% Metadata ====================================================================
% Page Dimensions =============================================================
% Title =======================================================================
% Running Headers =============================================================
% Frontmatter =================================================================
% Sectioning ==================================================================
% Footnotes ===================================================================
% Bibliography ================================================================
% Backmatter ==================================================================
% Other Environments ==========================================================
% Useful Macros ===============================================================
