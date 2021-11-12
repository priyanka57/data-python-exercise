The python application will take the two data files [students.csv , teachers.parquet] as input. The application uses both files to output a report in json listing each student, the teacher the student has and the class ID the student is scheduled for. 


Instructions:
1. Extract the zip file

2. Go to <your path>/dataeng/

3. The source code is located in 4 files - 'main.py, extract_data.py, validate_data.py, create_report.py' under dataeng folder

4. This application was developed on Pycharm. Pycharm uses a virtual environment. The application can be run through the IDE. Please check the 'main.py' and un-comment variables for input/output file path + file names. Use your own location and filenames for these three variables. 

5. Additionally, To run the program in your terminal, the virtual enviroment isn't active. You need to build or upload your enviroment Pycharm with your libraries. cd to the directory project /dataeng/ and write in terminal:
'source venv/bin/activate'
To run python program from the command line, use 
'python3.6 main.py csvfilename parquetfilename outputfilename' (Please use all filenames with their full directory path)
For example, 
'python3.6 /home/priya/PycharmProjects/dataeng/main.py /home/priya/Desktop/data_python_exercise/data_engineer/students.csv /home/priya/Desktop/data_python_exercise/data_engineer/teachers.parquet /home/priya/Desktop/data_python_exercise/data_engineer/report.json'

6. Please always make sure that the first argument provided to main.py through command line terminal is csv file, second argument must be parquet file and the third argument must be a output file(name it as you want) in .json extension.

7. Print statements are deliberately added to know where you currently stand during the whole application process. If you want to remove them, replace all the print statements with 'pass'
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Checklist to run this python application:

1. Python 3.6 or above
2. Configure python interpreter $PYTHONPATH to the executable shell. 
3. .CSV file containing students records
4. .parquet file containing teachers records
5. Modules Used: pandas, pyarrow, json, numpy. If not installed, please install them using pip3 install <modulename> on RHEL
6. The application comes with all the involved packages and virtual environment already setup. 

Helpful links:
https://www.jetbrains.com/help/pycharm/run-for-the-first-time.html

if the interpreter (virtual environment) is not located in the Project folder then it should be configured again 
https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html

