from logging import PlaceHolder
from secrets import choice
import streamlit as st
from PIL import Image
import os
import time
import shutil

def load_image(image_file):
    img = Image.open(image_file)
    return img

def compress_data():
    os.remove('output.zip')
    shutil.make_archive('output','zip','./test_images')
    print('data compressed')


def main():
    st.title("Multiple articulator segmentation")
    placeholder_heading = st.empty()
    placeholder_data_loader = st.empty()
    menu = ['Train images', 'Train labels', 'Test images']
    choice = st.sidebar.selectbox("Data upload", menu)
    gap = st.sidebar.text('')
    gap = st.sidebar.text('Traning the model')
    train_button = st.sidebar.button('Train the model')
    gap = st.sidebar.text('')
    gap = st.sidebar.text('Select what model to use')
    checkbox_custom = st.sidebar.checkbox('Use my trained model')
    checkbox_pretrained = st.sidebar.checkbox('Use pre-trained model')
    inference_button = st.sidebar.button('Test the model')
    gap = st.sidebar.text('')
    gap = st.sidebar.text('Zip the output data')
    zip_output = st.sidebar.button('Zip files')
    gap = st.sidebar.text('Download output')
    zip_file_root = 'output.zip'
    isZipExist = os.path.exists(zip_file_root)
    
    if isZipExist:
        with open("output.zip", "rb") as fp:
            download_output = st.sidebar.download_button(
                label="Download ZIP",
                data=fp,
                file_name="output.zip",
                mime="application/zip"
            )
    

    if choice == 'Train images':
        placeholder_heading.subheader('Upload train images')
        train_image_files = placeholder_data_loader.file_uploader("", type=['png','jpg','jpeg'], accept_multiple_files=True)

        if train_image_files is not None:
            for train_image_file in train_image_files:
                st.image(load_image(train_image_file),width=256)
                #saving image
                train_image_folder_name = 'train_images'
                isExist = os.path.exists(train_image_folder_name)
                if not isExist:
                    os.makedirs(train_image_folder_name)
                with open(os.path.join(train_image_folder_name,train_image_file.name),'wb') as f:
                    f.write((train_image_file).getbuffer())
            #process_status = placeholder.success("Files saved")

    if choice == 'Train labels':
        placeholder_heading.subheader('Upload train labels')
        train_image_files = placeholder_data_loader.file_uploader("", type=['png','jpg','jpeg'], accept_multiple_files=True)

        if train_image_files is not None:
            for train_image_file in train_image_files:
                st.image(load_image(train_image_file),width=256)
                #saving image
                train_label_folder_name = 'train_labels'
                isExist = os.path.exists(train_label_folder_name)
                if not isExist:
                    os.makedirs(train_label_folder_name)
                with open(os.path.join(train_label_folder_name,train_image_file.name),'wb') as f:
                    f.write((train_image_file).getbuffer())
            #placeholder.success("Files saved")

    if choice == ('Test images'):
        placeholder_heading.subheader('Upload test images')
        train_image_files = placeholder_data_loader.file_uploader("", type=['png','jpg','jpeg'], accept_multiple_files=True)

        if train_image_files is not None:
            for train_image_file in train_image_files:
                st.image(load_image(train_image_file),width=256)
                #saving image
                test_images_folder_name = 'test_images'
                isExist = os.path.exists(test_images_folder_name)
                if not isExist:
                    os.makedirs(test_images_folder_name)
                with open(os.path.join(test_images_folder_name,train_image_file.name),'wb') as f:
                    f.write((train_image_file).getbuffer())
            #placeholder.success("Files saved")

    if inference_button:
        placeholder_data_loader.empty()
        placeholder_heading.empty()
        st.subheader('Model inferencing')
        st.progress(10)
        st.subheader("wait the execution")
        with st.spinner('wait for it...'):
            time.sleep(10)

    if train_button:
        placeholder_data_loader.empty()
        placeholder_heading.empty()
        st.subheader('Model training')
        st.progress(10)
        st.subheader("wait the execution")
        with st.spinner('wait for it...'):
            time.sleep(10)

    if zip_output:
        placeholder_data_loader.empty()
        placeholder_heading.empty()
        with st.spinner('Zipping output files'):
            time.sleep(5)
            compress_data()


if __name__=='__main__':
    main()
