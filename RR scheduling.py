#  RR scheduling
# function หา waiting time ของทุก process
def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = [0] * n  # สร้าง array สำหรับเก็บเวลาที่เหลือของ burst time

    # คัดลอก burst time ไปยัง rem_bt[]
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0  # เวลาปัจจุบัน

    # ทำการวนซ้ำ processes ในรูปแบบ round robin
    # จนกว่าทุก process จะเสร็จสมบูรณ์
    while(1):
        done = True  # ตัวบ่งชี้ว่าทุก process เสร็จแล้วหรือยัง

        # วนซ้ำทุก process
        for i in range(n):

            # ตรวจสอบว่า burst time ของ process มากกว่า 0 หรือไม่
            if (rem_bt[i] > 0):
                done = False  # ยังมี process ที่ต้องดำเนินการ

                # ถ้า burst time มากกว่า quantum
                if (rem_bt[i] > quantum):

                    # เพิ่มค่า t เพื่อบอกว่า process ใช้เวลาไปเท่าไร
                    t += quantum

                    # ลดค่า burst time ของ process ปัจจุบันลงตาม quantum
                    rem_bt[i] -= quantum

                # ถ้า burst time น้อยกว่าหรือเท่ากับ quantum
                # เป็นรอบสุดท้ายของ process นี้
                else:

                    # เพิ่มค่า t เพื่อบอกว่า process ใช้เวลาไปทั้งหมด
                    t = t + rem_bt[i]

                    # คำนวณ waiting time = เวลาปัจจุบัน - burst time
                    wt[i] = t - bt[i]

                    # ตั้งค่า burst time ที่เหลือของ process นี้เป็น 0
                    rem_bt[i] = 0

        # ถ้าทุก process เสร็จสมบูรณ์
        if (done == True):
            break

# function หา turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):

    # คำนวณ turnaround time = burst time + waiting time
    for i in range(n):
        tat[i] = bt[i] + wt[i]


# function คำนวณค่าเฉลี่ยของ waiting time และ turn-around time
def findavgTime(processes, n, bt, quantum):
    wt = [0] * n  # สร้างอาร์เรย์สำหรับ waiting time
    tat = [0] * n  # สร้างอาร์เรย์สำหรับ turnaround time

    # เรียก function เพื่อหา waiting time ของทุก process
    findWaitingTime(processes, n, bt, wt, quantum)

    # เรียก function เพื่อหา turn around time ของทุก process
    findTurnAroundTime(processes, n, bt, wt, tat)

    # แสดงผล process พร้อมรายละเอียด
    print("Processes    Burst Time     Waiting",
          "Time    Turn-Around Time")
    total_wt = 0  # รวมค่า waiting time
    total_tat = 0  # รวมค่า turnaround time
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i],
              "\t\t", wt[i], "\t\t", tat[i])

    # แสดงค่าเฉลี่ย waiting time และ turn around time
    print("\nAverage waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = %.5f " % (total_tat / n))


# ส่วนของ Driver code
if __name__ == "__main__":

    # รหัสของ process
    proc = [1, 2, 3]
    n = 3  # จำนวน process

    # burst time ของแต่ละ process
    burst_time = [10, 5, 8]

    # ค่า time quantum
    quantum = 2

    # เรียกใช้ function เพื่อคำนวณค่าเฉลี่ย
    findavgTime(proc, n, burst_time, quantum)
