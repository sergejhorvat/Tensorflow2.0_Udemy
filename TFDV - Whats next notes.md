We’ve covered a lot in this section - from covering importing a dataset to making the TensorFlow Data Validation schema that detects anomalies in the serving time as well!
However, what’s next? What to do after saving the Schema?


The TensorFlow Data Validation (TFDV) is a small part of the technology stack called TensorFlow Extended, which is made to carry the whole deep learning project end-to-end.


The Schema that we saved in the last video of this section can be used in multiple ways. The most common way would we with the TensorFlow Transform, also part of the TensorFlow Extended technology stack, covered in the next section. This behavior is useful in the end-to-end pipelines because the TensorFlow Transform knows what data to expects based on statistics generated in the Schema.


There is also a handy way of using the Schema, and that is data validation before the inference time.


Here are a few additional links where you can read/learn more about the TFDV and how to use it in the end-to-end pipelines:


1. Great blog post that explains how to use data visualization part of the TFDV and feature engineering process in more details:

    https://towardsdatascience.com/hands-on-tensorflow-data-validation-61e552f123d7


2. TensorFlow source tutorial on how to leverage the TFDV in the end-to-end pipelines:

    https://www.tensorflow.org/tfx/guide/tfdv


3. TensorFlow Data Validation - custom data validation pipeline:

    https://www.tensorflow.org/tfx/data_validation/get_started
