''' A test checking program
    Copyright (C) 2026 HippoProgrammer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''
print(''' q3.py  Copyright (C) 2026  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')

def mean(data):
    return sum(data)/len(data)
def analyseScores(scores:list):
    mean_score = mean(scores)
    greater_scores = 0
    for score in scores:
        if score > mean_score:
            greater_scores += 1
    return (mean_score,greater_scores)