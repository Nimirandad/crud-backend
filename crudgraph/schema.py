import graphene
import compania.schema

class Query(compania.schema.Query, graphene.ObjectType):
    pass

class Mutation(compania.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)