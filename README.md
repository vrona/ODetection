# Hazardous_OT

Hazardous Objects Tracking

Principle
In step 1: in order to contribute to reduce the number puncture occured by debris*, we are developing a computer vision model that able to detect and track from small to big debris*, on any given racetrack.

In step 1.5: locate the debris.

In step 2: additional objects and scene interpretation will be included, such as:
- track itself,
- racing vehicle car and moto (while performing/crashing),
- drivers (while driving / fallen / sliding)
- lane, lines,
- grass,
- wall,
- deceleration zone,
- gravel,
- curbs (flat curbstones lining the corners and chicanes),

*debris: is a piece of any parts (whole or broken) that may have been lost or ejected after a collision from a racing vehicle.

NB: objects like debris have their shapes which may change in the case when they are moving or if the camera moves.
They then appear bigger or smaller frame after frame.

The domain of the problem
Online multi-object tracking (MOT) for high-level spatial reasoning and path planning for autonomous and highly-automated vehicles.

Strategy
tracking-by-detection online (aka real-time)

detection : Yolov5 (backbone)
tracking: DeepSort (or SORT)

Yolov5 is natively not dedicated to any "content" from motorsport.
Thus, a racing Yolov5 model has to be made and based on a dedicated racing dataset.

Scenarii and Data

2D MOT via vision sensor (monocular camera) from nose cam or top cam -  embedded model Hazardous DT
2D MOT via race track edge camera - model at local safety desk officer.

Evaluation Metrics
 We cannot miss tiny debris as it may cause a puncture which may lead to a lethal accident.
Strong Recall (among the actual positive, how often does the model predict positive?).
Correctly tracked, falsely tracked, True and False Positive rates.


mAP (to check)


"Recent progress in 2D MOT has focused on the tracking-by-detection strategy, where object detections from a category detector are linked to form trajectories of the targets. To perform tracking-by-detection online (i.e. in a causal fashion), the major challenge is to correctly associate noisy object detections in the current video frame with pre- viously tracked objects"

source (No Blind Spots: Full-Surround Multi-Object Tracking for Autonomous Vehicles using Cameras & LiDARs - (Akshay Rangesh†, Member, IEEE, and Mohan M. Trivedi†, Fellow, IEEE) )
