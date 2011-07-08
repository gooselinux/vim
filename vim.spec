# used for CVS snapshots:
%define CVSDATE %{nil}
%if %{?WITH_SELINUX:0}%{!?WITH_SELINUX:1}
%define WITH_SELINUX 1
%endif
%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

%define withnetbeans 1

%define withvimspell 0
%define withhunspell 0
%define withruby 1

%define baseversion 7.2
#used for pre-releases:
%define beta %{nil}
%define vimdir vim72%{?beta}
%define patchlevel 411

Summary: The VIM editor
URL:     http://www.vim.org/
Name: vim
Version: %{baseversion}.%{beta}%{patchlevel}
Release: 1.5%{?dist}
License: Vim and GPLv2+ and BSD and LGPLv2+ and Open Publication
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{baseversion}%{?beta}%{?CVSDATE}.tar.bz2
Source1: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}%{?beta}-lang%{?CVSDATE}.tar.gz
Source2: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}%{?beta}-extra%{?CVSDATE}.tar.gz
Source3: gvim.desktop
Source4: vimrc
#Source5: ftp://ftp.vim.org/pub/vim/patches/README.patches
Source7: gvim16.png
Source8: gvim32.png
Source9: gvim48.png
Source10: gvim64.png
Source11: Changelog.rpm
Source12: vi_help.txt
%if %{withvimspell}
Source13: vim-spell-files.tar.bz2
%endif
Source14: spec-template
Source15: http://www.cvjb.de/comp/vim/forth.vim

