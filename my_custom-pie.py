import bpy

bl_info = {
    "name": "Hotkey 'Alt + W' Custom Pie Menu",
    "description": "This is a custom pie menu activated with Alt + W",
    "author": "Fernando Felix",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location": "3D View -> Alt + W",
    "category": "Custom Pie Menu"
}

# Define the Custom Pie Menu class
class CustomPieMenu(bpy.types.Menu):
    bl_label = "Custom Pie Menu"
    bl_idname = "VIEW3D_MT_custom_pie_menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        # Add cube operator
        pie.operator("mesh.primitive_cube_add", text="Add Cube", icon='MESH_CUBE')
    
        # Add empty object operator
        pie.operator("object.empty_add", text="Add Empty", icon='EMPTY_AXIS').type = 'PLAIN_AXES'

        # Check if we are in mesh edit mode before showing the merge operator
        if context.active_object and context.active_object.mode == 'EDIT' and context.active_object.type == 'MESH':
            pie.operator("mesh.merge", text="Merge at Last", icon='SNAP_VERTEX').type = 'LAST'

# Register function
def register():
    bpy.utils.register_class(CustomPieMenu)
    wm = bpy.context.window_manager
    # Use the appropriate keymap for the 3D View
    km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('wm.call_menu_pie', 'W', 'PRESS', alt=True)
    kmi.properties.name = "VIEW3D_MT_custom_pie_menu"

# Unregister function
def unregister():
    bpy.utils.unregister_class(CustomPieMenu)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps['3D View']
    for kmi in km.keymap_items:
        if kmi.properties.name == "VIEW3D_MT_custom_pie_menu":
            km.keymap_items.remove(kmi)

# Register the addon when the script is executed directly
if __name__ == "__main__":
    register()
