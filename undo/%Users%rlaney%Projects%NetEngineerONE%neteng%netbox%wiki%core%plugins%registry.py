Vim�UnDo� ��0Ꮊ��^�)Z�p�U��w��ʨ�{�O�   7   0from django.utils.importlib import import_module                             X;��    _�                           ����                                                                                                                                                                                                                                                                                                                                                v       X;��     �         7      0from django.utils.importlib import import_module5�_�                             ����                                                                                                                                                                                                                                                                                                                                              v       X;��    �   $   &              �   #   %          X    _markdown_extensions.extend(getattr(PluginClass, 'markdown_extensions', []))        �      !              �                    �                    �                    5�_�                    7        ����                                                                                                                                                                                                                                                                                                                                                             X;��     �   6   8              return _settings_forms5�_�                     7       ����                                                                                                                                                                                                                                                                                                                                                             X;��     �       8       %   H# -*- coding: utf-8 -*- from django.utils.importlib import import_module       M_cache = {} _settings_forms = [] _markdown_extensions = [] _article_tabs = []   _sidebar = []       Odef register(PluginClass): """ Register a plugin class. This function will call   Kback your plugin's constructor.  """ if PluginClass in _cache.keys(): raise   CException("Plugin class already registered") plugin = PluginClass()   _cache[PluginClass] = plugin          B    settings_form = getattr(PluginClass, 'settings_form', None) if   H    settings_form: if isinstance(settings_form, basestring): klassname =   -    settings_form.split(".")[-1] modulename =   9    ".".join(settings_form.split(".")[:-1]) form_module =   M    import_module(modulename) settings_form = getattr(form_module, klassname)   )    _settings_forms.append(settings_form)                 N    if getattr(PluginClass, 'article_tab', None): _article_tabs.append(plugin)          E    if getattr(PluginClass, 'sidebar', None): _sidebar.append(plugin)       X    _markdown_extensions.extend(getattr(PluginClass, 'markdown_extensions', []))                  Mdef get_plugins(): """Get loaded plugins - do not call before all plugins are   loaded.""" return _cache       Idef get_markdown_extensions(): """Get all markdown extension classes from   &plugins""" return _markdown_extensions       Kdef get_article_tabs(): """Get all article tab dictionaries from plugins"""   return _article_tabs       Gdef get_sidebar(): """Returns plugin classes that should connect to the   sidebar""" return _sidebar       0def get_settings_forms(): return _settings_forms5��