# remove this for the next major version, CVE fixes:
Source16: ftp://ftp.vim.org/vol/2/vim/runtime/plugin/netrwPlugin.vim
Source17: ftp://ftp.vim.org/vol/2/vim/runtime/plugin/gzip.vim
Source18: ftp://ftp.vim.org/vol/2/vim/runtime/filetype.vim
Source19: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/zip.vim
Source20: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/tar.vim
Source21: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrwFileHandlers.vim
Source22: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrw.vim
Source23: ftp://ftp.vim.org/vol/2/vim/runtime/autoload/netrwSettings.vim

Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
Patch2004: vim-7.0-crv.patch
Patch2010: xxd-locale.patch
%if %{withhunspell}
Patch2011: vim-7.0-hunspell.patch
BuildRequires: hunspell-devel
%endif
# Patches 001 < 999 are patches from the base maintainer.
# If you're as lazy as me, generate the list using
# for i in `seq 1 14`; do printf "Patch%03d: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.%03d\n" $i $i; done
Patch001: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.001
Patch002: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.002
Patch003: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.003
Patch004: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.004
Patch005: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.005
Patch006: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.006
Patch007: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.007
Patch008: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.008
Patch009: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.009
Patch010: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.010
Patch011: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.011
Patch012: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.012
Patch013: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.013
Patch014: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.014
Patch015: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.015
Patch016: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.016
Patch017: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.017
Patch018: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.018
Patch019: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.019
Patch020: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.020
Patch021: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.021
Patch022: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.022
Patch023: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.023
Patch024: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.024
Patch025: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.025
Patch026: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.026
Patch027: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.027
Patch028: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.028
Patch029: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.029
Patch030: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.030
Patch031: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.031
Patch032: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.032
Patch033: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.033
Patch034: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.034
Patch035: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.035
Patch036: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.036
Patch037: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.037
Patch038: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.038
Patch039: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.039
Patch040: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.040
Patch041: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.041
Patch042: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.042
Patch043: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.043
Patch044: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.044
Patch045: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.045
Patch046: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.046
Patch047: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.047
Patch048: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.048
Patch049: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.049
Patch050: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.050
Patch051: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.051
Patch052: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.052
Patch053: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.053
Patch054: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.054
Patch055: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.055
Patch056: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.056
Patch057: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.057
Patch058: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.058
Patch059: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.059
Patch060: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.060
Patch061: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.061
Patch062: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.062
Patch063: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.063
Patch064: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.064
Patch065: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.065
Patch066: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.066
Patch067: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.067
Patch068: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.068
Patch069: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.069
Patch070: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.070
Patch071: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.071
Patch072: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.072
Patch073: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.073
Patch074: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.074
Patch075: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.075
Patch076: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.076
Patch077: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.077
Patch078: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.078
Patch079: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.079
Patch080: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.080
Patch081: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.081
Patch082: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.082
Patch083: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.083
Patch084: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.084
Patch085: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.085
Patch086: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.086
Patch087: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.087
Patch088: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.088
Patch089: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.089
Patch090: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.090
Patch091: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.091
Patch092: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.092
Patch093: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.093
Patch094: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.094
Patch095: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.095
Patch096: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.096
Patch097: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.097
Patch098: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.098
Patch099: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.099
Patch100: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.100
Patch101: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.101
Patch102: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.102
Patch103: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.103
Patch104: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.104
Patch105: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.105
Patch106: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.106
Patch107: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.107
Patch108: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.108
Patch109: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.109
Patch110: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.110
Patch111: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.111
Patch112: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.112
Patch113: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.113
Patch114: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.114
Patch115: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.115
Patch116: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.116
Patch117: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.117
Patch118: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.118
Patch119: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.119
Patch120: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.120
Patch121: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.121
Patch122: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.122
Patch123: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.123
Patch124: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.124
Patch125: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.125
Patch126: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.126
Patch127: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.127
Patch128: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.128
Patch129: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.129
Patch130: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.130
Patch131: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.131
Patch132: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.132
Patch133: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.133
Patch134: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.134
Patch135: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.135
Patch136: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.136
Patch137: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.137
Patch138: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.138
Patch139: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.139
Patch140: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.140
Patch141: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.141
Patch142: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.142
Patch143: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.143
Patch144: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.144
Patch145: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.145
Patch146: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.146
Patch147: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.147
Patch148: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.148
Patch149: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.149
Patch150: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.150
Patch151: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.151
Patch152: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.152
Patch153: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.153
Patch154: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.154
Patch155: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.155
Patch156: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.156
Patch157: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.157
Patch158: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.158
Patch159: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.159
Patch160: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.160
Patch161: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.161
Patch162: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.162
Patch163: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.163
Patch164: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.164
Patch165: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.165
Patch166: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.166
Patch167: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.167
Patch168: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.168
Patch169: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.169
Patch170: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.170
Patch171: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.171
Patch172: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.172
Patch173: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.173
Patch174: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.174
Patch175: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.175
Patch176: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.176
Patch177: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.177
Patch178: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.178
Patch179: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.179
Patch180: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.180
Patch181: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.181
Patch182: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.182
Patch183: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.183
Patch184: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.184
Patch185: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.185
Patch186: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.186
Patch187: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.187
Patch188: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.188
Patch189: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.189
Patch190: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.190
Patch191: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.191
Patch192: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.192
Patch193: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.193
Patch194: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.194
Patch195: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.195
Patch196: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.196
Patch197: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.197
Patch198: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.198
Patch199: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.199
Patch200: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.200
Patch201: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.201
Patch202: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.202
Patch203: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.203
Patch204: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.204
Patch205: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.205
Patch206: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.206
Patch207: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.207
Patch208: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.208
Patch209: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.209
Patch210: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.210
Patch211: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.211
Patch212: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.212
Patch213: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.213
Patch214: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.214
Patch215: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.215
Patch216: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.216
Patch217: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.217
Patch218: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.218
Patch219: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.219
Patch220: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.220
Patch221: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.221
Patch222: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.222
Patch223: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.223
Patch224: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.224
Patch225: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.225
Patch226: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.226
Patch227: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.227
Patch228: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.228
Patch229: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.229
Patch230: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.230
Patch231: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.231
Patch232: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.232
Patch233: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.233
Patch234: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.234
Patch235: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.235
Patch236: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.236
Patch237: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.237
Patch238: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.238
Patch239: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.239
Patch240: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.240
Patch241: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.241
Patch242: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.242
Patch243: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.243
Patch244: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.244
Patch245: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.245
Patch246: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.246
Patch247: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.247
Patch248: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.248
Patch249: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.249
Patch250: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.250
Patch251: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.251
Patch252: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.252
Patch253: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.253
Patch254: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.254
Patch255: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.255
Patch256: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.256
Patch257: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.257
Patch258: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.258
Patch259: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.259
Patch260: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.260
Patch261: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.261
Patch262: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.262
Patch263: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.263
Patch264: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.264
Patch265: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.265
Patch266: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.266
Patch267: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.267
Patch268: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.268
Patch269: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.269
Patch270: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.270
Patch271: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.271
Patch272: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.272
Patch273: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.273
Patch274: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.274
Patch275: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.275
Patch276: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.276
Patch277: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.277
Patch278: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.278
Patch279: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.279
Patch280: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.280
Patch281: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.281
Patch282: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.282
Patch283: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.283
Patch284: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.284
Patch285: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.285
Patch286: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.286
Patch287: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.287
Patch288: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.288
Patch289: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.289
Patch290: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.290
Patch291: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.291
Patch292: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.292
Patch293: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.293
Patch294: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.294
Patch295: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.295
Patch296: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.296
Patch297: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.297
Patch298: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.298
Patch299: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.299
Patch300: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.300
Patch301: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.301
Patch302: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.302
Patch303: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.303
Patch304: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.304
Patch305: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.305
Patch306: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.306
Patch307: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.307
Patch308: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.308
Patch309: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.309
Patch310: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.310
Patch311: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.311
Patch312: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.312
Patch313: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.313
Patch314: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.314
Patch315: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.315
Patch316: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.316
Patch317: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.317
Patch318: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.318
Patch319: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.319
Patch320: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.320
Patch321: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.321
Patch322: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.322
Patch323: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.323
Patch324: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.324
Patch325: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.325
Patch326: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.326
Patch327: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.327
Patch328: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.328
Patch329: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.329
Patch330: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.330
Patch331: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.331
Patch332: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.332
Patch333: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.333
Patch334: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.334
Patch335: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.335
Patch336: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.336
Patch337: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.337
Patch338: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.338
Patch339: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.339
Patch340: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.340
Patch341: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.341
Patch342: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.342
Patch343: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.343
Patch344: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.344
Patch345: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.345
Patch346: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.346
Patch347: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.347
Patch348: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.348
Patch349: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.349
Patch350: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.350
Patch351: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.351
Patch352: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.352
Patch353: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.353
Patch354: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.354
Patch355: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.355
Patch356: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.356
Patch357: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.357
Patch358: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.358
Patch359: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.359
Patch360: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.360
Patch361: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.361
Patch362: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.362
Patch363: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.363
Patch364: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.364
Patch365: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.365
Patch366: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.366
Patch367: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.367
Patch368: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.368
Patch369: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.369
Patch370: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.370
Patch371: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.371
Patch372: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.372
Patch373: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.373
Patch374: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.374
Patch375: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.375
Patch376: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.376
Patch377: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.377
Patch378: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.378
Patch379: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.379
Patch380: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.380
Patch381: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.381
Patch382: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.382
Patch383: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.383
Patch384: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.384
Patch385: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.385
Patch386: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.386
Patch387: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.387
Patch388: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.388
Patch389: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.389
Patch390: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.390
Patch391: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.391
Patch392: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.392
Patch393: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.393
Patch394: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.394
Patch395: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.395
Patch396: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.396
Patch397: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.397
Patch398: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.398
Patch399: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.399
Patch400: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.400
Patch401: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.401
Patch402: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.402
Patch403: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.403
Patch404: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.404
Patch405: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.405
Patch406: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.406
Patch407: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.407
Patch408: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.408
Patch409: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.409
Patch410: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.410
Patch411: ftp://ftp.vim.org/pub/vim/patches/7.2/7.2.411

