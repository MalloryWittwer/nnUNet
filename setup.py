from setuptools import setup, find_namespace_packages

setup(name='nnunetv2',
      packages=find_namespace_packages(include=["nnunetv2", "nnunetv2.*"]),
      version='2.1.1',
      description='nnU-Net. Framework for out-of-the box biomedical image segmentation.',
      url='https://github.com/MIC-DKFZ/nnUNet',
      author='Helmholtz Imaging Applied Computer Vision Lab, Division of Medical Image Computing, German Cancer Research Center',
      author_email='f.isensee@dkfz-heidelberg.de',
      license='Apache License Version 2.0, January 2004',
      python_requires=">=3.9",
      install_requires=[
          "torch>=2.0.0",
          "acvl-utils>=0.2",
          "dynamic-network-architectures>=0.2",
          "tqdm",
          "dicom2nifti",
          "scikit-image>=0.14",
          "medpy",
          "scipy",
          "batchgenerators>=0.25",
          "numpy",
          "scikit-learn",
          "scikit-image>=0.19.3",
          "SimpleITK>=2.2.1",
          "pandas",
          "graphviz",
          'tifffile',
          'requests',
          "nibabel",
          "matplotlib",
          "seaborn",
          "imagecodecs",
          "yacs",
        #   "csbdeep"
      ],
      entry_points={
          'console_scripts': [
              'nnUNetv2_predict = nnunetv2.inference.predict_from_raw_data:predict_entry_point',  # api available
          ],
      },
      keywords=['deep learning', 'image segmentation', 'medical image analysis',
                'medical image segmentation', 'nnU-Net', 'nnunet']
      )
