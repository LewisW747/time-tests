import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    if end_time < start_time:
         raise ValueError("End time cannot be before start time!")
    else:
        start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
        sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                    start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                    for i in range(number_of_intervals)]
        return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):  
        overlap_time = []

        start1 = range1[0][0]
        end1 = range1[-1][-1]

        start2 = range2[0][0]
        end2 = range2[-1][-1]

        start = min(start1, start2)
        end = max(end1, end2)

        for i in range1:
             for j in range2:
                  int1_start = i[0]
                  int1_end = i[-1]

                  int2_start = j[0]
                  int2_end = j[-1]

                  if int1_start > start and int1_end < end:
                       overlap_time.append((int1_start, int1_end))
                  elif int1_start > start and int1_end > end:
                        overlap_time.append((int1_start))
                  elif int1_start < start and int1_end < end:
                        overlap_time.append((int1_end))
                  
                  if int2_start > start and int2_end < end:
                                         overlap_time.append((int2_start, int2_end))
                  elif int2_start > start and int2_end > end:
                                          overlap_time.append((int2_start))
                  elif int2_start < start and int2_end < end:
                                          overlap_time.append((int2_end))

        return overlap_time

