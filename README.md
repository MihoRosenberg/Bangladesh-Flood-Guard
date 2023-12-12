# **Bangladesh-Flood-Guard**
[Streamlit Web App](https://bangladesh-flood-guard-k65x4wbqyaykvbgf8jyunl.streamlit.app/)
## **Problem Statement**
The aftermath of flooding in Bangladesh results in immediate and long-term challenges, including loss of lives, destruction of crops, damage to infrastructure, and displacement of communities. Timely and accurate flood prediction and waterbody forecasting are crucial for reducing the impact of floods, enabling better disaster preparedness, and facilitating effective resource allocation.
## **Model Overview** 
The study predicts the daily average precipitation for four divisions in Bangladesh- Dhaka, Khulna, Mymensingh, and Narayanganj- using RandomForest Regressor. The model’s performance was evaluated: 
|Metrics|Value|
| --- | --- |
|R2 score|0.71|
|MSE|19.50|
|MAE|2.33|

## **Further Consideration** 
A possible way to reduce the negative effects and prevent further harm is to use a real-time prediction mechanism. This would allow for timely and accurate responses to the situation. To achieve this, an automated end-to-end ML pipeline is suggested. The pipeline would collect data through API, transform it into a suitable format, and deliver a near real-time prediction.

