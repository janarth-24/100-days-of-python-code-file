{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "783ff0f0-f830-4757-bacd-fb1a6d690fc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guessing number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "To low!, Try again\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guessing number 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "To high!, Try again\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guessing number 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exactly you find the secret number\n",
      "Sorry!, your attempt are over the secret number is 8\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "secret_number=random.randint(0,9)\n",
    "attempt=3\n",
    "while attempt>0:\n",
    "    guessing_number=int(input(\"Enter your guessing number\"))\n",
    "    if secret_number==guessing_number:\n",
    "        print(\"Exactly you find the secret number\")\n",
    "    elif secret_number<guessing_number:\n",
    "        print(\"To high!, Try again\")\n",
    "    else:\n",
    "        print(\"To low!, Try again\") \n",
    "    attempt-=1\n",
    "if attempt==0:\n",
    "    print(\"Sorry!, your attempt are over the secret number is\",secret_number)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09532703-637b-494a-a40e-dcdca2304152",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
