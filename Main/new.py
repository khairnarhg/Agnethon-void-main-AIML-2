{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "News 1 ) Google’s pause on Gemini’s ability to generate AI images of people | Explained - The Hindu\n",
      "News 2 ) Putin Critic May Have Been Killed With \"Single Punch To Heart\": Report - NDTV\n",
      "News 3 ) Scientists measure gravity at microscopic scale, say it paves way for understanding quantum gravity - Deccan Herald\n",
      "News 4 ) Sheikh Shahjahan, his men tortured tribals, took wages: Sandeshkhali probe team - Hindustan Times\n",
      "News 5 ) Sonakshi Sinha, Aditi Rao Hydari, Richa Chadha share BTS pics of Heeramandi on Sanjay Leela Bhansali's birthday - Hindustan Times\n",
      "News 6 ) India vs England, 4th Test Match Day 2 Highlights: Dhruv Jurel-Kuldeep Yadav Help Seven-Down India Fight Back - NDTV Sports\n",
      "News 7 ) Chandrababu Naidu, Pawan Kalyan's Andhra Polls List Leaves Room For BJP - NDTV\n",
      "News 8 ) Bishop passes verdict on Jaiswal's not out decision that left England shocked - Hindustan Times\n",
      "News 9 ) Adhir Ranjan says TMC in dilemma over seat-sharing; party hits back - Hindustan Times\n",
      "News 10 ) 6 dry fruits that help sharpen the memory - Moneycontrol\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import json\n",
    "r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0ce7ce0d861141d0bbf3c527b076ba07')\n",
    "r\n",
    "data=json.loads(r.content)\n",
    "\n",
    "for i in range(10):\n",
    "    News=data['articles'][i]['title']\n",
    "    print(\"News\",i+1,\")\",News)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
