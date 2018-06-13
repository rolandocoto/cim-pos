Procedures

(1) To create the first "incorrectly tagged sentence":

Go to the Java-Eclipse
Go to HolaMundo.java
Go to a line around 371. It should have the name of the batchFile.
Go to that file (in your computer, e.g. /Users/tenamu/Desktop/148.txt) and put in it the sentences you want to tag. Save it.
Go back to Java-Eclipse > HolaMundo.java.
Go to the downward pointing arrow next to the green "play" button. Select "HolaMundo". This will run the program.
There will be a lot of output. Copy-paste the tagged sentences that correspond to the ones you put in the batchFile. 
Paste those into the "incorrectly tagged sentence" column.
Correct them, and paste them into the correctly tagged column. 
Let Rolando know so he can retrain :)

(2) To create a file that you can use to train Weka:

Have ready a text file with lines of correctly tagged text in CIM. Put it in the same folder as pos-to-csv-asWekaTrainingInput.py

Run the instruction:
python pos-to-csv-asWekaTrainingInput.py pos-to-csv-asWekaInput-example-input.txt
the third words is the name of the file from where it's going to read the lines of tagged text.

This will create the CSV file weka-pos-training-set.csv . It's formatted as follows:
prePrePreToken | prePreToken | preToken | token | tokenPOS | followingToken

Open Weka.
Click on "Explorer"
Click on "Open file". Select the CSV file you just created.
Go to "Classify" on the upper part.

Choose > Trees > RandomTree
Choose "Cross-validation" at leave it at 10 folds.
Instead of (nom) postToken, select tokenPOS
Click "Start". This is going to start the training. After a while you'll see the results, including the confusion matrix and the error rates.

(One way to make better random trees is to click on the instruction "RandomTree -K 0 -M 1.0 -V...". Click on those letters, and then give it a KValue of at least 5).

Look at the "Results list" on the lower right. Right click on the name of the latest model you have trained. 
Click on "Save model". Save it and give it the extension .model

(If you want to connect this new model to the JAVA-Eclipse HolaMundo:

Go to Java-Eclipse
Go to HolaMundo.java, to the line 369 (approximately), the one that specifies the modelFile.
Change the route of the model file to the model you just made.
Run it. (Downward pointing button next to the green play button).
