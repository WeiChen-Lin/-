from flask import *
from datetime import date
import re
from calendar import monthrange

def OutputDay(cycle, settle, payday, today):
    
    payday = payday.split("-")
    today = today.split("-")

    #相差日期
    delta = date(int(today[0]), int(today[1]), int(today[2])) - date(int(payday[0]), int(payday[1]), int(payday[2]))

    if delta.days >= 1:

        if int(today[1]) - int(payday[1]) < 1:

            month_plus = int(payday[1]) + int(cycle)

            #判斷年分
            if month_plus // 12 >= 1 and month_plus % 12 > 0:
                
                payday[0] = int(payday[0]) + (month_plus // 12)  
            
            elif month_plus // 12 >= 1:

                payday[0] = int(payday[0]) + (month_plus // 12) - 1
            
            else:

                payday[0] = int(payday[0])

            #判斷月份
            if month_plus % 12 > 0:
        
                payday[1] = month_plus % 12
        
            else:

                payday[1] = 12

            #判斷日期
            if monthrange(payday[0], payday[1])[1] < settle:

                payday[2] = monthrange(payday[0], payday[1])[1]
            
            else:

                payday[2] = settle

            #回傳日期
            for i in range(len(payday)):

                if payday[i] < 10:
                    
                    payday[i] = "0" + str(payday[i])

                else:
                    payday[i] = str(payday[i])  

            return "-".join(payday)
        
        else:
            
            month_plus = int(today[1]) + cycle

            #判斷年分
            if month_plus // 12 >= 1 and month_plus % 12 > 0:
                
                today[0] = int(today[0]) + (month_plus // 12)  
            
            elif month_plus // 12 >= 1:

                today[0] = int(today[0]) + (month_plus // 12) - 1
            
            else:

                today[0] = int(today[0])

            #判斷月份
            if month_plus % 12 > 0:
        
                today[1] = month_plus % 12
        
            else:

                today[1] = 12

            #判斷日期
            if monthrange(today[0], today[1])[1] < settle:

                today[2] = monthrange(today[0], today[1])[1]
            
            else:

                today[2] = settle

            #回傳日期
            for i in range(len(today)):

                if today[i] < 10:
                    
                    today[i] = "0" + str(today[i])

                else:
                    today[i] = str(today[i])  

            return "-".join(today)

    else: 
        
        return "-".join(payday)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route("/q2", methods=["POST"])
def returndate():
    
    data = request.get_json()


    return( jsonify({
        "message":OutputDay(int(data["cycle"]), int(data["settle"]), data["payday"], data["today"])
        }), 200)






if __name__ == '__main__':
    app.run(debug=True, port=5000)