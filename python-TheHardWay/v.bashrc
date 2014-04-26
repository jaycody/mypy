#!/bin/bash

alias ll='ls -l -G'
alias ls='ls -G'
alias lar='ls -ARG'
alias vir='vi -R'
alias tf='tail -f'
alias psle='ps fawx | less'
alias virbashrc='vi -R ~/.bash_profile'
alias lintpy='pylint --disable-msg-cat=C,R,W --reports=n *.py'

export GREP_OPTIONS='-I --color=auto'
export PS1='\[\e[36;40m\]\d \t \w/ \\$ \[\e[0m\]'

# gvim () { /Applications/MacVim.app/Contents/MacOS/MacVim "$*" & ;}

les () { eval "$@" | less ;}

vit () { eval "$@" | vim - ;}

ctime () { echo | awk '{print strftime("%c",t)}' t=$1 ;}

where () { find . -type f -name "$1" ;}

thither () { dirsWhere=( `where "$1"` ); if [ -z "$dirsWhere" ]; then
echo 'Not found' >&2; elif [ -n "${dirsWhere[1]}" ]; then echo
"Ambiguous: ${dirsWhere[@]}" >&2; else cd `dirname $dirsWhere`; fi ;}

# stty erase '^?'
