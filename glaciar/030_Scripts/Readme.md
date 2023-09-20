










export BASH_DOTS=/home/ubuntu/deepracer-on-the-spot-pei/glaciar/030_Scripts
# if bash dots
if [ -f "$BASH_DOTS/.bashDotsRc" ]; then
    echo "Hola"
    . "$BASH_DOTS/.bashDotsRc"
fi
# if bash africa
if [ -f "$BASH_DOTS/.bashRegion_Africa" ]; then
    echo "Hola"
    . "$BASH_DOTS/.bashRegion_Africa"
fi


