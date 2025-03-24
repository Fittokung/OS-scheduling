# FCFS scheduling
# function หา waiting time ขอทุก process
def findWaitingTime(processes, n, bt, wt):

    # waiting time ของ process แรก = 0
    wt[0] = 0

    # คำนวณ
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

# function หา turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):

    # คำนวณ turn around time โดยการบวก bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# function คำนวณค่าเฉลี่ย
def findavgTime(processes, n, bt):

    wt = [0] * n  # เวลารอของแต่ละ process
    tat = [0] * n  # เวลาเสร็จสิ้นของแต่ละ process
    total_wt = 0  # รวมเวลารอ
    total_tat = 0  # รวมเวลาเสร็จสิ้น

    # เรียก function เพื่อหา waiting time ของทุก process
    findWaitingTime(processes, n, bt, wt)

    # เรียก function เพื่อหา turn around time ของทุก process
    findTurnAroundTime(processes, n, bt, wt, tat)

    # แสดง process พร้อมรายละเอียด
    print("Processes Burst time " +
          " Waiting time " +
          " Turn around time")

    # คำนวณรวม waiting time และรวม turn around time
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +
              str(bt[i]) + "\t " +
              str(wt[i]) + "\t\t " +
              str(tat[i]))

    # แสดงผลค่าเฉลี่ย waiting time และ turn around time
    print("Average waiting time = " +
          str(total_wt / n))
    print("Average turn around time = " +
          str(total_tat / n))

if __name__ == "__main__":

    # รหัสของ process
    processes = [1, 2, 3]
    n = len(processes)  # จำนวน process

    # เวลา Burst ของแต่ละ process
    burst_time = [10, 5, 8]

    # เรียกใช้ function คำนวณค่าเฉลี่ย
    findavgTime(processes, n, burst_time)
