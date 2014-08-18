for FILE in *; do
	  # do something with $FILE
	    python parser.py $FILE
	    echo "File: $FILE"
done
