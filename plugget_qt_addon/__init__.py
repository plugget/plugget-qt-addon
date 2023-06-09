bl_info = {
    "name": "Plugget Qt Package Manager TEST",
    "description": "manage Plugget packages",
    "author": "Hannes D TEST",
    "version": (0, 0, 1),
    "blender": (2, 91, 0),
    "location": "Window/Plugget Qt Manager",
    "category": "Development",
}


import bpy


class OpenPluggetQt(bpy.types.Operator):
    """Open the Plugget Qt Manager window"""
    bl_idname = "plugget.show_qt_manager"
    bl_label = "Plugget Qt Manager"
    self.widget = None

    def execute(self, context):
        import plugget_qt
        self.widget = plugget_qt.show()  # store ref to prevent garbage collect
        return {'RUNNING_MODAL'}  # MODAL keeps operator alive to prevent instant garbage collection


def menu_func(self, context):
    # Add the new menu item to the "Window" menu
    self.layout.operator(OpenPluggetQt.bl_idname, icon="MESH_CUBE")


def register():
    bpy.utils.register_class(OpenPluggetQt)
    bpy.types.TOPBAR_MT_window.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OpenPluggetQt)
    bpy.types.TOPBAR_MT_window.remove(menu_func)
