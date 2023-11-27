#!/bin/bash
set -e

function usage() {
    echo "Usage:       $0 [year-1> <year-2>...]"
    echo "Example:     $0 2021 2022 2023"
    echo "-h | --help  Show this help message"
}

while [ "$1" != "" ]; do
    case $1 in
        -h | --help )
            usage
            exit
            ;;
    esac
    shift
done

cd kifu
for var in "$@"
do
    echo "Connecting to http://wdoor.c.u-tokyo.ac.jp/shogi/x/wdoor$var.7z"
    wget http://wdoor.c.u-tokyo.ac.jp/shogi/x/wdoor$var.7z
    7z x wdoor$var.7z
done
