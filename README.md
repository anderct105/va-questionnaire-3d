<h1 align="center"> VA Questions Projection with Tensorflow Projector</h1>

Quick demo to generate and project the VA (Verbal Autopsy) questionnaires (http://www.healthdata.org/verbal-autopsy) data into a 3 dimensional space using either T-SNE or PCA with [TensorflowProjector](https://projector.tensorflow.org/). 
TensorflowProjector demo             |  Software demo
:-------------------------:|:-------------------------:
![](https://github.com/anderct105/va-questionnaire-3d/blob/develop/img/tf_projector_demo.gif)  |  ![](https://github.com/anderct105/va-questionnaire-3d/blob/develop/img/software_demo.gif) 
> **Content**  
> - [Requirements](https://github.com/anderct105/va-questionnaire-3d/develop/README.md#Requirements)  
> - [Run](https://github.com/anderct105/va-questionnaire-3d/develop/README.md#Run)  
> - [Results](https://github.com/anderct105/va-questionnaire-3d/develop/README.md#Results)  
> - [Projection](https://github.com/anderct105/va-questionnaire-3d/develop/README.md#Projection)  


## Requirements
Python 3 or later with all [requirements.txt](https://github.com/anderct105/va-questionnaire-3d/blob/master/requirements.txt) dependencies installed or docker. To install run:
```
$ pip3 install -r requirements.txt
```
or

```bash
$ sudo apt-get install docker
```

## Run
Make sure to have downloaded a [Glove](https://nlp.stanford.edu/projects/glove/) word embedding file, named as glove.txt.  Any dimension is admitted. 
### Python script
To run this project, download it and run this inside the folder **(you need to have glove.txt in the same folder)**: 

```$ python3 main.py```
### Docker
This image is available in registry.docker.com/anderct105/va-questionnaire-3d, just run **(you need to have glove.txt in the same folder)**:
```bash
$ docker run -it \
     -v $PWD/glove.txt:/usr/src/app/glove.txt \
     -v $PWD/out:/usr/src/app/out \
     anderct105/va-questionnaire-3d
```
## Results
You should see the output inside the out folder (two examples are given to you in this repository, you can use them on the projection step):
> **[questions_emb.tsv](https://github.com/anderct105/va-questionnaire-3d/blob/master/out/questions_emb.tsv)**: contains the corresponding doc-embedding for each question.

> **[questions_meta.tsv](https://github.com/anderct105/va-questionnaire-3d/blob/develop/out/questions_meta.tsv)**: contains the corresponding question formulation.
Each line of the first file corresponds with the same line in the second file.

## Projection
Once you have both files, you are now able to project them in [TensorflowProjector](https://projector.tensorflow.org/), by following this steps:
![](https://github.com/anderct105/va-questionnaire-3d/blob/develop/img/tensorflow_howto.gif)
