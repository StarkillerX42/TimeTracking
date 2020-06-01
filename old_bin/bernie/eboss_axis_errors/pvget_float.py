#!/usr/bin/env python

# bernie Tue. 26 June '18
# just playing around:  a script to retrieve arbitrarily defined intervals of APO process variables

import datetime
from channelarchiver import Archiver, codes, utils
ss='http://sdss-telemetry.apo.nmsu.edu/telemetry/cgi/ArchiveDataServer.cgi'

archiver = Archiver(ss)
archiver.scan_archives()

# DEFAULT INTERVAL IS PAST 24 HOURS BUT WE SHOULD BE ABLE TO OVERRIDE ON THE COMMAND-LINE:
# start = str(datetime.datetime.utcnow() - datetime.timedelta(days=1))	# 1 day before current moment
# end = str(datetime.datetime.utcnow())			# current moment
# print "# DIAGNOSTIC: start:  " + start
# print "# DIAGNOSTIC: end:    " + end
# start='2018-10-10 01:00:00'
# end='2018-10-10 12:00:00'

periods = ([ '2017-10-01 00:00:00', '2017-10-01 12:19:33' ], \
	[ '2017-10-02 00:00:00', '2017-10-02 11:43:34' ], \
	[ '2017-10-08 00:00:00', '2017-10-08 12:14:30' ], \
	[ '2017-10-09 00:00:00', '2017-10-09 12:23:45' ], \
	[ '2017-10-10 00:00:00', '2017-10-10 12:40:04' ], \
	[ '2017-10-11 00:00:00', '2017-10-11 12:56:26' ], \
	[ '2017-10-12 00:00:00', '2017-10-12 12:30:08' ], \
	[ '2017-10-13 00:00:00', '2017-10-13 11:07:09' ], \
	[ '2017-10-14 00:00:00', '2017-10-14 12:32:42' ], \
	[ '2017-10-15 00:00:00', '2017-10-15 12:47:11' ], \
	[ '2017-10-16 00:00:00', '2017-10-16 12:43:37' ], \
	[ '2017-10-17 00:00:00', '2017-10-17 12:20:21' ], \
	[ '2017-10-18 00:00:00', '2017-10-18 12:16:18' ], \
	[ '2017-10-19 00:00:00', '2017-10-19 12:38:45' ], \
	[ '2017-10-20 00:00:00', '2017-10-20 12:22:04' ], \
	[ '2017-10-21 00:00:00', '2017-10-21 12:36:07' ], \
	[ '2017-10-22 00:00:00', '2017-10-22 12:42:47' ], \
	[ '2017-10-23 00:00:00', '2017-10-23 11:16:18' ], \
	[ '2017-10-24 00:00:00', '2017-10-24 12:33:40' ], \
	[ '2017-10-25 00:00:00', '2017-10-25 12:35:45' ], \
	[ '2017-10-26 00:00:00', '2017-10-26 11:40:46' ], \
	[ '2017-10-27 00:00:00', '2017-10-27 13:15:08' ], \
	[ '2017-10-28 00:00:00', '2017-10-28 12:25:10' ], \
	[ '2017-10-29 00:00:00', '2017-10-29 12:32:49' ], \
	[ '2017-10-30 00:00:00', '2017-10-30 11:14:10' ], \
	[ '2017-10-31 00:00:00', '2017-10-31 12:34:44' ], \
	[ '2017-11-06 00:00:00', '2017-11-06 12:17:15' ], \
	[ '2017-11-07 00:00:00', '2017-11-07 12:39:25' ], \
	[ '2017-11-08 00:00:00', '2017-11-08 11:59:54' ], \
	[ '2017-11-09 00:00:00', '2017-11-09 13:08:37' ], \
	[ '2017-11-10 00:00:00', '2017-11-10 12:54:34' ], \
	[ '2017-11-11 00:00:00', '2017-11-11 12:40:46' ], \
	[ '2017-11-12 00:00:00', '2017-11-12 12:31:49' ], \
	[ '2017-11-13 00:00:00', '2017-11-13 12:09:49' ], \
	[ '2017-11-14 00:00:00', '2017-11-14 12:32:36' ], \
	[ '2017-11-15 00:00:00', '2017-11-15 12:42:07' ], \
	[ '2017-11-16 00:00:00', '2017-11-16 12:51:02' ], \
	[ '2017-11-17 00:00:00', '2017-11-17 12:54:59' ], \
	[ '2017-11-18 00:00:00', '2017-11-18 12:57:56' ], \
	[ '2017-11-19 00:00:00', '2017-11-19 13:06:09' ], \
	[ '2017-11-20 00:00:00', '2017-11-20 12:04:24' ], \
	[ '2017-11-21 00:00:00', '2017-11-21 12:57:17' ], \
	[ '2017-11-22 00:00:00', '2017-11-22 12:50:44' ], \
	[ '2017-11-23 00:00:00', '2017-11-23 12:54:31' ], \
	[ '2017-11-24 00:00:00', '2017-11-24 13:06:53' ], \
	[ '2017-11-25 00:00:00', '2017-11-25 13:00:17' ], \
	[ '2017-11-26 00:00:00', '2017-11-26 12:55:12' ], \
	[ '2017-11-27 00:00:00', '2017-11-27 13:01:11' ], \
	[ '2017-11-28 00:00:00', '2017-11-28 13:06:01' ], \
	[ '2017-11-29 00:00:00', '2017-11-29 11:27:32' ], \
	[ '2017-11-30 00:00:00', '2017-11-30 11:56:41' ], \
	[ '2017-11-30 00:00:00', '2017-11-30 12:01:48' ], \
	[ '2017-12-05 00:00:00', '2017-12-05 12:15:14' ], \
	[ '2017-12-06 00:00:00', '2017-12-06 11:32:32' ], \
	[ '2017-12-07 00:00:00', '2017-12-07 13:16:43' ], \
	[ '2017-12-08 00:00:00', '2017-12-08 13:21:18' ], \
	[ '2017-12-09 00:00:00', '2017-12-09 13:39:51' ], \
	[ '2017-12-10 00:00:00', '2017-12-10 13:31:12' ], \
	[ '2017-12-11 00:00:00', '2017-12-11 13:12:11' ], \
	[ '2017-12-12 00:00:00', '2017-12-12 13:38:48' ], \
	[ '2017-12-13 00:00:00', '2017-12-13 13:01:37' ], \
	[ '2017-12-14 00:00:00', '2017-12-14 13:07:27' ], \
	[ '2017-12-15 00:00:00', '2017-12-15 13:03:58' ], \
	[ '2017-12-16 00:00:00', '2017-12-16 12:46:02' ], \
	[ '2017-12-17 00:00:00', '2017-12-17 11:56:31' ], \
	[ '2017-12-18 00:00:00', '2017-12-18 11:54:45' ], \
	[ '2017-12-19 00:00:00', '2017-12-19 13:25:15' ], \
	[ '2017-12-20 00:00:00', '2017-12-20 13:09:42' ], \
	[ '2017-12-21 00:00:00', '2017-12-21 11:39:56' ], \
	[ '2017-12-22 00:00:00', '2017-12-22 12:52:25' ], \
	[ '2017-12-23 00:00:00', '2017-12-23 13:00:16' ], \
	[ '2017-12-24 00:00:00', '2017-12-24 13:08:25' ], \
	[ '2017-12-25 00:00:00', '2017-12-25 13:26:27' ], \
	[ '2018-01-04 00:00:00', '2018-01-04 13:28:54' ], \
	[ '2018-01-05 00:00:00', '2018-01-05 13:35:58' ], \
	[ '2018-01-06 00:00:00', '2018-01-06 11:52:59' ], \
	[ '2018-01-07 00:00:00', '2018-01-07 13:22:28' ], \
	[ '2018-01-08 00:00:00', '2018-01-08 13:49:53' ], \
	[ '2018-01-09 00:00:00', '2018-01-09 12:20:41' ], \
	[ '2018-01-10 00:00:00', '2018-01-10 12:22:36' ], \
	[ '2018-01-11 00:00:00', '2018-01-11 13:28:55' ], \
	[ '2018-01-12 00:00:00', '2018-01-12 13:13:59' ], \
	[ '2018-01-13 00:00:00', '2018-01-13 13:30:54' ], \
	[ '2018-01-14 00:00:00', '2018-01-14 13:30:54' ], \
	[ '2018-01-15 00:00:00', '2018-01-15 13:18:09' ], \
	[ '2018-01-16 00:00:00', '2018-01-16 12:47:50' ], \
	[ '2018-01-17 00:00:00', '2018-01-17 13:04:38' ], \
	[ '2018-01-18 00:00:00', '2018-01-18 12:53:45' ], \
	[ '2018-01-19 00:00:00', '2018-01-19 13:08:14' ], \
	[ '2018-01-20 00:00:00', '2018-01-20 11:50:36' ], \
	[ '2018-01-21 00:00:00', '2018-01-21 12:39:36' ], \
	[ '2018-01-22 00:00:00', '2018-01-22 13:06:23' ], \
	[ '2018-01-23 00:00:00', '2018-01-23 12:54:24' ], \
	[ '2018-01-24 00:00:00', '2018-01-24 13:17:19' ], \
	[ '2018-01-25 00:00:00', '2018-01-25 13:41:56' ], \
	[ '2018-01-26 00:00:00', '2018-01-26 13:22:24' ], \
	[ '2018-01-27 00:00:00', '2018-01-27 13:22:13' ], \
	[ '2018-02-02 00:00:00', '2018-02-02 13:31:59' ], \
	[ '2018-02-03 00:00:00', '2018-02-03 13:20:43' ], \
	[ '2018-02-04 00:00:00', '2018-02-04 13:34:25' ], \
	[ '2018-02-05 00:00:00', '2018-02-05 13:51:31' ], \
	[ '2018-02-06 00:00:00', '2018-02-06 13:19:17' ], \
	[ '2018-02-07 00:00:00', '2018-02-07 13:17:39' ], \
	[ '2018-02-08 00:00:00', '2018-02-08 13:07:38' ], \
	[ '2018-02-09 00:00:00', '2018-02-09 13:09:09' ], \
	[ '2018-02-10 00:00:00', '2018-02-10 11:52:05' ], \
	[ '2018-02-11 00:00:00', '2018-02-11 12:54:40' ], \
	[ '2018-02-12 00:00:00', '2018-02-12 13:13:58' ], \
	[ '2018-02-13 00:00:00', '2018-02-13 11:45:15' ], \
	[ '2018-02-14 00:00:00', '2018-02-14 10:28:05' ], \
	[ '2018-02-15 00:00:00', '2018-02-15 11:25:09' ], \
	[ '2018-02-16 00:00:00', '2018-02-16 11:20:01' ], \
	[ '2018-02-17 00:00:00', '2018-02-17 11:53:31' ], \
	[ '2018-02-18 00:00:00', '2018-02-18 11:44:27' ], \
	[ '2018-02-19 00:00:00', '2018-02-19 11:43:34' ], \
	[ '2018-02-20 00:00:00', '2018-02-20 11:34:22' ], \
	[ '2018-02-21 00:00:00', '2018-02-21 12:35:47' ], \
	[ '2018-02-22 00:00:00', '2018-02-22 12:26:10' ], \
	[ '2018-02-23 00:00:00', '2018-02-23 12:46:59' ], \
	[ '2018-02-24 00:00:00', '2018-02-24 12:37:40' ], \
	[ '2018-02-25 00:00:00', '2018-02-25 12:55:52' ], \
	[ '2018-03-11 00:00:00', '2018-03-11 11:13:08' ], \
	[ '2018-03-12 00:00:00', '2018-03-12 11:36:47' ], \
	[ '2018-03-13 00:00:00', '2018-03-13 12:34:34' ], \
	[ '2018-03-14 00:00:00', '2018-03-14 12:16:44' ], \
	[ '2018-03-15 00:00:00', '2018-03-15 12:28:10' ], \
	[ '2018-03-16 00:00:00', '2018-03-16 11:30:48' ], \
	[ '2018-03-17 00:00:00', '2018-03-17 11:39:41' ], \
	[ '2018-03-18 00:00:00', '2018-03-18 12:09:28' ], \
	[ '2018-03-19 00:00:00', '2018-03-19 12:20:09' ], \
	[ '2018-03-20 00:00:00', '2018-03-20 12:43:27' ], \
	[ '2018-03-21 00:00:00', '2018-03-21 12:46:16' ], \
	[ '2018-03-22 00:00:00', '2018-03-22 12:38:36' ], \
	[ '2018-04-10 00:00:00', '2018-04-10 12:10:07' ], \
	[ '2018-04-11 00:00:00', '2018-04-11 12:29:03' ], \
	[ '2018-04-12 00:00:00', '2018-04-12 10:24:36' ], \
	[ '2018-04-13 00:00:00', '2018-04-13 12:13:14' ], \
	[ '2018-04-14 00:00:00', '2018-04-14 12:25:35' ], \
	[ '2018-04-16 00:00:00', '2018-04-16 12:24:50' ], \
	[ '2018-04-17 00:00:00', '2018-04-17 12:21:28' ], \
	[ '2018-04-18 00:00:00', '2018-04-18 12:15:17' ], \
	[ '2018-04-19 00:00:00', '2018-04-19 11:19:08' ], \
	[ '2018-04-20 00:00:00', '2018-04-20 10:56:51' ], \
	[ '2018-05-09 00:00:00', '2018-05-09 11:51:26' ], \
	[ '2018-05-10 00:00:00', '2018-05-10 11:29:54' ], \
	[ '2018-05-11 00:00:00', '2018-05-11 11:53:26' ], \
	[ '2018-05-12 00:00:00', '2018-05-12 11:43:01' ], \
	[ '2018-05-13 00:00:00', '2018-05-13 11:57:20' ], \
	[ '2018-05-14 00:00:00', '2018-05-14 11:53:58' ], \
	[ '2018-05-15 00:00:00', '2018-05-15 11:45:09' ], \
	[ '2018-05-16 00:00:00', '2018-05-16 11:16:01' ], \
	[ '2018-05-17 00:00:00', '2018-05-17 11:59:07' ], \
	[ '2018-05-18 00:00:00', '2018-05-18 11:43:44' ], \
	[ '2018-05-19 00:00:00', '2018-05-19 11:07:16' ], \
	[ '2018-05-20 00:00:00', '2018-05-20 11:05:35' ], \
	[ '2018-06-08 00:00:00', '2018-06-08 10:33:19' ], \
	[ '2018-06-09 00:00:00', '2018-06-09 10:17:39' ], \
	[ '2018-06-10 00:00:00', '2018-06-10 11:30:46' ], \
	[ '2018-06-11 00:00:00', '2018-06-11 11:38:37' ], \
	[ '2018-06-12 00:00:00', '2018-06-12 11:32:42' ], \
	[ '2018-06-13 00:00:00', '2018-06-13 11:37:33' ], \
	[ '2018-06-14 00:00:00', '2018-06-14 11:25:25' ], \
	[ '2018-06-15 00:00:00', '2018-06-15 10:03:17' ], \
	[ '2018-06-16 00:00:00', '2018-06-16 11:00:18' ], \
	[ '2018-06-17 00:00:00', '2018-06-17 11:14:54' ], \
	[ '2018-06-18 00:00:00', '2018-06-18 11:21:41' ], \
	[ '2018-06-19 00:00:00', '2018-06-19 11:19:55' ], \
	[ '2018-09-18 00:00:00', '2018-09-18 11:58:47' ], \
	[ '2018-09-19 00:00:00', '2018-09-19 11:01:17' ], \
	[ '2018-09-20 00:00:00', '2018-09-20 12:16:42' ], \
	[ '2018-09-21 00:00:00', '2018-09-21 11:50:46' ], \
	[ '2018-09-28 00:00:00', '2018-09-28 12:52:03' ], \
	[ '2018-09-29 00:00:00', '2018-09-29 12:52:45' ], \
	[ '2018-09-30 00:00:00', '2018-09-30 12:34:49' ], \
	[ '2018-10-01 00:00:00', '2018-10-01 11:15:51' ], \
	[ '2018-10-02 00:00:00', '2018-10-02 10:52:29' ], \
	[ '2018-10-03 00:00:00', '2018-10-03 12:08:27' ], \
	[ '2018-10-04 00:00:00', '2018-10-04 12:47:57' ], \
	[ '2018-10-05 00:00:00', '2018-10-05 12:07:12' ], \
	[ '2018-10-06 00:00:00', '2018-10-06 11:34:58' ], \
	[ '2018-10-07 00:00:00', '2018-10-07 10:57:52' ], \
	[ '2018-10-08 00:00:00', '2018-10-08 11:00:46' ], \
	[ '2018-10-09 00:00:00', '2018-10-09 12:42:56' ], \
	[ '2018-10-10 00:00:00', '2018-10-10 12:24:21' ], \
	[ '2018-10-11 00:00:00', '2018-10-11 11:12:14' ], \
	[ '2018-10-12 00:00:00', '2018-10-12 11:27:05' ], \
	[ '2018-10-13 00:00:00', '2018-10-13 10:52:18' ], \
	[ '2018-10-14 00:00:00', '2018-10-14 10:55:58' ], \
	[ '2018-10-15 00:00:00', '2018-10-15 11:31:42' ], \
	[ '2018-10-16 00:00:00', '2018-10-16 11:06:13' ], \
	[ '2018-10-17 00:00:00', '2018-10-17 10:15:17' ], \
	[ '2018-10-18 00:00:00', '2018-10-18 11:16:37' ], \
	[ '2018-10-19 00:00:00', '2018-10-19 11:14:50' ], \
	[ '2018-10-20 00:00:00', '2018-10-20 11:23:03' ], \
	[ '2018-10-27 00:00:00', '2018-10-27 12:52:11' ], \
	[ '2018-10-28 00:00:00', '2018-10-28 12:57:38' ], \
	[ '2018-10-29 00:00:00', '2018-10-29 12:58:54' ], \
	[ '2018-10-30 00:00:00', '2018-10-30 10:46:52' ], \
	[ '2018-10-31 00:00:00', '2018-10-31 11:38:24' ], \
	[ '2018-11-01 00:00:00', '2018-11-01 13:01:42' ], \
	[ '2018-11-02 00:00:00', '2018-11-02 12:44:53' ], \
	[ '2018-11-03 00:00:00', '2018-11-03 13:16:30' ], \
	[ '2018-11-04 00:00:00', '2018-11-04 13:01:33' ], \
	[ '2018-11-05 00:00:00', '2018-11-05 12:13:37' ], \
	[ '2018-11-06 00:00:00', '2018-11-06 12:36:55' ], \
	[ '2018-11-07 00:00:00', '2018-11-07 12:33:23' ], \
	[ '2018-11-08 00:00:00', '2018-11-08 11:38:06' ], \
	[ '2018-11-09 00:00:00', '2018-11-09 11:36:58' ], \
	[ '2018-11-10 00:00:00', '2018-11-10 12:06:53' ], \
	[ '2018-11-11 00:00:00', '2018-11-11 12:40:48' ], \
	[ '2018-11-12 00:00:00', '2018-11-12 12:04:19' ], \
	[ '2018-11-13 00:00:00', '2018-11-13 12:57:46' ], \
	[ '2018-11-15 00:00:00', '2018-11-15 12:49:57' ], \
	[ '2018-11-16 00:00:00', '2018-11-16 12:40:58' ], \
	[ '2018-11-17 00:00:00', '2018-11-17 12:57:49' ], \
	[ '2018-11-18 00:00:00', '2018-11-18 12:36:10' ], \
	[ '2018-11-19 00:00:00', '2018-11-19 12:37:27' ], \
	[ '2018-11-25 00:00:00', '2018-11-25 13:25:46' ], \
	[ '2018-11-26 00:00:00', '2018-11-26 13:24:49' ], \
	[ '2018-11-28 00:00:00', '2018-11-28 13:23:27' ], \
	[ '2018-11-29 00:00:00', '2018-11-29 12:24:11' ], \
	[ '2018-11-30 00:00:00', '2018-11-30 11:52:02' ], \
	[ '2018-12-03 00:00:00', '2018-12-03 12:49:43' ], \
	[ '2018-12-04 00:00:00', '2018-12-04 13:04:25' ], \
	[ '2018-12-05 00:00:00', '2018-12-05 11:43:13' ], \
	[ '2018-12-06 00:00:00', '2018-12-06 12:42:36' ], \
	[ '2018-12-07 00:00:00', '2018-12-07 10:00:54' ], \
	[ '2018-12-08 00:00:00', '2018-12-08 11:38:05' ], \
	[ '2018-12-09 00:00:00', '2018-12-09 13:11:02' ], \
	[ '2018-12-10 00:00:00', '2018-12-10 11:54:55' ])
