class MessageDefect:
    """Base class for a message defect."""

    def __init__(self, line=None):
        self.line = line

class NoBoundaryInMultipartDefect(MessageDefect):
    """A message claimed to be a multipart but had no boundary parameter."""

class StartBoundaryNotFoundDefect(MessageDefect):
    """The claimed start boundary was never found."""

class FirstHeaderLineIsContinuationDefect(MessageDefect):
    """A message had a continuation line as its first header line."""

class MisplacedEnvelopeHeaderDefect(MessageDefect):
    """A 'Unix-from' header was found in the middle of a header block."""

class MalformedHeaderDefect(MessageDefect):
    """Found a header that was missing a colon, or was otherwise malformed."""

class MultipartInvariantViolationDefect(MessageDefect):
    """A message claimed to be a multipart but no subparts were found."""


a = MultipartInvariantViolationDefect()

print help(a)
