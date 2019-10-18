import alembic


class ArchiveInfo(object):
    def __init__(self):
        super(ArchiveInfo, self).__init__()

        self._fps = 24.0
        self._start_frame = 1001
        self._end_frame = 1001
        self.time_per_cycle = 1 / self.fps
        self.start_time = self.start_frame / self.fps
        self.ts = alembic.AbcCoreAbstract.TimeSampling(self.time_per_cycle, self.start_time)

    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, fps):
        self._fps = fps

    @property
    def start_frame(self):
        return self._start_frame

    @start_frame.setter
    def start_frame(self, start_frame):
        self._start_frame = start_frame

    @property
    def end_frame(self):
        return self._end_frame

    @end_frame.setter
    def end_frame(self, end_frame):
        self._end_frame = end_frame