Patch3000: vim-7.0-syntax.patch
Patch3002: vim-7.1-nowarnings.patch
Patch3003: vim-6.1-rh3.patch
Patch3004: vim-7.0-rclocation.patch
Patch3006: vim-6.4-checkhl.patch
Patch3007: vim-7.2-fstabsyntax.patch
# Replaced by 7.2.315 patch:
#Patch3008: vim-7.1-lib64.patch
Patch3009: vim-7.0-warning.patch
Patch3010: vim-7.0-syncolor.patch
Patch3011: vim-7.0-specedit.patch
Patch3012: vim72-rh514717.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel ncurses-devel gettext perl-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: libacl-devel gpm-devel autoconf
%if %{WITH_SELINUX}
BuildRequires: libselinux-devel
%endif
%if %{desktop_file}
# for /usr/bin/desktop-file-install
Requires: desktop-file-utils
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
%endif
Epoch: 2

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
Group: Applications/Editors
Conflicts: man-pages-fr < 0.9.7-14
Conflicts: man-pages-it < 0.3.0-17
Conflicts: man-pages-pl < 0.24-2

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.

%package spell
Summary: The dictionaries for spell checking. This package is optional
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release}

%description spell
This subpackage contains dictionaries for vim spell checking in
many different languages.

%package minimal
Summary: A minimal version of the VIM editor
Group: Applications/Editors
Provides: vi = %{version}-%{release}

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, which is
installed into /bin/vi for use when only the root partition is
present. NOTE: The online help is only available when the vim-common
package is installed.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} which
Provides: vim = %{version}-%{release}
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.

%package X11
Summary: The VIM version of the vi editor for the X Window System
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} libattr >= 2.4 gtk2 >= 2.6
Provides: gvim = %{version}-%{release}
BuildRequires: gtk2-devel libSM-devel libXt-devel libXpm-devel
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: hicolor-icon-theme

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and
more. VIM-X11 is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support.

Install the vim-X11 package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim-common package.

