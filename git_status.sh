#!/bin/bash

commit=$(git rev-list HEAD --count --first-parent)
echo "Nombre de Commit effectué : "$commit

pull=$(git rev-list HEAD --count --show-pulls)
echo "Nombre de Pull effectué : "$pull

liste=$(git shortlog -s --all )
echo "liste des utilisateurs aillant fait un Commit: " $liste
