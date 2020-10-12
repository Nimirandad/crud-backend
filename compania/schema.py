import graphene
from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id
from .models import *


class CiudadNode(DjangoObjectType):
    class Meta:
        model = Ciudad
        filter_fields = ['nombre_ciudad']
        interfaces = (relay.Node,)


class TituloNode(DjangoObjectType):
    class Meta:
        model = Titulo
        filter_fields = ['nombre_titulo']
        interfaces = (relay.Node,)


class EmpleadoNode(DjangoObjectType):
    class Meta:
        model = Empleado
        filter_fields = [
            'nombre_empleado', 'ciudad_empleado__nombre_ciudad', 'titulo_empleado__nombre_titulo']
        interfaces = (relay.Node,)


# Mutations para Titulo
class CrearTitulo(relay.ClientIDMutation):
    titulo = graphene.Field(TituloNode)

    class Input:
        nombre_titulo = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        titulo = Titulo(nombre_titulo=input.get('nombre_titulo'))
        titulo.save()

        return CrearTitulo(titulo=titulo)


class ActualizarTitulo(relay.ClientIDMutation):
    titulo = graphene.Field(TituloNode)

    class Input:
        id = graphene.String()
        nombre_titulo = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        titulo = Titulo.objects.get(pk=from_global_id(input.get('id'))[1])
        titulo.nombre_titulo = input.get('nombre_titulo')
        titulo.save()

        return ActualizarTitulo(titulo=titulo)


class EliminarTitulo(relay.ClientIDMutation):
    titulo = graphene.Field(TituloNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        titulo = Titulo.objects.get(pk=from_global_id(input.get('id'))[1])
        titulo.delete()

        return EliminarTitulo(titulo=titulo)


# Mutations para Ciudad
class CrearCiudad(relay.ClientIDMutation):
    ciudad = graphene.Field(CiudadNode)

    class Input:
        nombre_ciudad = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        ciudad = Ciudad(nombre_ciudad=input.get('nombre_ciudad'))
        ciudad.save()

        return CrearCiudad(ciudad=ciudad)


class ActualizarCiudad(relay.ClientIDMutation):
    ciudad = graphene.Field(CiudadNode)

    class Input:
        id = graphene.String()
        nombre_ciudad = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        ciudad = Ciudad.objects.get(pk=from_global_id(input.get('id'))[1])
        ciudad.nombre_ciudad = input.get('nombre_ciudad')
        ciudad.save()

        return ActualizarCiudad(ciudad=ciudad)


class EliminarCiudad(relay.ClientIDMutation):
    empleado = graphene.Field(CiudadNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        ciudad = Ciudad.objects.get(pk=from_global_id(input.get('id'))[1])
        ciudad.delete()

        return EliminarCiudad(ciudad=ciudad)

# Mutations para Empleado
class CrearEmpleado(relay.ClientIDMutation):
    empleado = graphene.Field(EmpleadoNode)

    class Input:
        nombre_empleado = graphene.String()
        ciudad_empleado = graphene.String()
        titulo_empleado = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        empleado = Empleado(
            nombre_empleado=input.get('nombre_empleado'),
            ciudad_empleado=Ciudad.objects.get(
                nombre_ciudad=input.get('ciudad_empleado')),
            titulo_empleado=Titulo.objects.get(
                nombre_titulo=input.get('titulo_empleado'))
        )
        empleado.save()

        return CrearEmpleado(empleado=empleado)


class ActualizarEmpleado(relay.ClientIDMutation):
    empleado = graphene.Field(EmpleadoNode)

    class Input:
        id = graphene.String()
        nombre_empleado = graphene.String()
        ciudad_empleado = graphene.String()
        titulo_empleado = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        empleado = Empleado.objects.get(pk=from_global_id(input.get('id'))[1])
        empleado.nombre_empleado = input.get('nombre_empleado')
        #empleado.ciudad_empleado = Ciudad.objects.get(nombre_ciudad=input.get('ciudad_empleado'))
        #empleado.titulo_empleado = Titulo.objects.get(nombre_titulo=input.get('titulo_empleado'))
        empleado.save()

        return ActualizarEmpleado(empleado=empleado)


class EliminarEmpleado(relay.ClientIDMutation):
    empleado = graphene.Field(EmpleadoNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        empleado = Empleado.objects.get(pk=from_global_id(input.get('id'))[1])
        empleado.delete()

        return EliminarEmpleado(empleado=empleado)
        

# Metodos GraphQL
class Query(ObjectType):
    ciudad = relay.Node.Field(CiudadNode)
    all_ciudades = DjangoFilterConnectionField(CiudadNode)

    titulo = relay.Node.Field(TituloNode)
    all_titulos = DjangoFilterConnectionField(TituloNode)

    empleado = relay.Node.Field(EmpleadoNode)
    all_empleados = DjangoFilterConnectionField(EmpleadoNode)


class Mutation(AbstractType):
    crear_titulo = CrearTitulo.Field()
    crear_ciudad = CrearCiudad.Field()
    crear_empleado = CrearEmpleado.Field()
    update_titulo = ActualizarTitulo.Field()
    update_ciudad = ActualizarCiudad.Field()
    update_empleado = ActualizarEmpleado.Field()
    delete_titulo = EliminarTitulo.Field()
    delete_ciudad = EliminarCiudad.Field()
    delete_empleado = EliminarEmpleado.Field()