%prep
%setup -q -b 0 -n %{vimdir}
%setup -q -D -b 1 -n %{vimdir}
%setup -q -D -b 2 -n %{vimdir}
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1
%patch2003 -p1
%patch2004 -p1
%patch2010 -p1
%if %{withhunspell}
%patch2011 -p1
%endif
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
# for i in `seq 1 14`; do printf "%%patch%03d -p0 \n" $i; done
%patch001 -p0
%patch002 -p0
%patch003 -p0
%patch004 -p0
%patch005 -p0
%patch006 -p0
%patch007 -p0
%patch008 -p0
%patch009 -p0
%patch010 -p0
%patch011 -p0
%patch012 -p0
%patch013 -p0
%patch014 -p0
%patch015 -p0
%patch016 -p0
%patch017 -p0
%patch018 -p0
%patch019 -p0
%patch020 -p0
%patch021 -p0
%patch022 -p0
%patch023 -p0
%patch024 -p0
%patch025 -p0
%patch026 -p0
%patch027 -p0
%patch028 -p0
%patch029 -p0
%patch030 -p0
%patch031 -p0
%patch032 -p0
%patch033 -p0
%patch034 -p0
%patch035 -p0
%patch036 -p0
%patch037 -p0
%patch038 -p0
%patch039 -p0
%patch040 -p0
%patch041 -p0
%patch042 -p0
%patch043 -p0
%patch044 -p0
%patch045 -p0
%patch046 -p0
%patch047 -p0
%patch048 -p0
%patch049 -p0
%patch050 -p0
%patch051 -p0
%patch052 -p0
%patch053 -p0
%patch054 -p0
%patch055 -p0
%patch056 -p0
%patch057 -p0
%patch058 -p0
%patch059 -p0
%patch060 -p0
%patch061 -p0                                          
%patch062 -p0
%patch063 -p0
%patch064 -p0
%patch065 -p0
%patch066 -p0
%patch067 -p0
%patch068 -p0
%patch069 -p0
%patch070 -p0
%patch071 -p0
%patch072 -p0
%patch073 -p0
%patch074 -p0
%patch075 -p0
%patch076 -p0
%patch077 -p0
%patch078 -p0
%patch079 -p0
%patch080 -p0
%patch081 -p0
%patch082 -p0
%patch083 -p0
%patch084 -p0
%patch085 -p0
%patch086 -p0
%patch087 -p0
%patch088 -p0
%patch089 -p0
%patch090 -p0
%patch091 -p0
%patch092 -p0
%patch093 -p0
%patch094 -p0
%patch095 -p0
%patch096 -p0
%patch097 -p0
%patch098 -p0
%patch099 -p0
%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0
%patch127 -p0
%patch128 -p0
%patch129 -p0
%patch130 -p0
%patch131 -p0
%patch132 -p0
%patch133 -p0                                          
%patch134 -p0                                          
%patch135 -p0                                          
%patch136 -p0                                          
%patch137 -p0                                          
%patch138 -p0                                          
%patch139 -p0                                          
%patch140 -p0                                          
%patch141 -p0
%patch142 -p0
%patch143 -p0
%patch144 -p0
%patch145 -p0
%patch146 -p0
%patch147 -p0
%patch148 -p0
%patch149 -p0 
%patch150 -p0 
%patch151 -p0 
%patch152 -p0 
%patch153 -p0 
%patch154 -p0 
%patch155 -p0 
%patch156 -p0 
%patch157 -p0 
%patch158 -p0 
%patch159 -p0 
%patch160 -p0 
%patch161 -p0 
%patch162 -p0 
%patch163 -p0 
%patch164 -p0 
%patch165 -p0 
%patch166 -p0 
%patch167 -p0 
%patch168 -p0 
%patch169 -p0 
%patch170 -p0 
%patch171 -p0 
%patch172 -p0 
%patch173 -p0 
%patch174 -p0 
%patch175 -p0 
%patch176 -p0 
%patch177 -p0 
%patch178 -p0 
%patch179 -p0 
%patch180 -p0 
%patch181 -p0 
%patch182 -p0 
%patch183 -p0 
%patch184 -p0 
%patch185 -p0 
%patch186 -p0 
%patch187 -p0 
%patch188 -p0 
%patch189 -p0 
%patch190 -p0 
%patch191 -p0 
%patch192 -p0 
%patch193 -p0 
%patch194 -p0 
%patch195 -p0 
%patch196 -p0 
%patch197 -p0 
%patch198 -p0 
%patch199 -p0 
%patch200 -p0 
%patch201 -p0 
%patch202 -p0 
%patch203 -p0 
%patch204 -p0 
%patch205 -p0 
%patch206 -p0 
%patch207 -p0 
%patch208 -p0 
%patch209 -p0 
%patch210 -p0 
%patch211 -p0 
%patch212 -p0 
%patch213 -p0 
%patch214 -p0 
%patch215 -p0 
%patch216 -p0 
%patch217 -p0 
%patch218 -p0 
%patch219 -p0 
%patch220 -p0 
%patch221 -p0 
%patch222 -p0 
%patch223 -p0 
%patch224 -p0 
%patch225 -p0 
%patch226 -p0 
%patch227 -p0 
%patch228 -p0 
%patch229 -p0 
%patch230 -p0 
%patch231 -p0 
%patch232 -p0 
%patch233 -p0 
%patch234 -p0 
%patch235 -p0 
%patch236 -p0 
%patch237 -p0 
%patch238 -p0 
%patch239 -p0 
%patch240 -p0 
%patch241 -p0 
%patch242 -p0 
%patch243 -p0 
%patch244 -p0 
%patch245 -p0 
%patch246 -p0
%patch247 -p0
%patch248 -p0
%patch249 -p0
%patch250 -p0
%patch251 -p0
%patch252 -p0
%patch253 -p0
%patch254 -p0
%patch255 -p0
%patch256 -p0
%patch257 -p0
%patch258 -p0
%patch259 -p0
%patch260 -p0
%patch261 -p0
%patch262 -p0
%patch263 -p0
%patch264 -p0
%patch265 -p0
%patch266 -p0
%patch267 -p0
%patch268 -p0
%patch269 -p0
%patch270 -p0
%patch271 -p0
%patch272 -p0
%patch273 -p0
%patch274 -p0
%patch275 -p0
%patch276 -p0
%patch277 -p0
%patch278 -p0
%patch279 -p0
%patch280 -p0
%patch281 -p0
%patch282 -p0
%patch283 -p0
%patch284 -p0
%patch285 -p0
%patch286 -p0
%patch287 -p0
%patch288 -p0
%patch289 -p0
%patch290 -p0
%patch291 -p0
%patch292 -p0
%patch293 -p0
%patch294 -p0
%patch295 -p0
%patch296 -p0
%patch297 -p0
%patch298 -p0
%patch299 -p0
%patch300 -p0
%patch301 -p0
%patch302 -p0
%patch303 -p0
%patch304 -p0
%patch305 -p0
%patch306 -p0
%patch307 -p0
%patch308 -p0
%patch309 -p0
%patch310 -p0
%patch311 -p0
%patch312 -p0
%patch313 -p0
%patch314 -p0
%patch315 -p0
%patch316 -p0
%patch317 -p0
%patch318 -p0
%patch319 -p0
%patch320 -p0
%patch321 -p0
%patch322 -p0
%patch323 -p0
%patch324 -p0
%patch325 -p0
%patch326 -p0
%patch327 -p0
%patch328 -p0
%patch329 -p0
%patch330 -p0
%patch331 -p0
%patch332 -p0
%patch333 -p0
%patch334 -p0
%patch335 -p0
%patch336 -p0
%patch337 -p0
%patch338 -p0
%patch339 -p0
%patch340 -p0
%patch341 -p0
%patch342 -p0
%patch343 -p0
%patch344 -p0
%patch345 -p0
%patch346 -p0
%patch347 -p0
%patch348 -p0
%patch349 -p0
%patch350 -p0
%patch351 -p0
%patch352 -p0
%patch353 -p0
%patch354 -p0
%patch355 -p0
%patch356 -p0
%patch357 -p0
%patch358 -p0
%patch359 -p0
%patch360 -p0
%patch361 -p0
%patch362 -p0
%patch363 -p0
%patch364 -p0
%patch365 -p0
%patch366 -p0
%patch367 -p0
%patch368 -p0
%patch369 -p0
%patch370 -p0
%patch371 -p0
%patch372 -p0
%patch373 -p0
%patch374 -p0
%patch375 -p0
%patch376 -p0
%patch377 -p0
%patch378 -p0
%patch379 -p0
%patch380 -p0
%patch381 -p0
%patch382 -p0
%patch383 -p0
%patch384 -p0
%patch385 -p0
%patch386 -p0
%patch387 -p0
%patch388 -p0
%patch389 -p0
%patch390 -p0
%patch391 -p0
%patch392 -p0
%patch393 -p0
%patch394 -p0
%patch395 -p0
%patch396 -p0
%patch397 -p0
%patch398 -p0
%patch399 -p0
%patch400 -p0
%patch401 -p0
%patch402 -p0
%patch403 -p0
%patch404 -p0
%patch405 -p0
%patch406 -p0
%patch407 -p0
%patch408 -p0
%patch409 -p0
%patch410 -p0
%patch411 -p0

