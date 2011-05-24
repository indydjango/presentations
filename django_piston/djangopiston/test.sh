#!/bin/sh

if [ $1 ]; then
    clear
    echo "Testing CREATE..."
    curl -v -X POST -d title="Hello world!" -d text="Hello world!" $1
    echo -n "Press enter to continue..."
    read null
    clear

    echo "Testing GET..."
    curl -v $1
    echo -n "Press enter to continue..."
    read null
    clear

    echo "Testing DELETE..."
    echo -n "Enter ID: "
    read ID
    curl -v -X DELETE $1/$ID/

    curl -v $1

else
    echo "Usage: $0 <url>"
fi


