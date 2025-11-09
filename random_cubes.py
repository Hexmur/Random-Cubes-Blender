bl_info = {
    "name": "Random Cubes",
    "author": "Hexmur (Mauro Alizzi)",
    "version": (1,0),
    "blender": (4,5,3),
    "description": "Adds randomly placed cubes",
}

import bpy
from random import randint
from bpy.types import (Panel, Operator)

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "random.1"
    bl_label = "Simple Random Operator"

    def execute(self, context):
        for i in range(100):
            random_scale = randint(-10,10)
            x = randint(-40, 40)
            y = randint(-40, 40)
            z = randint(-40, 40)
            bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(random_scale, random_scale, random_scale))
    
        return {'FINISHED'}

class CustomPanel(bpy.types.Panel):
    bl_label = "Random Panel"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "objectmode"
    bl_category = "Random Cubes"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='CUBE')


from bpy.utils import register_class, unregister_class

_classes = [
    ButtonOperator,
    CustomPanel
]

def register():
    for cls in _classes:
        register_class(cls)
    
def unregister():
    for cls in _classes:
        unregister_class(cls)
        

if __name__ == "__main__":
    register()

