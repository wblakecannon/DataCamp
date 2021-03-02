'''
NMF applied to Wikipedia articles

In the video, you saw NMF applied to transform a toy word-frequency array. Now it's your turn to apply NMF, this time using the tf-idf word-frequency array of Wikipedia articles, given as a csr matrix articles. Here, fit the model and transform the articles. In the next exercise, you'll explore the result.

INSTRUCTIONS
100XP
Import NMF from sklearn.decomposition.
Create an NMF instance called model with 6 components.
Fit the model to the word count data articles.
Use the .transform() method of model to transform articles, and assign the result to nmf_features.
Print nmf_features to get a first idea what it looks like (.round(2) rounds the entries to 2 decimal places.).
'''
# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

# Print the NMF features
print(nmf_features.round(2))
