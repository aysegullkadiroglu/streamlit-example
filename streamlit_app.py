{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aysegullkadiroglu/streamlit-example/blob/master/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "SgzXi_ev_7lv"
      },
      "outputs": [],
      "source": [
        "# @title Setup code\n",
        "!pip install -q streamlit"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eQVBXF9fLJAR",
        "outputId": "f387db9d-c1c8-49c0-cbb8-bf84b73aaa83"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app.py"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ROd2ygQhI1No",
        "outputId": "a1b2f619-518e-4dfd-d279-c1666500bdef"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.10/dist-packages (7.0.0)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.1)\n"
          ]
        }
      ],
      "source": [
        "!pip install pyngrok"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "owsL9d_8Hpi2",
        "outputId": "3c3614ce-f1e1-42af-ce9e-33d8b3cb7a18"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "itoFgw68_1VV",
        "outputId": "9e6a8518-8101-413e-9168-0947579ae120"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2023-11-05 18:02:08.352 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "import pickle\n",
        "import streamlit as st\n",
        "\n",
        "# yukarıdakileri fonkisyona alalım\n",
        "def recommend_movie(movie):\n",
        "  index = netflix_data_v2[netflix_data_v2['TITLE']==movie].index[0]\n",
        "  # benzerlik değerlerine göre sıralayıp uzaklık değerine atıyoruz\n",
        "  distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])\n",
        "  recommended_movies_name = []\n",
        "  for index, _ in distance[:10]:\n",
        "     index = netflix_data_v2.iloc[i[0]]['index']\n",
        "     recommended_movies_name.append(netflix_data_v2['TITLE'])\n",
        "  return recommended_movies_name\n",
        "\n",
        "st.header(\"Netflix Movie Recommendation System\")\n",
        "netflix_data_v2 = np.load('drive/MyDrive/netflix_titles.pkl', allow_pickle = True)\n",
        "\n",
        "similarity = np.load('drive/MyDrive/netflix_titles.pkl', allow_pickle = True)\n",
        "\n",
        "movie_list = netflix_data_v2['TITLE'].values\n",
        "select_movie = st.selectbox(\n",
        "    \"Please type or select a movie for recommendation\",\n",
        "    movie_list\n",
        ")\n",
        "\n",
        "if st.button(\"Show recommendation\"):\n",
        "    recommended_movies_name = recommend_movie(select_movie)\n",
        "\n",
        "    # Display the recommended movie titles\n",
        "    st.write(\"Recommended Movies:\")\n",
        "    for movie_name in recommended_movies_name:\n",
        "        st.write(movie_name)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1wCfitPn6Az0rtP38HpCeCLpxPQVuBRyR",
      "authorship_tag": "ABX9TyOhlIV0jrWEr+meMytLJnqR",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}