# install spell files
%if %{withvimspell}
%{__tar} xjf %{SOURCE13}
%endif

%patch3000 -p1
%patch3002 -p1
%patch3003 -p1
%patch3004 -p1

%patch3006 -p1
%patch3007 -p1
#patch3008 -p1
%patch3009 -p1
%patch3010 -p1
%patch3011 -p1
%patch3012 -p1

cp -f %{SOURCE15} runtime/syntax/forth.vim
cp -f %{SOURCE16} runtime/plugin/netrwPlugin.vim
cp -f %{SOURCE17} runtime/plugin/gzip.vim
cp -f %{SOURCE18} runtime/plugin/filetype.vim
cp -f %{SOURCE19} runtime/autoload/zip.vim
cp -f %{SOURCE20} runtime/autoload/tar.vim
cp -f %{SOURCE21} runtime/autoload/netrwFileHandlers.vim
cp -f %{SOURCE22} runtime/autoload/netrw.vim
cp -f %{SOURCE23} runtime/autoload/netrwSettings.vim


%build
cd src
autoconf

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

%configure --with-features=huge --enable-pythoninterp --enable-perlinterp \
  --disable-tclinterp --with-x=yes \
  --enable-xim --enable-multibyte \
  --with-tlib=ncurses \
  --enable-gtk2-check --enable-gui=gtk2 \
  --with-compiledby="<bugzilla@redhat.com>" --enable-cscope \
  --with-modified-by="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp \
%else
  --disable-rubyinterp \
%endif

make %{?_smp_mflags}
cp vim gvim
make clean

%configure --prefix=%{_prefix} --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=%{_prefix} --enable-multibyte \
 --enable-cscope --with-modified-by="<bugzilla@redhat.com>" \
 --with-tlib=ncurses \
 --with-compiledby="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp \
%else
  --disable-rubyinterp \
%endif

make %{?_smp_mflags}
cp vim enhanced-vim
make clean

perl -pi -e "s/help.txt/vi_help.txt/"  os_unix.h ex_cmds.c
perl -pi -e "s/\/etc\/vimrc/\/etc\/virc/"  os_unix.h
%configure --prefix=%{_prefix} --with-features=small --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
%if %{WITH_SELINUX}
  --enable-selinux \
%else
  --disable-selinux \
