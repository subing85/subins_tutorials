from studio_usd_pipe.api import studioPublish
reload(studioPublish)
pub=studioPublish.Publish(pipe='assets',subfield='model')
pub.python_pack('ssssssssssssssssssss')
message = pub.python_pack(
    'subin',
    description=None,source_maya='/venture/shows/batman/batman_0.0.3.mb',subfield='model',caption='batman',tag='character',version='3.0.0',type='non-interactive',thumbnail=None)
