import time
import numpy as np

from Matching_timestamps.Solutions.TwoPointers_numba import match_timestamps
from benchmark import make_timestamps


def perf_measurement():
    """
    Performance measurement procedure
    """
    st_ts = time.time()
    fn_ts = st_ts + 3600 * 2
    fps = 30
    ts1 = make_timestamps(fps, st_ts, fn_ts)
    ts2 = make_timestamps(fps, st_ts + 200, fn_ts)
    # warmup
    for _ in range(10):
        match_timestamps(ts1, ts2)
    n_iter = 100
    t0 = time.perf_counter()
    for _ in range(n_iter):
        match_timestamps(ts1, ts2)
    print(f"Perf time: {(time.perf_counter() - t0) / n_iter} seconds")


def main():
    """
    Setup:
        Say we have two videocameras, each filming the same scene. We make
        a prediction based on this scene (e.g. detect a human pose).
        To improve the robustness of the detection algorithm,
        we average the predictions from both cameras at each moment.
        The camera data is a pair (frame, timestamp), where the timestamp
        represents the moment when the frame was captured by the camera.

    Problem:
        For each frame of camera1, we need to find the index of the
        corresponding frame received by camera2. The frame i from camera2
        corresponds to the frame j from camera1, if
        abs(timestamps[i] - timestamps[j]) is minimal for all i.

    Estimation criteria:
        - The solution has to be optimal algorithmically. As an example, let's assume that
    the best solution has O(n^3) complexity. In this case, the O(n^3 * logn) solution will add -1 point penalty,
    O(n^4) will add -2 points and so on.
        - The solution has to be optimal python-wise.
    If it can be optimized ~x5 times by rewriting the algorithm in Python,
    this will add -1 point. x20 times optimization will result in -2 points.
    You may use any optimization library!
        - All corner cases must be handled correctly. A wrong solution will add -3 points.
        - The base score is 6.
        - Parallel implementation adds +1 point, provided it is effective (cannot be optimized x5 times)
        - 3 points for this homework are added by completing the second problem (the one with the medians).
    Optimize the solution to work with ~2-3 hours of data.
    Good luck!
    """

    perf_measurement()


if __name__ == '__main__':
    main()
