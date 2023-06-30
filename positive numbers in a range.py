{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gollasrihitha/MyCaptain-Python/blob/main/positive%20numbers%20in%20a%20range.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "list1=[12,-7,5,64,-14]\n",
        "print(list1)\n",
        "l=[]\n",
        "for i in list1:\n",
        "  if i>0:\n",
        "    l.append(i)\n",
        "    print(l)\n",
        "\n",
        "list2=[12,14,-95,3]\n",
        "print(list2)\n",
        "l=[]\n",
        "for i in list2:\n",
        "  if i>0:\n",
        "    l.append(i)\n",
        "    print(l)\n",
        ""
      ],
      "metadata": {
        "id": "PE7NGjcHVrIe",
        "outputId": "5495f880-c708-4153-eae4-b8ef7d61fe93",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[12, -7, 5, 64, -14]\n",
            "[12]\n",
            "[12, 5]\n",
            "[12, 5, 64]\n",
            "[12, 14, -95, 3]\n",
            "[12]\n",
            "[12, 14]\n",
            "[12, 14, 3]\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colaboratory",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}