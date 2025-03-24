# OS-scheduling
OS Scheduling Algorithm
## First-Come, First-Served (FCFS) Scheduling
แนวคิด:
- จัดลำดับการทำงานของ process ตามลำดับที่เข้ามาในระบบ (เหมือนคิว FIFO)
- ไม่มีการสลับเปลี่ยน process จนกว่าจะเสร็จ

ข้อดี:
- เข้าใจง่าย และใช้ทรัพยากรต่ำ
- Context Switching ต่ำ

ข้อเสีย:
- เกิด Convoy Effect ถ้า process ที่มาก่อนใช้เวลานาน process ที่ตามมาจะต้องรอนานมาก
- ไม่เหมาะกับระบบที่ต้องการตอบสนองเร็ว

## Round Robin (RR) Scheduling
แนวคิด:
- จัด process แบบหมุนเวียน โดยแต่ละ process จะได้รับเวลาการทำงานตาม Time Quantum
- ถ้า process ยังไม่เสร็จภายใน TQ ก็จะถูกพักและส่งไปต่อท้ายคิว รอรอบถัดไป

ข้อดี:
- ลดปัญหา Convoy Effect
- ทุก process ได้รับโอกาสทำงานเท่าๆกัน
- เหมาะกับระบบ Multitasking

ข้อเสีย:
- มีการ Context Switching บ่อย
- ถ้าเลือก TQ ไม่เหมาะสม (มากเกินไปหรือเล็กเกินไป) อาจส่งผลให้การทำงานไม่มีประสิทธิภาพ

## Shortest Job First (SJF) Scheduling
แนวคิด:
- เลือก process ที่ใช้เวลา Burst Time น้อยที่สุดมาทำก่อน
- มี 2 ประเภท
1. Non-preemptive SJF: หาก process เริ่มทำงานแล้ว จะไม่ถูกขัดจังหวะ
2. Preemptive SJF: หากมี process ใหม่ที่มี Burst Time สั้นกว่ากำลังรันอยู่ จะสลับไปทำ process ใหม่นั้นก่อน

ข้อดี:
- ลด Average Waiting Time
- มีประสิทธิภาพสูงกว่าวิธีอื่นๆ

ข้อเสีย:
- อาจเกิดปัญหา Starvation
- ต้องรู้ Burst Time ล่วงหน้า 