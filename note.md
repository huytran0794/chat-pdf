<!-- TOC -->

- [Variable](#variable)
- [For code run in google colab](#for-code-run-in-google-colab)
    - [How to add secret key](#how-to-add-secret-key)
    - [How to run the aforementioned code block](#how-to-run-the-aforementioned-code-block)
    - [Change Pinecode index](#change-pinecode-index)
- [For ui code:](#for-ui-code)
    - [Library to install](#library-to-install)
    - [Variables to be notified:](#variables-to-be-notified)

<!-- /TOC -->

## Variable

- hugging face api key = "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"

## For code run in google colab

- This code is to convert data from documents into vectors and stored them inside an online vector-database called "Pinecone"

- Noted: The following code block can only run correctly after secret_key is setup inside Google Colab
  ![Alt text](image.png)

### How to add secret key

1. On left side, click on icon "Key" belongs to left vertical sidebar, then, click on "Thêm giá trị bí mật mới"
   ![Alt text](image-1.png)

2. Then fill in key_name, key_value in the input field
   ![Alt text](image-2.png)

3. Remember to toggle the button, that way your notebook can access the data inside Google Colab's secret key
   ![Alt text](image-3.png)

### How to run the aforementioned code block

1. Open Secret key like aboved tutorial
2. Run the code block
3. Check if result is same as this image
   ![Alt text](image-4.png)

### Change Pinecode index

- You can change my Pinecone index to your own Pinecone index
- Change the following api key inside the code block to your own Pinecone database api key.
![alt text](image-6.png)
- If you want to change the name of the index, you can change this
![alt text](image-7.png)

## For ui code:

- 2 files: app.py and utils.py, with app.py is the main file.

### Library to install

- used the following command

```
pip install langchain langchain-openai openai tiktoken pinecone-client streamlit
sentence-transformers
```

### Variables to be notified:

![Alt text](image-5.png)

- index_name is the name of the database in Pinecone, this one must be correct or else the code can't run
- Same with openapi key.
