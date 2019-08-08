if [ "$#" -eq 1 ]; then
    python create_mdp.py $1 1
fi
if [ "$#" -eq 2 ]; then
    python create_mdp.py $1 $2
fi

