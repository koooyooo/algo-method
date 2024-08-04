for dir in `find . -type d`; do
    if [[ $dir == ./.git* ]]; then
        continue
    fi
    touch "$dir/.gitkeep"
done
