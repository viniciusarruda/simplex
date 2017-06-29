for file in in/*
do
	filename="$(cut -d'/' -f2 <<<"$file")"
	python src/main.py "$file" > out/"$filename" 2>&1
done
