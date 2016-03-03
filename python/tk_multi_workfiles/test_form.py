import sgtk
from sgtk.platform.qt import QtCore, QtGui

from .file_model import FileModel

from .ui.test_form import Ui_TestForm

#shotgun_view = sgtk.platform.import_framework("tk-framework-qtwidgets", "shotgun_view")
#WidgetDelegate = shotgun_view.WidgetDelegate
from .tmp_delegate import WidgetDelegate


from .file_tile import FileTile
from .group_header_widget import GroupHeaderWidget

from .grouped_list_view import GroupListViewItemDelegate

from .file_list_form import TestItemDelegate        
#
#class TestItemDelegate(GroupListViewItemDelegate):
#
#    def __init__(self, view):
#        GroupListViewItemDelegate.__init__(self, view)
#
#    def _create_group_widget(self, parent):
#        """
#        """
#        return GroupHeaderWidget(parent)
#    
#    def _create_item_widget(self, parent):
#        """
#        """
#        return FileTile(parent)
#
#    def _setup_widget(self, widget, model_index, style_options):
#        """
#        """
#        if isinstance(widget, GroupHeaderWidget):
#            # update group widget:
#            widget.label = model_index.data()
#        elif isinstance(widget, FileTile):
#            # update item widget:
#            widget.title = model_index.data()
#            widget.selected = (style_options.state & QtGui.QStyle.State_Selected) == QtGui.QStyle.State_Selected 
#
#    def _on_before_paint(self, widget, model_index, style_options):
#        """
#        """
#        self._setup_widget(widget, model_index, style_options) 
#
#    def _on_before_selection(self, widget, model_index, style_options):
#        """
#        """
#        self._setup_widget(widget, model_index, style_options)
#        
#    def setModelData(self, editor, model, model_index):
#        pass

class TestModel(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        QtGui.QStandardItemModel.__init__(self, parent)
        
        
        

class TestForm(QtGui.QWidget):
    """
    """
    
    def __init__(self, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
        
        # set up the UI
        self._ui = Ui_TestForm()
        self._ui.setupUi(self)
        
        # set up the model:
        self._model = self._init_model()
        
        item_delegate = TestItemDelegate(self._ui.listView)
        self._ui.listView.setItemDelegate(item_delegate)    
        
        item_delegate = TestItemDelegate(self._ui.treeView)
        self._ui.treeView.setItemDelegate(item_delegate)
        
        item_delegate = TestItemDelegate(self._ui.customView)
        self._ui.customView.setItemDelegate(item_delegate)
        
        self._ui.listView.setModel(self._model)        
        self._ui.treeView.setModel(self._model)
        self._ui.customView.setModel(self._model)
        
        for row in range(self._model.rowCount()):
            idx = self._model.index(row,0)
            self._expand_recursive(self._ui.treeView, idx)
            #self._expand_recursive(self._ui.customView, idx)
        
    def _init_model(self):
        model = FileModel(None, self)


        # populate the model with some dummy data:
        class _Details(object):
            def __init__(self, item, entity=None, is_leaf=False):
                """
                """
                self.item = item
                self.entity = entity
                self.task = None
                self.step = None
                self.is_leaf = is_leaf
                self.child_entities = []
                self.name = item.text() if item else ""
                
            def __repr__(self):
                return ("%s\n"
                        " - Entity: %s\n"
                        " - Task: %s\n"
                        " - Step: %s\n"
                        " - Is leaf: %s\n%s"
                        % (self.name, self.entity, self.task, self.step, self.is_leaf, self.children))
                
        class _Item(object):
            def __init__(self, name):
                self._name = name

            def text(self):
                return self._name
        
        variation = 2
        details = []    
        if variation == 0:
            details = _Details(_Item("Sequence 01"), {"type":"Sequence", "id":123})
            details.children.append(_Details(_Item("Shot 01"), {"type":"Shot", "id":123}))
            details.children.append(_Details(_Item("Shot 02"), {"type":"Shot", "id":123}))
            details.children.append(_Details(_Item("Shot 03"), {"type":"Shot", "id":123}))
        elif variation == 1:
            details = _Details(_Item("Sequence 02"), {"type":"Sequence", "id":123})
            details.children.append(_Details(_Item("Shot A"), {"type":"Shot", "id":123}))
            details.children.append(_Details(_Item("Shot B"), {"type":"Shot", "id":123}))
            details.children.append(_Details(_Item("Shot C"), {"type":"Shot", "id":123}))
        elif variation == 2:
            details.append(_Details(_Item("Shot 01"), {"type":"Shot", "id":123}))
            details.append(_Details(_Item("Light - Lighting"), {"type":"Task", "id":123}, True))
            details.append(_Details(_Item("Mod - Modelling"), {"type":"Task", "id":123}, True))
            details.append(_Details(_Item("Anm - Animation"), {"type":"Task", "id":123}, True))
            details.append(_Details(_Item("Anm - More Animation"), {"type":"Task", "id":123}, True))


        
        model.refresh_files(details)
        

        
        """
        model = TestModel(self)
        
        items = {
            "Headmasters":["Brainstorm", "Chromedome", "Hardhead"],
            "Targetmasters":["Kup", "Hot-rod", "Blur"],
            "Primes":["Optimus", "Omega", "Nova"],
            "Lost Light":["Rodimus", "Fort Max"]
        }
        
        for name, group in items.iteritems():
            header_item = QtGui.QStandardItem(name)
            model.appendRow(header_item)
            
            for tf in group:
                header_item.appendRow(QtGui.QStandardItem(tf))
        """
        
        return model
        
    def _expand_recursive(self, view, idx, expand=True):
        
        model = idx.model()
        
        if not model.hasChildren(idx):
            return
        
        view.setExpanded(idx, expand)
        
        for row in range(model.rowCount(idx)):
            child_idx = idx.child(row, 0)
            self._expand_recursive(view, child_idx, expand)
        
        
        