if [ "$#" -eq 2 ]; then
    python gen_direction.py $1 $2 1
fi
if [ "$#" -eq 3 ]; then
    python gen_direction.py $1 $2 $3
fi
