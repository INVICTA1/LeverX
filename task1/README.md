About project:
====================
The project is used to merge JSON files:students, rooms.
And saves the result depending on the request to an xml or json file

Usage
====================
main.py [-s] students [-r] rooms [-f] format   

    -s      --students      Path to students Json file
    -r      --rooms         Path to rooms Json file
    -f      --format        Format result    
    
Examples
====================
    main.py -s resources\students.json -r resources\rooms.json -f xml

Notes
====================
The files to search for data are located in the resources folder