%endif
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm --exec-prefix=/ \
  --with-compiledby="<bugzilla@redhat.com>" \
  --with-modified-by="<bugzilla@redhat.com>"

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/{after,autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/after/{autoload,colors,compiler,doc,ftdetect,ftplugin,indent,keymap,lang,plugin,print,spell,syntax,tutor}
cp -f %{SOURCE11} .
cp -f %{SOURCE14} $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/template.spec
cp runtime/doc/uganda.txt LICENSE
# Those aren't Linux info files but some binary files for Amiga:
rm -f README*.info


cd src
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin
make installgtutorbin  DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/%{_bindir}/xxd
mv $RPM_BUILD_ROOT/bin/gvimtutor $RPM_BUILD_ROOT/%{_bindir}/gvimtutor
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 gvim $RPM_BUILD_ROOT/%{_bindir}/gvim
install -p -m644 %{SOURCE7} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -p -m644 %{SOURCE8} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -p -m644 %{SOURCE9} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -p -m644 %{SOURCE10} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/gvim.png
install -m755 enhanced-vim $RPM_BUILD_ROOT/%{_bindir}/vim

( cd $RPM_BUILD_ROOT
  mv ./bin/vimtutor ./%{_bindir}/vimtutor
  mv ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vi ./bin/view
  ln -sf vim ./%{_bindir}/ex
  ln -sf vim ./%{_bindir}/rvim
  ln -sf vim ./%{_bindir}/vimdiff
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  ln -sf gvim ./%{_bindir}/gview
  ln -sf gvim ./%{_bindir}/gex
  ln -sf gvim ./%{_bindir}/evim
  ln -sf gvim ./%{_bindir}/gvimdiff
  ln -sf gvim ./%{_bindir}/vimx
  %if "%{desktop_file}" == "1"
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
    desktop-file-install --vendor fedora \
        --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
        %{SOURCE3}
        # --add-category "Development;TextEditor;X-Red-Hat-Base"
  %else
    mkdir -p ./%{_sysconfdir}/X11/applnk/Applications
    cp %{SOURCE3} ./%{_sysconfdir}/X11/applnk/Applications/gvim.desktop
  %endif
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

pushd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tutor
mkdir conv
   iconv -f CP1252 -t UTF8 tutor.ca > conv/tutor.ca
   iconv -f CP1252 -t UTF8 tutor.it > conv/tutor.it
   #iconv -f CP1253 -t UTF8 tutor.gr > conv/tutor.gr
   iconv -f CP1252 -t UTF8 tutor.fr > conv/tutor.fr
   iconv -f CP1252 -t UTF8 tutor.es > conv/tutor.es
   iconv -f CP1252 -t UTF8 tutor.de > conv/tutor.de
   #iconv -f CP737 -t UTF8 tutor.gr.cp737 > conv/tutor.gr.cp737
   #iconv -f EUC-JP -t UTF8 tutor.ja.euc > conv/tutor.ja.euc
   #iconv -f SJIS -t UTF8 tutor.ja.sjis > conv/tutor.ja.sjis
   iconv -f UTF8 -t UTF8 tutor.ja.utf-8 > conv/tutor.ja.utf-8
   iconv -f UTF8 -t UTF8 tutor.ko.utf-8 > conv/tutor.ko.utf-8
   iconv -f CP1252 -t UTF8 tutor.no > conv/tutor.no
   iconv -f ISO-8859-2 -t UTF8 tutor.pl > conv/tutor.pl
   iconv -f ISO-8859-2 -t UTF8 tutor.sk > conv/tutor.sk
   iconv -f KOI8R -t UTF8 tutor.ru > conv/tutor.ru
   iconv -f CP1252 -t UTF8 tutor.sv > conv/tutor.sv
   mv -f tutor.ja.euc tutor.ja.sjis tutor.ko.euc tutor.pl.cp1250 tutor.zh.big5 tutor.ru.cp1251 tutor.zh.euc conv/
   rm -f tutor.ca tutor.de tutor.es tutor.fr tutor.gr tutor.it tutor.ja.utf-8 tutor.ko.utf-8 tutor.no tutor.pl tutor.sk tutor.ru tutor.sv
mv -f conv/* .
rmdir conv
popd

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x %{_bindir}/id ] || return
  ID=\`%{_bindir}/id -u\`
  [ -n "\$ID" -a "\$ID" -le 200 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.csh <<EOF
if ( -x %{_bindir}/id ) then
  if ( "\`%{_bindir}/id -u\`" > 200 ) then
    alias vi vim
  endif
endif
EOF
chmod 0644 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/*
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/vimrc
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/virc
(cd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc;
 gzip -9 *.txt
 gzip -d help.txt.gz version7.txt.gz sponsor.txt.gz
 cp %{SOURCE12} .
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/;s/\tversion7.txt.gz\t/\tversion7.txt\t/;s/\tsponsor.txt.gz\t/\tsponsor.txt\t/' > tags.new; mv -f tags.new tags
cat >> tags << EOF
vi_help.txt	vi_help.txt	/*vi_help.txt*
vi-author.txt	vi_help.txt	/*vi-author*
vi-Bram.txt	vi_help.txt	/*vi-Bram*
vi-Moolenaar.txt	vi_help.txt	/*vi-Moolenaar*
vi-credits.txt	vi_help.txt	/*vi-credits*
EOF
 )
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/macros/maze/maze*.c
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tools
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/doc/vim2html.pl
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tutor/tutor.gr.utf-8~
( cd $RPM_BUILD_ROOT/%{_mandir}
  for i in `find ??/ -type f`; do
    bi=`basename $i`
    iconv -f latin1 -t UTF8 $i > $RPM_BUILD_ROOT/$bi
    mv -f $RPM_BUILD_ROOT/$bi $i
  done
)

# Remove not UTF-8 manpages
for i in pl.ISO8859-2 it.ISO8859-1 ru.KOI8-R fr.ISO8859-1; do
  rm -rf $RPM_BUILD_ROOT/%{_mandir}/$i
done

# use common man1/ru directory
mv $RPM_BUILD_ROOT/%{_mandir}/ru.UTF-8 $RPM_BUILD_ROOT/%{_mandir}/ru

# Remove duplicate man pages
for i in fr.UTF-8 it.UTF-8 pl.UTF-8; do
  rm -rf $RPM_BUILD_ROOT/%{_mandir}/$i
done

for i in rvim.1 gvim.1 gvimdiff.1; do 
  echo ".so man1/vim.1" > $RPM_BUILD_ROOT/%{_mandir}/man1/$i
done

%post X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%postun X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/vimrc
%doc README* LICENSE
%doc runtime/docs
%doc Changelog.rpm
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{vimdir}
%dir %{_datadir}/%{name}/vimfiles
%dir %{_datadir}/%{name}/vimfiles/after
%dir %{_datadir}/%{name}/vimfiles/after/*
%dir %{_datadir}/%{name}/vimfiles/autoload
%dir %{_datadir}/%{name}/vimfiles/colors
%dir %{_datadir}/%{name}/vimfiles/compiler
%dir %{_datadir}/%{name}/vimfiles/doc
%dir %{_datadir}/%{name}/vimfiles/ftdetect
%dir %{_datadir}/%{name}/vimfiles/ftplugin
%dir %{_datadir}/%{name}/vimfiles/indent
%dir %{_datadir}/%{name}/vimfiles/keymap
%dir %{_datadir}/%{name}/vimfiles/lang
%dir %{_datadir}/%{name}/vimfiles/plugin
%dir %{_datadir}/%{name}/vimfiles/print
%dir %{_datadir}/%{name}/vimfiles/spell
%dir %{_datadir}/%{name}/vimfiles/syntax
%dir %{_datadir}/%{name}/vimfiles/tutor
%{_datadir}/%{name}/vimfiles/template.spec
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%dir %{_datadir}/%{name}/%{vimdir}/lang
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%if ! %{withvimspell}
%{_datadir}/%{name}/%{vimdir}/spell
%endif
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(eo) %{_datadir}/%{name}/%{vimdir}/lang/eo
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fi) %{_datadir}/%{name}/%{vimdir}/lang/fi
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(pt_BR) %{_datadir}/%{name}/%{vimdir}/lang/pt_BR
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8
/%{_bindir}/xxd
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(ru) %{_mandir}/ru/man1/*

%if %{withvimspell}
%files spell
%defattr(-,root,root)
%dir %{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/vim70/spell/cleanadd.vim
%lang(af) %{_datadir}/%{name}/%{vimdir}/spell/af.*
%lang(am) %{_datadir}/%{name}/%{vimdir}/spell/am.*
%lang(bg) %{_datadir}/%{name}/%{vimdir}/spell/bg.*
%lang(ca) %{_datadir}/%{name}/%{vimdir}/spell/ca.*
%lang(cs) %{_datadir}/%{name}/%{vimdir}/spell/cs.*
%lang(cy) %{_datadir}/%{name}/%{vimdir}/spell/cy.*
%lang(da) %{_datadir}/%{name}/%{vimdir}/spell/da.*
%lang(de) %{_datadir}/%{name}/%{vimdir}/spell/de.*
%lang(el) %{_datadir}/%{name}/%{vimdir}/spell/el.*
%lang(en) %{_datadir}/%{name}/%{vimdir}/spell/en.*
%lang(eo) %{_datadir}/%{name}/%{vimdir}/spell/eo.*
%lang(es) %{_datadir}/%{name}/%{vimdir}/spell/es.*
%lang(fo) %{_datadir}/%{name}/%{vimdir}/spell/fo.*
%lang(fr) %{_datadir}/%{name}/%{vimdir}/spell/fr.*
%lang(ga) %{_datadir}/%{name}/%{vimdir}/spell/ga.*
%lang(gd) %{_datadir}/%{name}/%{vimdir}/spell/gd.*
%lang(gl) %{_datadir}/%{name}/%{vimdir}/spell/gl.*
%lang(he) %{_datadir}/%{name}/%{vimdir}/spell/he.*
%lang(hr) %{_datadir}/%{name}/%{vimdir}/spell/hr.*
%lang(hu) %{_datadir}/%{name}/%{vimdir}/spell/hu.*
%lang(id) %{_datadir}/%{name}/%{vimdir}/spell/id.*
%lang(it) %{_datadir}/%{name}/%{vimdir}/spell/it.*
%lang(ku) %{_datadir}/%{name}/%{vimdir}/spell/ku.*
%lang(la) %{_datadir}/%{name}/%{vimdir}/spell/la.*
%lang(lt) %{_datadir}/%{name}/%{vimdir}/spell/lt.*
%lang(lv) %{_datadir}/%{name}/%{vimdir}/spell/lv.*
%lang(mg) %{_datadir}/%{name}/%{vimdir}/spell/mg.*
%lang(mi) %{_datadir}/%{name}/%{vimdir}/spell/mi.*
%lang(ms) %{_datadir}/%{name}/%{vimdir}/spell/ms.*
%lang(nb) %{_datadir}/%{name}/%{vimdir}/spell/nb.*
%lang(nl) %{_datadir}/%{name}/%{vimdir}/spell/nl.*
%lang(nn) %{_datadir}/%{name}/%{vimdir}/spell/nn.*
%lang(ny) %{_datadir}/%{name}/%{vimdir}/spell/ny.*
%lang(pl) %{_datadir}/%{name}/%{vimdir}/spell/pl.*
%lang(pt) %{_datadir}/%{name}/%{vimdir}/spell/pt.*
%lang(ro) %{_datadir}/%{name}/%{vimdir}/spell/ro.*
%lang(ru) %{_datadir}/%{name}/%{vimdir}/spell/ru.*
%lang(rw) %{_datadir}/%{name}/%{vimdir}/spell/rw.*
%lang(sk) %{_datadir}/%{name}/%{vimdir}/spell/sk.*
%lang(sl) %{_datadir}/%{name}/%{vimdir}/spell/sl.*
%lang(sv) %{_datadir}/%{name}/%{vimdir}/spell/sv.*
%lang(sw) %{_datadir}/%{name}/%{vimdir}/spell/sw.*
%lang(tet) %{_datadir}/%{name}/%{vimdir}/spell/tet.*
%lang(th) %{_datadir}/%{name}/%{vimdir}/spell/th.*
%lang(tl) %{_datadir}/%{name}/%{vimdir}/spell/tl.*
%lang(tn) %{_datadir}/%{name}/%{vimdir}/spell/tn.*
%lang(uk) %{_datadir}/%{name}/%{vimdir}/spell/uk.*
%lang(yi) %{_datadir}/%{name}/%{vimdir}/spell/yi.*
%lang(yi-tr) %{_datadir}/%{name}/%{vimdir}/spell/yi-tr.*
%lang(zu) %{_datadir}/%{name}/%{vimdir}/spell/zu.*
%endif

%files minimal
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/virc
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview

%files enhanced
%defattr(-,root,root)
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/ex
%{_bindir}/vimtutor
%config(noreplace) %{_sysconfdir}/profile.d/vim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*

%files X11
%defattr(-,root,root)
%if "%{desktop_file}" == "1"
/%{_datadir}/applications/*
%else
/%{_sysconfdir}/X11/applnk/*/gvim.desktop
%endif
%{_bindir}/gvimtutor
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/gview
%{_bindir}/gex
%{_bindir}/vimx
%{_bindir}/evim
%{_mandir}/man1/evim.*
%{_mandir}/man1/gvim*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Fri Jul 08 2011 Mike Adams <shalkie@gooseproject.org> 7.2.411-1.5
- Rebuild for GoOSe Linux 6

* Wed May 19 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.4
- fix vim.sh scripts as id -u might return an empty string (#578795)

* Mon May 03 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.3
- remove duplicate entry in menu (#587940)

* Tue Apr 20 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.2
- fix rvim manpage
- Resolves: #583940

* Mon Apr 19 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1.1
- augroup "fedora" in /etc/vimrc renamed to "redhat"
- Resolves: #578785
- fix vim.csh  'tcsh -e' scripts
- Resolves: #578795

* Wed Mar 24 2010 Karsten Hopp <karsten@redhat.com> 7.2.411-1
- patchlevel 411

* Fri Feb 26 2010 Karsten Hopp <karsten@redhat.com> 7.2.245-3.3
- rebuild

* Mon Feb 22 2010 Karsten Hopp <karsten@redhat.com> 7.2.245-3.2
- update licenses and tarball

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 2:7.2.245-3.1
- Rebuilt for RHEL 6

* Thu Aug 20 2009 Karsten Hopp <karsten@redhat.com> 7.2.245-3
- change range of system ids in /etc/profile.d/vim/* (#518555)

* Mon Aug 03 2009 Karsten Hopp <karsten@redhat.com> 7.2.245-2
- add fix for glibc fortify segfault (#514717, Adam Tkac)

* Sat Aug 01 2009 Karsten Hopp <karsten@redhat.com> 7.2.245-1
- add 97 upstream patches to get to patchlevel 245

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:7.2.148-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Karsten Hopp <karsten@redhat.com> 7.2.148-1
- patchlevel 148, fixes #461417

* Tue Mar 10 2009 Karsten Hopp <karsten@redhat.com> 7.2.132-1
- patchlevel 132, fixes accesses to freed memory

* Wed Mar 04 2009 Karsten Hopp <karsten@redhat.com> 7.2.131-1
- patchlevel 131

* Tue Feb 24 2009 Karsten Hopp <karsten@redhat.com> 7.2.127-1
- patchlevel 127

* Mon Feb 23 2009 Karsten Hopp <karsten@redhat.com> 7.2.124-1
- patchlevel 124

* Mon Jan 26 2009 Karsten Hopp <karsten@redhat.com> 7.2.088-1
- patchlevel 88

* Thu Jan 08 2009 Karsten Hopp <karsten@redhat.com> 7.2.079-2
- patchlevel 79

* Thu Dec 04 2008 Jesse Keating <jkeating@redhat.com> - 7.2.060-2
- Rebuild for new python.

* Mon Dec 01 2008 Karsten Hopp <karsten@redhat.com> 7.2.060-1
- patchlevel 60

* Mon Nov 10 2008 Karsten Hopp <karsten@redhat.com> 7.2.032-1
- patchlevel 32

* Mon Nov 03 2008 Karsten Hopp <karsten@redhat.com> 7.2.026-2
- add more /usr/share/vim/vimfiles directories (#444387)

* Mon Nov 03 2008 Karsten Hopp <karsten@redhat.com> 7.2.026-1
- patchlevel 26
- own some directories in /usr/share/vim/vimfiles (#469491)

* Tue Oct 21 2008 Karsten Hopp <karsten@redhat.com> 7.2.025-2
- re-enable clean

* Mon Oct 20 2008 Karsten Hopp <karsten@redhat.com> 7.2.025-1
- patchlevel 25
- add Categories tag to desktop file (#226526)
- add requirement on hicolor-icon-theme to vim-X11 (#226526)
- drop Amiga info files (#226526)
- remove non-utf8 man pages (#226526)
- drop Application from categories (#226526)

* Tue Sep 30 2008 Karsten Hopp <karsten@redhat.com> 7.2.022-1
- patchlevel 22

* Mon Sep 08 2008 Karsten Hopp <karsten@redhat.com> 7.2.013-1
- patchlevel 13

* Mon Aug 25 2008 Karsten Hopp <karsten@redhat.com> 7.2.006-1
- patchlevel 6

* Mon Aug 18 2008 Karsten Hopp <karsten@redhat.com> 7.2.002-1
- patchlevel 2
- fix specfile template (#446070)
- old specfile changelog moved to Changelog.rpm

* Fri Aug 14 2008 Karsten Hopp <karsten@redhat.com> 7.2.000-1
- vim 7.2
- drop 330 patches

# vim:nrformats-=octal
