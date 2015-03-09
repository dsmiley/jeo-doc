from docutils import nodes

def make_link_node(rawtext, ref, app):
  try:
    base_url = app.config.jeo_javadoc_url
  except AttributeError, err:
    raise ValueError('jeo_javadoc_url value is not set (%s) in conf.py' % str(err))

  if '#' in ref:
    class_name, member_name = ref.split('#')
  else:
    class_name, member_name = ref, None

  class_path = class_name.split('.')
  link_url = '%s/org/jeo/%s.html' % (base_url, '/'.join(class_path))
  if member_name is not None:
    link_url += '#' + member_name

  link_text = class_path[-1]
  if member_name is not None:
    link_text += '.' + member_name

  return nodes.reference(rawtext, link_text, refuri=link_url)

def jeoref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
  app = inliner.document.settings.env.app
  link = make_link_node(rawtext, text, app)
  return [link], []

def setup(app):
  app.add_role('jeoref', jeoref_role)
  app.add_config_value('jeo_javadoc_url', None, 'env')