for period in range(len(periods)):
	start = periods[period][0]
	end = periods[period][1]

	archiver.scan_archives()

	# NEED TO TAKE THIS FROM THE COMMAND LINE
	pvs_to_retrieve=['25m:guider:axisError:DEC', '25m:guider:axisError:RA', '25m:guider:seeing']
	# pvs_to_retrieve=[ '25m:boss:SP1B2LN2TempRead', '25m:boss:SP1R0LN2TempRead', '25m:boss:SP2B2LN2TempRead', '25m:boss:SP2R0LN2TempRead', '25m:boss:sp1camSecondaryDewarPress', '25m:boss:SP1SecondaryDewarPress', '25m:boss:sp2camSecondaryDewarPress', '25m:boss:SP2SecondaryDewarPress' ]
	# pvs_to_retrieve=[ '25m:boss:sp1camSecondaryDewarPress', '25m:boss:SP1SecondaryDewarPress', '25m:boss:sp2camSecondaryDewarPress', '25m:boss:SP2SecondaryDewarPress' ]
	# pvs_to_retrieve=[ '25m:boss:sp1camSecondaryDewarPress', '25m:boss:sp2camSecondaryDewarPress' ]
	# pvs_to_retrieve=[ '25m:boss:SP1R0CCDTempRead', '25m:boss:SP1B2CCDTempRead', '25m:boss:SP2R0CCDTempRead', '25m:boss:SP2B2CCDTempRead' ]
	# pvs_to_retrieve=[ '25m:boss:tpm_Ndewar_spectro', '25m:boss:tpm_Sdewar_spectro' ]
	# pvs_to_retrieve=[ '25m:boss:SP1SecondaryDewarPress', '25m:boss:SP2SecondaryDewarPress' ]
	# pvs_to_retrieve=[ '25m:guider:axisError:RA', '25m:guider:axisError:DEC']

	for pv in pvs_to_retrieve:
		print "# " + pv
		retrieved_pv = archiver.get(pv, start, end, interpolation='raw',scan_archives=False)
		for i in range(len(retrieved_pv.values)):
			print "%s\t%f" % (retrieved_pv.times[i].strftime('%Y-%m-%d %H:%M:%S.%f'), retrieved_pv.values[i])