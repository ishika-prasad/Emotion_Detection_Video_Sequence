Author: Shuo Yao, Ishika Prasad.

The src folder contains the following directory: Flow, OFLW, PCA_Flow, PCA_newf, Video.

Directory Flow, OFLW, PCA_Flow, PCA_newf are created for ease of storing data, please do not modify.

**************************************************************************************************************
Directory Video contains data from RAVDESS dataset.

To download data, go to link: https://zenodo.org/record/1188976#.XfZ2I2RKguU

When data downloaded, put them into directory Video. Then run 'file_processor.py'. This program will deleted
every not related data.

**************************************************************************************************************
To Run the implement for the first approach:

First run 'video_processor.py': this program will process every video and calcuate their optical flow. The calculated
result will be stored in directory Flow.

Then run 'pca.py': this program will use PCA for feature extraction on every flow. And store the result in directory PCA_Flow

To train the model, run 'train.py': this program will train the KNN and HMM.

To test the model, run 'test.py': this program will conduct test on test data and output confusion matrix.
**************************************************************************************************************
To Run the implement for the second approach:

First use openface toolkit to preprocess the RAVDESS data, put the processed data in directory OFLW.
link to Openface 2.2.0: https://github.com/TadasBaltrusaitis/OpenFace

Then run 'pca_new.py': this program will use PCA for feature extraction on every response. 
And store the result in directory PCA_newf

To train the model, run 'train_new.py': this program will train the KNN and HMM.

To test the model, run 'test_new.py': this program will conduct test on test data and output confusion matrix.
**************************************************************************************************************
'ang_hmm.pkl', 'dis_hmm.pkl', 'fea_hmm.pkl', 'hap_hmm.pkl', 'sad_hmm.pkl', 'sup_hmm.pkl' are trained HMM moidel.
'knn_model.pkl' are trained KNN model.
They can be directly used for test.