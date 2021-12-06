# Auto generated from sio-model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-03T14:16:13
# Schema: semanticscience-model
#
# id: https://semanticscience.org
# description: The Semanticscience Integrated Ontology (SIO) provides a simple, integrated ontology of types and
#              relations for rich description of objects, processes and their attributes.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CITO = CurieNamespace('cito', 'http://purl.org/spar/cito/')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROTEGE = CurieNamespace('protege', 'http://protege.stanford.edu/plugins/owl/protege#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/')
SKOSVOCAB = CurieNamespace('skosvocab', 'http://www.w3.org/2004/02/skos/core#')
VANN = CurieNamespace('vann', 'http://purl.org/vocab/vann/')
XML = CurieNamespace('xml', 'http://www.w3.org/XML/1998/namespace')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SIO


# Types

# Class references



@dataclass
class Entity(YAMLRoot):
    """
    Every thing is an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Entity
    class_class_curie: ClassVar[str] = "sio:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = SIO.Entity

    hasCreator: Optional[Union[dict, "Entity"]] = None
    hasAttribute: Optional[Union[dict, "Entity"]] = None
    satisfies: Optional[Union[dict, Description]] = None
    isRelatedTo: Optional[Union[dict, "Entity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasCreator is not None and not isinstance(self.hasCreator, Entity):
            self.hasCreator = Entity(**as_dict(self.hasCreator))

        if self.hasAttribute is not None and not isinstance(self.hasAttribute, Entity):
            self.hasAttribute = Entity(**as_dict(self.hasAttribute))

        if self.satisfies is not None and not isinstance(self.satisfies, Description):
            self.satisfies = Description(**as_dict(self.satisfies))

        if self.isRelatedTo is not None and not isinstance(self.isRelatedTo, Entity):
            self.isRelatedTo = Entity(**as_dict(self.isRelatedTo))

        super().__post_init__(**kwargs)


class Attribute(Entity):
    """
    An attribute is a characteristic of some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Attribute
    class_class_curie: ClassVar[str] = "sio:Attribute"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = SIO.Attribute


@dataclass
class Object(Entity):
    """
    An object is an entity that is wholly identifiable at any instant of time during which it exists.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Object
    class_class_curie: ClassVar[str] = "sio:Object"
    class_name: ClassVar[str] = "Object"
    class_model_uri: ClassVar[URIRef] = SIO.Object

    derivesInto: Optional[Union[dict, "Object"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.derivesInto is not None and not isinstance(self.derivesInto, Object):
            self.derivesInto = Object(**as_dict(self.derivesInto))

        super().__post_init__(**kwargs)


class InformationContentEntity(Object):
    """
    information content entity is an object that requires some background knowledge or procedure to correctly
    interpret.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationContentEntity
    class_class_curie: ClassVar[str] = "sio:InformationContentEntity"
    class_name: ClassVar[str] = "InformationContentEntity"
    class_model_uri: ClassVar[URIRef] = SIO.InformationContentEntity


class ComputationalEntity(InformationContentEntity):
    """
    A computational entity is an information content entity operated on using some computational system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ComputationalEntity
    class_class_curie: ClassVar[str] = "sio:ComputationalEntity"
    class_name: ClassVar[str] = "ComputationalEntity"
    class_model_uri: ClassVar[URIRef] = SIO.ComputationalEntity


class Cellinformational(ComputationalEntity):
    """
    The minimal unit of a cellular automaton that can change state and has an associated behavior.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Cellinformational
    class_class_curie: ClassVar[str] = "sio:Cellinformational"
    class_name: ClassVar[str] = "Cellinformational"
    class_model_uri: ClassVar[URIRef] = SIO.Cellinformational


class Column(ComputationalEntity):
    """
    A column is a vertical sequence of cells in a cellular automata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Column
    class_class_curie: ClassVar[str] = "sio:Column"
    class_name: ClassVar[str] = "Column"
    class_model_uri: ClassVar[URIRef] = SIO.Column


class DataItem(ComputationalEntity):
    """
    A data item consists of information that has been collected/generated towards some purpose.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataItem
    class_class_curie: ClassVar[str] = "sio:DataItem"
    class_name: ClassVar[str] = "DataItem"
    class_model_uri: ClassVar[URIRef] = SIO.DataItem


class Database(ComputationalEntity):
    """
    A database is a set of tables.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Database
    class_class_curie: ClassVar[str] = "sio:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = SIO.Database


class DatabaseColumn(Column):
    """
    A database collumn is a column in a database table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DatabaseColumn
    class_class_curie: ClassVar[str] = "sio:DatabaseColumn"
    class_name: ClassVar[str] = "DatabaseColumn"
    class_model_uri: ClassVar[URIRef] = SIO.DatabaseColumn


class DatabaseEntry(ComputationalEntity):
    """
    A database entry is a single, implicitly structured data item in a table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DatabaseEntry
    class_class_curie: ClassVar[str] = "sio:DatabaseEntry"
    class_name: ClassVar[str] = "DatabaseEntry"
    class_model_uri: ClassVar[URIRef] = SIO.DatabaseEntry


class DatabaseKey(ComputationalEntity):
    """
    A database key is an informational entity whose value is constructed from one or more database columns.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DatabaseKey
    class_class_curie: ClassVar[str] = "sio:DatabaseKey"
    class_name: ClassVar[str] = "DatabaseKey"
    class_model_uri: ClassVar[URIRef] = SIO.DatabaseKey


class DatabaseTable(ComputationalEntity):
    """
    A database table is a set of named columns with zero or more rows composed of cells that contain column values and
    is part of a database.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DatabaseTable
    class_class_curie: ClassVar[str] = "sio:DatabaseTable"
    class_name: ClassVar[str] = "DatabaseTable"
    class_model_uri: ClassVar[URIRef] = SIO.DatabaseTable


@dataclass
class Dataset(DataItem):
    """
    A dataset is a data item that is a collection of data items.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Dataset
    class_class_curie: ClassVar[str] = "sio:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = SIO.Dataset

    hasDataItem: Optional[Union[dict, "Entity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasDataItem is not None and not isinstance(self.hasDataItem, Entity):
            self.hasDataItem = Entity(**as_dict(self.hasDataItem))

        super().__post_init__(**kwargs)


class ForeignDatabaseKey(DatabaseKey):
    """
    A foreign database key is a database key that refers to a key in some table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ForeignDatabaseKey
    class_class_curie: ClassVar[str] = "sio:ForeignDatabaseKey"
    class_name: ClassVar[str] = "ForeignDatabaseKey"
    class_model_uri: ClassVar[URIRef] = SIO.ForeignDatabaseKey


class GeometricEntity(InformationContentEntity):
    """
    A geometric entity is an information content entity that pertains to the structure and topology of a space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeometricEntity
    class_class_curie: ClassVar[str] = "sio:GeometricEntity"
    class_name: ClassVar[str] = "GeometricEntity"
    class_model_uri: ClassVar[URIRef] = SIO.GeometricEntity


class Curve(GeometricEntity):
    """
    A curve is a geometric entity that may be located in n-dimensional spatial region whose extension may be
    n-dimensional, is composed of at least two fully connected points and does not intersect itself.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Curve
    class_class_curie: ClassVar[str] = "sio:Curve"
    class_name: ClassVar[str] = "Curve"
    class_model_uri: ClassVar[URIRef] = SIO.Curve


class Arc(Curve):
    """
    an arc is a closed segment of a differentiable curve.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Arc
    class_class_curie: ClassVar[str] = "sio:Arc"
    class_name: ClassVar[str] = "Arc"
    class_model_uri: ClassVar[URIRef] = SIO.Arc


class CurveSegment(Curve):
    """
    A curve segment is a part of a curve that consists of at least three points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CurveSegment
    class_class_curie: ClassVar[str] = "sio:CurveSegment"
    class_name: ClassVar[str] = "CurveSegment"
    class_model_uri: ClassVar[URIRef] = SIO.CurveSegment


@dataclass
class LanguageEntity(InformationContentEntity):
    """
    A language entity implements some language specification for the visual interpretation and is part of some
    document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LanguageEntity
    class_class_curie: ClassVar[str] = "sio:LanguageEntity"
    class_name: ClassVar[str] = "LanguageEntity"
    class_model_uri: ClassVar[URIRef] = SIO.LanguageEntity

    isAnnotationOf: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isAnnotationOf is not None and not isinstance(self.isAnnotationOf, Entity):
            self.isAnnotationOf = Entity(**as_dict(self.isAnnotationOf))

        super().__post_init__(**kwargs)


class Character(LanguageEntity):
    """
    A character is a language symbol used to construct words.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Character
    class_class_curie: ClassVar[str] = "sio:Character"
    class_name: ClassVar[str] = "Character"
    class_model_uri: ClassVar[URIRef] = SIO.Character


class Description(LanguageEntity):
    """
    A description is language entity in which elements of a language (formal or natural) are used to characterize an
    entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Description
    class_class_curie: ClassVar[str] = "sio:Description"
    class_name: ClassVar[str] = "Description"
    class_model_uri: ClassVar[URIRef] = SIO.Description


class Annotation(Description):
    """
    An annotation is a written explanatory or critical description, or other in-context information (e.g., pattern,
    motif, link), that has been associated with data or other types of information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Annotation
    class_class_curie: ClassVar[str] = "sio:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = SIO.Annotation


class Answer(Description):
    """
    An answer is a reply to a question.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Answer
    class_class_curie: ClassVar[str] = "sio:Answer"
    class_name: ClassVar[str] = "Answer"
    class_model_uri: ClassVar[URIRef] = SIO.Answer


class Definition(Description):
    """
    A definition is a description that succintly characterizes an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Definition
    class_class_curie: ClassVar[str] = "sio:Definition"
    class_name: ClassVar[str] = "Definition"
    class_model_uri: ClassVar[URIRef] = SIO.Definition


class History(Description):
    """
    history is a sequence of past events.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.History
    class_class_curie: ClassVar[str] = "sio:History"
    class_name: ClassVar[str] = "History"
    class_model_uri: ClassVar[URIRef] = SIO.History


class EvolutionaryLineage(History):
    """
    evolutionary lineage is a sequence of species, that form a line of descent, each new species the direct result of
    speciation from an immediate ancestral species.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EvolutionaryLineage
    class_class_curie: ClassVar[str] = "sio:EvolutionaryLineage"
    class_name: ClassVar[str] = "EvolutionaryLineage"
    class_model_uri: ClassVar[URIRef] = SIO.EvolutionaryLineage


class FamilyHistory(History):
    """
    family history is the systematic narrative and research of past events relating to a specific family, or specific
    families.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FamilyHistory
    class_class_curie: ClassVar[str] = "sio:FamilyHistory"
    class_name: ClassVar[str] = "FamilyHistory"
    class_model_uri: ClassVar[URIRef] = SIO.FamilyHistory


class Language(LanguageEntity):
    """
    Language is a language entity which is the result of encoding and decoding information through systematic creation
    and usage of systems of symbols, each pairing a specific sign with an intended meaning, established through social
    conventions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Language
    class_class_curie: ClassVar[str] = "sio:Language"
    class_name: ClassVar[str] = "Language"
    class_model_uri: ClassVar[URIRef] = SIO.Language


class Line(Curve):
    """
    A line is curve that extends in a single dimension (e.g. straight line; exhibits no curvature), and is composed of
    at least two fully connected points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Line
    class_class_curie: ClassVar[str] = "sio:Line"
    class_name: ClassVar[str] = "Line"
    class_model_uri: ClassVar[URIRef] = SIO.Line


class Edge(Line):
    """
    an edge is a line connecting two graph vertices.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Edge
    class_class_curie: ClassVar[str] = "sio:Edge"
    class_name: ClassVar[str] = "Edge"
    class_model_uri: ClassVar[URIRef] = SIO.Edge


class InfiniteLine(Line):
    """
    An infinite line is a line that extends outwards in both directions of a single dimensional and is not bounded by
    terminal points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InfiniteLine
    class_class_curie: ClassVar[str] = "sio:InfiniteLine"
    class_name: ClassVar[str] = "InfiniteLine"
    class_model_uri: ClassVar[URIRef] = SIO.InfiniteLine


class LineSegment(Line):
    """
    A line segment is a line and a part of a curve that is (inclusively) bounded by two terminal points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LineSegment
    class_class_curie: ClassVar[str] = "sio:LineSegment"
    class_name: ClassVar[str] = "LineSegment"
    class_model_uri: ClassVar[URIRef] = SIO.LineSegment


class DirectedLineSegment(LineSegment):
    """
    A directed line segment is a line segment that is contained by an ordered pair
    of endpoints (a start point and an endpoint).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DirectedLineSegment
    class_class_curie: ClassVar[str] = "sio:DirectedLineSegment"
    class_name: ClassVar[str] = "DirectedLineSegment"
    class_model_uri: ClassVar[URIRef] = SIO.DirectedLineSegment


class ArrowedLineSegment(DirectedLineSegment):
    """
    An arrowed line is a directed line segment in which one or both endpoints is tangentially part of a triangle that
    bisects the line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ArrowedLineSegment
    class_class_curie: ClassVar[str] = "sio:ArrowedLineSegment"
    class_name: ClassVar[str] = "ArrowedLineSegment"
    class_model_uri: ClassVar[URIRef] = SIO.ArrowedLineSegment


class Axis(DirectedLineSegment):
    """
    An axis is a line segment that is part of a statistical graph in which the
    position along the line corresponds to a numeric or categorical value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Axis
    class_class_curie: ClassVar[str] = "sio:Axis"
    class_name: ClassVar[str] = "Axis"
    class_model_uri: ClassVar[URIRef] = SIO.Axis


class CategoryAxis(Axis):
    """
    A category axis is an axis in which the position along the line is partioned into categories.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CategoryAxis
    class_class_curie: ClassVar[str] = "sio:CategoryAxis"
    class_name: ClassVar[str] = "CategoryAxis"
    class_model_uri: ClassVar[URIRef] = SIO.CategoryAxis


class DoubleArrowedLineSegment(ArrowedLineSegment):
    """
    A double arrowed line is an arrowed line in which both terminal points are tangentially part of different
    triangles that bisect the line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DoubleArrowedLineSegment
    class_class_curie: ClassVar[str] = "sio:DoubleArrowedLineSegment"
    class_name: ClassVar[str] = "DoubleArrowedLineSegment"
    class_model_uri: ClassVar[URIRef] = SIO.DoubleArrowedLineSegment


class MaterialEntity(Object):
    """
    A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has
    mass.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaterialEntity
    class_class_curie: ClassVar[str] = "sio:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = SIO.MaterialEntity


class ChemicalEntity(MaterialEntity):
    """
    A chemical entity is a material entity that pertains to chemistry.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalEntity
    class_class_curie: ClassVar[str] = "sio:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalEntity


@dataclass
class Atom(ChemicalEntity):
    """
    An atom is composed of a core of protons and/or neutrons which may be surrounded by a cloud of electrons.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Atom
    class_class_curie: ClassVar[str] = "sio:Atom"
    class_name: ClassVar[str] = "Atom"
    class_model_uri: ClassVar[URIRef] = SIO.Atom

    isCovalentlyConnectedTotransitive: Optional[Union[dict, "Atom"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isCovalentlyConnectedTotransitive is not None and not isinstance(self.isCovalentlyConnectedTotransitive, Atom):
            self.isCovalentlyConnectedTotransitive = Atom(**as_dict(self.isCovalentlyConnectedTotransitive))

        super().__post_init__(**kwargs)


class ActiniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ActiniumAtom
    class_class_curie: ClassVar[str] = "sio:ActiniumAtom"
    class_name: ClassVar[str] = "ActiniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ActiniumAtom


class AluminiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AluminiumAtom
    class_class_curie: ClassVar[str] = "sio:AluminiumAtom"
    class_name: ClassVar[str] = "AluminiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.AluminiumAtom


class AmericiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AmericiumAtom
    class_class_curie: ClassVar[str] = "sio:AmericiumAtom"
    class_name: ClassVar[str] = "AmericiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.AmericiumAtom


class AntimonyAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AntimonyAtom
    class_class_curie: ClassVar[str] = "sio:AntimonyAtom"
    class_name: ClassVar[str] = "AntimonyAtom"
    class_model_uri: ClassVar[URIRef] = SIO.AntimonyAtom


class ArgonAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ArgonAtom
    class_class_curie: ClassVar[str] = "sio:ArgonAtom"
    class_name: ClassVar[str] = "ArgonAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ArgonAtom


class ArsenicAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ArsenicAtom
    class_class_curie: ClassVar[str] = "sio:ArsenicAtom"
    class_name: ClassVar[str] = "ArsenicAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ArsenicAtom


class AstatineAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AstatineAtom
    class_class_curie: ClassVar[str] = "sio:AstatineAtom"
    class_name: ClassVar[str] = "AstatineAtom"
    class_model_uri: ClassVar[URIRef] = SIO.AstatineAtom


class BariumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BariumAtom
    class_class_curie: ClassVar[str] = "sio:BariumAtom"
    class_name: ClassVar[str] = "BariumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.BariumAtom


class BerkeliumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BerkeliumAtom
    class_class_curie: ClassVar[str] = "sio:BerkeliumAtom"
    class_name: ClassVar[str] = "BerkeliumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.BerkeliumAtom


class BerylliumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BerylliumAtom
    class_class_curie: ClassVar[str] = "sio:BerylliumAtom"
    class_name: ClassVar[str] = "BerylliumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.BerylliumAtom


class BismuthAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BismuthAtom
    class_class_curie: ClassVar[str] = "sio:BismuthAtom"
    class_name: ClassVar[str] = "BismuthAtom"
    class_model_uri: ClassVar[URIRef] = SIO.BismuthAtom


class BohriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BohriumAtom
    class_class_curie: ClassVar[str] = "sio:BohriumAtom"
    class_name: ClassVar[str] = "BohriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.BohriumAtom


class BoronAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BoronAtom
    class_class_curie: ClassVar[str] = "sio:BoronAtom"
    class_name: ClassVar[str] = "BoronAtom"
    class_model_uri: ClassVar[URIRef] = SIO.BoronAtom


class BromineAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BromineAtom
    class_class_curie: ClassVar[str] = "sio:BromineAtom"
    class_name: ClassVar[str] = "BromineAtom"
    class_model_uri: ClassVar[URIRef] = SIO.BromineAtom


class CadmiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CadmiumAtom
    class_class_curie: ClassVar[str] = "sio:CadmiumAtom"
    class_name: ClassVar[str] = "CadmiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CadmiumAtom


class CaesiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CaesiumAtom
    class_class_curie: ClassVar[str] = "sio:CaesiumAtom"
    class_name: ClassVar[str] = "CaesiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CaesiumAtom


class CalciumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CalciumAtom
    class_class_curie: ClassVar[str] = "sio:CalciumAtom"
    class_name: ClassVar[str] = "CalciumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CalciumAtom


class CaliforniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CaliforniumAtom
    class_class_curie: ClassVar[str] = "sio:CaliforniumAtom"
    class_name: ClassVar[str] = "CaliforniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CaliforniumAtom


class CarbonAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CarbonAtom
    class_class_curie: ClassVar[str] = "sio:CarbonAtom"
    class_name: ClassVar[str] = "CarbonAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CarbonAtom


class CeriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CeriumAtom
    class_class_curie: ClassVar[str] = "sio:CeriumAtom"
    class_name: ClassVar[str] = "CeriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CeriumAtom


class ChemicalSubstance(ChemicalEntity):
    """
    A chemical substance is a chemical entity composed of two or more weakly (non-covalently) interacting chemical
    entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalSubstance
    class_class_curie: ClassVar[str] = "sio:ChemicalSubstance"
    class_name: ClassVar[str] = "ChemicalSubstance"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalSubstance


class Analyte(ChemicalSubstance):
    """
    an analyte is a substance or chemical constituent of interest in an analytical procedure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Analyte
    class_class_curie: ClassVar[str] = "sio:Analyte"
    class_name: ClassVar[str] = "Analyte"
    class_model_uri: ClassVar[URIRef] = SIO.Analyte


class BinaryCompound(ChemicalSubstance):
    """
    A binary compound is a mereological maximum sum of two kinds of weakly connected entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BinaryCompound
    class_class_curie: ClassVar[str] = "sio:BinaryCompound"
    class_name: ClassVar[str] = "BinaryCompound"
    class_model_uri: ClassVar[URIRef] = SIO.BinaryCompound


class Catalyst(ChemicalSubstance):
    """
    A catalyst is a molecule that has the capability to reduce the activation energy of a reaction and hence increase
    the overall rate of reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Catalyst
    class_class_curie: ClassVar[str] = "sio:Catalyst"
    class_name: ClassVar[str] = "Catalyst"
    class_model_uri: ClassVar[URIRef] = SIO.Catalyst


class CentrifugationSubstance(ChemicalSubstance):
    """
    A centrifugation substance is a substance that is the target or product of centrifugation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CentrifugationSubstance
    class_class_curie: ClassVar[str] = "sio:CentrifugationSubstance"
    class_name: ClassVar[str] = "CentrifugationSubstance"
    class_model_uri: ClassVar[URIRef] = SIO.CentrifugationSubstance


class CentrifugationPellet(CentrifugationSubstance):
    """
    A centrifugation pellet is a solid substance that forms as a result of compaction by a centrifuge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CentrifugationPellet
    class_class_curie: ClassVar[str] = "sio:CentrifugationPellet"
    class_name: ClassVar[str] = "CentrifugationPellet"
    class_model_uri: ClassVar[URIRef] = SIO.CentrifugationPellet


class ChemicalComplex(ChemicalSubstance):
    """
    A chemical complex is a chemical substance composed of weakly connected molecules and ions in a known
    stoichiometry.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalComplex
    class_class_curie: ClassVar[str] = "sio:ChemicalComplex"
    class_name: ClassVar[str] = "ChemicalComplex"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalComplex


class ChlorineAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChlorineAtom
    class_class_curie: ClassVar[str] = "sio:ChlorineAtom"
    class_name: ClassVar[str] = "ChlorineAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ChlorineAtom


class ChromiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChromiumAtom
    class_class_curie: ClassVar[str] = "sio:ChromiumAtom"
    class_name: ClassVar[str] = "ChromiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ChromiumAtom


class CobaltAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CobaltAtom
    class_class_curie: ClassVar[str] = "sio:CobaltAtom"
    class_name: ClassVar[str] = "CobaltAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CobaltAtom


class CoperniciumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CoperniciumAtom
    class_class_curie: ClassVar[str] = "sio:CoperniciumAtom"
    class_name: ClassVar[str] = "CoperniciumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CoperniciumAtom


class CopperAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CopperAtom
    class_class_curie: ClassVar[str] = "sio:CopperAtom"
    class_name: ClassVar[str] = "CopperAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CopperAtom


class CuriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CuriumAtom
    class_class_curie: ClassVar[str] = "sio:CuriumAtom"
    class_name: ClassVar[str] = "CuriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.CuriumAtom


class DarmstadtiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DarmstadtiumAtom
    class_class_curie: ClassVar[str] = "sio:DarmstadtiumAtom"
    class_name: ClassVar[str] = "DarmstadtiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.DarmstadtiumAtom


class Drug(ChemicalSubstance):
    """
    A drug is a chemical substance that contains one or more active ingredients that regulate one or more biological
    processes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Drug
    class_class_curie: ClassVar[str] = "sio:Drug"
    class_name: ClassVar[str] = "Drug"
    class_model_uri: ClassVar[URIRef] = SIO.Drug


class DubniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DubniumAtom
    class_class_curie: ClassVar[str] = "sio:DubniumAtom"
    class_name: ClassVar[str] = "DubniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.DubniumAtom


class DysprosiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DysprosiumAtom
    class_class_curie: ClassVar[str] = "sio:DysprosiumAtom"
    class_name: ClassVar[str] = "DysprosiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.DysprosiumAtom


class EinsteiniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EinsteiniumAtom
    class_class_curie: ClassVar[str] = "sio:EinsteiniumAtom"
    class_name: ClassVar[str] = "EinsteiniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.EinsteiniumAtom


class ErbiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ErbiumAtom
    class_class_curie: ClassVar[str] = "sio:ErbiumAtom"
    class_name: ClassVar[str] = "ErbiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ErbiumAtom


class EuropiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EuropiumAtom
    class_class_curie: ClassVar[str] = "sio:EuropiumAtom"
    class_name: ClassVar[str] = "EuropiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.EuropiumAtom


class FermiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FermiumAtom
    class_class_curie: ClassVar[str] = "sio:FermiumAtom"
    class_name: ClassVar[str] = "FermiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.FermiumAtom


class FluorineAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FluorineAtom
    class_class_curie: ClassVar[str] = "sio:FluorineAtom"
    class_name: ClassVar[str] = "FluorineAtom"
    class_model_uri: ClassVar[URIRef] = SIO.FluorineAtom


class FranciumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FranciumAtom
    class_class_curie: ClassVar[str] = "sio:FranciumAtom"
    class_name: ClassVar[str] = "FranciumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.FranciumAtom


class GadoliniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GadoliniumAtom
    class_class_curie: ClassVar[str] = "sio:GadoliniumAtom"
    class_name: ClassVar[str] = "GadoliniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.GadoliniumAtom


class GalliumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GalliumAtom
    class_class_curie: ClassVar[str] = "sio:GalliumAtom"
    class_name: ClassVar[str] = "GalliumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.GalliumAtom


class GermaniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GermaniumAtom
    class_class_curie: ClassVar[str] = "sio:GermaniumAtom"
    class_name: ClassVar[str] = "GermaniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.GermaniumAtom


class GoldAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GoldAtom
    class_class_curie: ClassVar[str] = "sio:GoldAtom"
    class_name: ClassVar[str] = "GoldAtom"
    class_model_uri: ClassVar[URIRef] = SIO.GoldAtom


class HafniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HafniumAtom
    class_class_curie: ClassVar[str] = "sio:HafniumAtom"
    class_name: ClassVar[str] = "HafniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.HafniumAtom


class HassiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HassiumAtom
    class_class_curie: ClassVar[str] = "sio:HassiumAtom"
    class_name: ClassVar[str] = "HassiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.HassiumAtom


class HeliumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HeliumAtom
    class_class_curie: ClassVar[str] = "sio:HeliumAtom"
    class_name: ClassVar[str] = "HeliumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.HeliumAtom


class HeterogeneousSubstance(ChemicalSubstance):
    """
    A heterogeneous substance is a chemical substance that is composed of more than one different kind of component.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HeterogeneousSubstance
    class_class_curie: ClassVar[str] = "sio:HeterogeneousSubstance"
    class_name: ClassVar[str] = "HeterogeneousSubstance"
    class_model_uri: ClassVar[URIRef] = SIO.HeterogeneousSubstance


class BiologicalEntity(HeterogeneousSubstance):
    """
    A biological entity is a heterogeneous substance that contains genomic material or is the product of a biological
    process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiologicalEntity
    class_class_curie: ClassVar[str] = "sio:BiologicalEntity"
    class_name: ClassVar[str] = "BiologicalEntity"
    class_model_uri: ClassVar[URIRef] = SIO.BiologicalEntity


class BiologicalFluid(BiologicalEntity):
    """
    A biological fluid is a fluid of biological origin.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiologicalFluid
    class_class_curie: ClassVar[str] = "sio:BiologicalFluid"
    class_name: ClassVar[str] = "BiologicalFluid"
    class_model_uri: ClassVar[URIRef] = SIO.BiologicalFluid


class Cell(BiologicalEntity):
    """
    A cell is a biological entity that is contained by a plasma membrane.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Cell
    class_class_curie: ClassVar[str] = "sio:Cell"
    class_name: ClassVar[str] = "Cell"
    class_model_uri: ClassVar[URIRef] = SIO.Cell


class CellLine(BiologicalEntity):
    """
    A cell line is a collection of genetically identifical cells.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CellLine
    class_class_curie: ClassVar[str] = "sio:CellLine"
    class_name: ClassVar[str] = "CellLine"
    class_model_uri: ClassVar[URIRef] = SIO.CellLine


class ChemicalSalt(HeterogeneousSubstance):
    """
    a chemical salt is a heterogenous substance composed of an ionic assembly of cations and anions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalSalt
    class_class_curie: ClassVar[str] = "sio:ChemicalSalt"
    class_name: ClassVar[str] = "ChemicalSalt"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalSalt


class Device(HeterogeneousSubstance):
    """
    A device is usually a constructed tool.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Device
    class_class_curie: ClassVar[str] = "sio:Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = SIO.Device


class CommunicationDevice(Device):
    """
    A communication device is a device that facilitates the transmission of information through encoded in an audio or
    digital signal between a sender and a receiver.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CommunicationDevice
    class_class_curie: ClassVar[str] = "sio:CommunicationDevice"
    class_name: ClassVar[str] = "CommunicationDevice"
    class_model_uri: ClassVar[URIRef] = SIO.CommunicationDevice


class DataCollectionDevice(Device):
    """
    A data collection device is a device that collects information about one or more objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataCollectionDevice
    class_class_curie: ClassVar[str] = "sio:DataCollectionDevice"
    class_name: ClassVar[str] = "DataCollectionDevice"
    class_model_uri: ClassVar[URIRef] = SIO.DataCollectionDevice


class DataStorageDevice(Device):
    """
    A data storage device is a device that is capable of storing information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataStorageDevice
    class_class_curie: ClassVar[str] = "sio:DataStorageDevice"
    class_name: ClassVar[str] = "DataStorageDevice"
    class_model_uri: ClassVar[URIRef] = SIO.DataStorageDevice


class Genome(BiologicalEntity):
    """
    A genome is a collection of nucleic acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Genome
    class_class_curie: ClassVar[str] = "sio:Genome"
    class_name: ClassVar[str] = "Genome"
    class_model_uri: ClassVar[URIRef] = SIO.Genome


class HardDiskDrive(DataStorageDevice):
    """
    A hard disk drive (HDD) is a non-volatile, random access device for digital data. It features rotating rigid
    platters on a motor-driven spindle within a protective enclosure. Data is magnetically read and written on the
    platter by read/write heads that float on a film of air above the platters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HardDiskDrive
    class_class_curie: ClassVar[str] = "sio:HardDiskDrive"
    class_name: ClassVar[str] = "HardDiskDrive"
    class_model_uri: ClassVar[URIRef] = SIO.HardDiskDrive


class HolmiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HolmiumAtom
    class_class_curie: ClassVar[str] = "sio:HolmiumAtom"
    class_name: ClassVar[str] = "HolmiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.HolmiumAtom


class HomogeneousSubstance(ChemicalSubstance):
    """
    A homogeneous substance is a substance that is composed of a uniform type of entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HomogeneousSubstance
    class_class_curie: ClassVar[str] = "sio:HomogeneousSubstance"
    class_name: ClassVar[str] = "HomogeneousSubstance"
    class_model_uri: ClassVar[URIRef] = SIO.HomogeneousSubstance


class ChemicalElement(HomogeneousSubstance):
    """
    A chemical element is a (effectively) homogeneous substance composed of one type of atom.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalElement
    class_class_curie: ClassVar[str] = "sio:ChemicalElement"
    class_name: ClassVar[str] = "ChemicalElement"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalElement


class Allotrope(ChemicalElement):
    """
    An allotrope is a structural variant of a chemical element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Allotrope
    class_class_curie: ClassVar[str] = "sio:Allotrope"
    class_name: ClassVar[str] = "Allotrope"
    class_model_uri: ClassVar[URIRef] = SIO.Allotrope


class CarbonAllotrope(Allotrope):
    """
    A carbon allotrope is a chemical substance composed of carbon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CarbonAllotrope
    class_class_curie: ClassVar[str] = "sio:CarbonAllotrope"
    class_name: ClassVar[str] = "CarbonAllotrope"
    class_model_uri: ClassVar[URIRef] = SIO.CarbonAllotrope


class AggregatedCarbonNanorods(CarbonAllotrope):
    """
    aggregate of carbon nanorods is an allotrope of carbon considered to be the least compressible material known, as
    measured by its isothermal bulk modulus; aggregated diamond nanorods have a modulus of 491 gigapascals (GPa),
    while a conventional diamond has a modulus of 442 GPa. ADNRs are also 0.3% denser than regular diamond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AggregatedCarbonNanorods
    class_class_curie: ClassVar[str] = "sio:AggregatedCarbonNanorods"
    class_name: ClassVar[str] = "AggregatedCarbonNanorods"
    class_model_uri: ClassVar[URIRef] = SIO.AggregatedCarbonNanorods


class AmorphousCarbon(CarbonAllotrope):
    """
    amorphous carbon is an allotrope of carbon that does not have any crystalline structure. As with all glassy
    materials, some short-range order can be observed, but there is no long-range pattern of atomic positions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AmorphousCarbon
    class_class_curie: ClassVar[str] = "sio:AmorphousCarbon"
    class_name: ClassVar[str] = "AmorphousCarbon"
    class_model_uri: ClassVar[URIRef] = SIO.AmorphousCarbon


class CarbonNanofoam(CarbonAllotrope):
    """
    carbon nanofoam is an allotrope of carbon that consists of a low-density cluster-assembly of carbon atoms strung
    together in a loose three-dimensional web. Each cluster is about 6 nanometers wide and consists of about 4000
    carbon atoms linked in graphite-like sheets that are given negative curvature by the inclusion of heptagons among
    the regular hexagonal pattern.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CarbonNanofoam
    class_class_curie: ClassVar[str] = "sio:CarbonNanofoam"
    class_name: ClassVar[str] = "CarbonNanofoam"
    class_model_uri: ClassVar[URIRef] = SIO.CarbonNanofoam


class Chaoite(CarbonAllotrope):
    """
    chaoite is an allotrope of carbon that is slightly harder than graphite with a reflection colour of grey to white.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Chaoite
    class_class_curie: ClassVar[str] = "sio:Chaoite"
    class_name: ClassVar[str] = "Chaoite"
    class_model_uri: ClassVar[URIRef] = SIO.Chaoite


class Diamond(CarbonAllotrope):
    """
    diamond is a carbon allotrope in which each carbon atom in diamond is covalently bonded to four other carbons in a
    tetrahedron. These tetrahedrons together form a 3-dimensional network of puckered six-membered rings of atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Diamond
    class_class_curie: ClassVar[str] = "sio:Diamond"
    class_name: ClassVar[str] = "Diamond"
    class_model_uri: ClassVar[URIRef] = SIO.Diamond


class Fullerene(CarbonAllotrope):
    """
    fullerene is a carbon allotrope which take the form of a hollow sphere, ellipsoid, or tube.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Fullerene
    class_class_curie: ClassVar[str] = "sio:Fullerene"
    class_name: ClassVar[str] = "Fullerene"
    class_model_uri: ClassVar[URIRef] = SIO.Fullerene


class GlassyCarbon(CarbonAllotrope):
    """
    glassy carbon is an allotrope of carbon which is widely used as an electrode material in electrochemistry, as well
    as for high temperature crucibles and as a component of some prosthetic devices.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GlassyCarbon
    class_class_curie: ClassVar[str] = "sio:GlassyCarbon"
    class_name: ClassVar[str] = "GlassyCarbon"
    class_model_uri: ClassVar[URIRef] = SIO.GlassyCarbon


class Graphite(CarbonAllotrope):
    """
    graphite is an allotrope of carbon which is a conductor, and is the most stable form of solid carbon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Graphite
    class_class_curie: ClassVar[str] = "sio:Graphite"
    class_name: ClassVar[str] = "Graphite"
    class_model_uri: ClassVar[URIRef] = SIO.Graphite


class HydrogenAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HydrogenAtom
    class_class_curie: ClassVar[str] = "sio:HydrogenAtom"
    class_name: ClassVar[str] = "HydrogenAtom"
    class_model_uri: ClassVar[URIRef] = SIO.HydrogenAtom


class IndiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IndiumAtom
    class_class_curie: ClassVar[str] = "sio:IndiumAtom"
    class_name: ClassVar[str] = "IndiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.IndiumAtom


class Ingredient(ChemicalSubstance):
    """
    an ingredient is a chemical substance that forms part of a mixture.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ingredient
    class_class_curie: ClassVar[str] = "sio:Ingredient"
    class_name: ClassVar[str] = "Ingredient"
    class_model_uri: ClassVar[URIRef] = SIO.Ingredient


class IodineAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IodineAtom
    class_class_curie: ClassVar[str] = "sio:IodineAtom"
    class_name: ClassVar[str] = "IodineAtom"
    class_model_uri: ClassVar[URIRef] = SIO.IodineAtom


class Ion(ChemicalEntity):
    """
    An ion is an atom or molecule in which the total number of electrons is not equal to the total number of protons,
    giving it a net positive or negative electrical charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ion
    class_class_curie: ClassVar[str] = "sio:Ion"
    class_name: ClassVar[str] = "Ion"
    class_model_uri: ClassVar[URIRef] = SIO.Ion


class Anion(Ion):
    """
    An anion is an atom or molecule with a net negative electrical charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Anion
    class_class_curie: ClassVar[str] = "sio:Anion"
    class_name: ClassVar[str] = "Anion"
    class_model_uri: ClassVar[URIRef] = SIO.Anion


class Cation(Ion):
    """
    An anion is an atom or molecule with a net positive electrical charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Cation
    class_class_curie: ClassVar[str] = "sio:Cation"
    class_name: ClassVar[str] = "Cation"
    class_model_uri: ClassVar[URIRef] = SIO.Cation


class IonicCompound(BinaryCompound):
    """
    An ionic compound is a mereological maximal sum of weakly connected paired positive and negative ions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IonicCompound
    class_class_curie: ClassVar[str] = "sio:IonicCompound"
    class_name: ClassVar[str] = "IonicCompound"
    class_model_uri: ClassVar[URIRef] = SIO.IonicCompound


class Ionsdaleite(CarbonAllotrope):
    """
    ionsdaleite is a hexagonal allotrope of the carbon allotrope diamond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ionsdaleite
    class_class_curie: ClassVar[str] = "sio:Ionsdaleite"
    class_name: ClassVar[str] = "Ionsdaleite"
    class_model_uri: ClassVar[URIRef] = SIO.Ionsdaleite


class IridiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IridiumAtom
    class_class_curie: ClassVar[str] = "sio:IridiumAtom"
    class_name: ClassVar[str] = "IridiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.IridiumAtom


class IronAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IronAtom
    class_class_curie: ClassVar[str] = "sio:IronAtom"
    class_name: ClassVar[str] = "IronAtom"
    class_model_uri: ClassVar[URIRef] = SIO.IronAtom


class KryptonAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.KryptonAtom
    class_class_curie: ClassVar[str] = "sio:KryptonAtom"
    class_name: ClassVar[str] = "KryptonAtom"
    class_model_uri: ClassVar[URIRef] = SIO.KryptonAtom


class LanthanumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LanthanumAtom
    class_class_curie: ClassVar[str] = "sio:LanthanumAtom"
    class_name: ClassVar[str] = "LanthanumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.LanthanumAtom


class LawrenciumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LawrenciumAtom
    class_class_curie: ClassVar[str] = "sio:LawrenciumAtom"
    class_name: ClassVar[str] = "LawrenciumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.LawrenciumAtom


class LeadAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LeadAtom
    class_class_curie: ClassVar[str] = "sio:LeadAtom"
    class_name: ClassVar[str] = "LeadAtom"
    class_model_uri: ClassVar[URIRef] = SIO.LeadAtom


class LiquidSolution(HeterogeneousSubstance):
    """
    A liquid solution is a heterogeneous substance in a liquid state.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LiquidSolution
    class_class_curie: ClassVar[str] = "sio:LiquidSolution"
    class_name: ClassVar[str] = "LiquidSolution"
    class_model_uri: ClassVar[URIRef] = SIO.LiquidSolution


class LiquidSolutionComponent(HeterogeneousSubstance):
    """
    A liquid solution component is a part of a liquid solution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LiquidSolutionComponent
    class_class_curie: ClassVar[str] = "sio:LiquidSolutionComponent"
    class_name: ClassVar[str] = "LiquidSolutionComponent"
    class_model_uri: ClassVar[URIRef] = SIO.LiquidSolutionComponent


class Acid(LiquidSolutionComponent):
    """
    An acid is a molecular entity in solution capable of donating a hydron (Bronsted acid) or capable of forming a
    covalent bond with an electron pair (Lewis acid).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Acid
    class_class_curie: ClassVar[str] = "sio:Acid"
    class_name: ClassVar[str] = "Acid"
    class_model_uri: ClassVar[URIRef] = SIO.Acid


class Base(LiquidSolutionComponent):
    """
    A base is a molecular entity dissolved in a solvent that is capable of accepting a proton (Bronsted base) or
    forming a covalent bond with a hydron (Lewis base) .
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Base
    class_class_curie: ClassVar[str] = "sio:Base"
    class_name: ClassVar[str] = "Base"
    class_model_uri: ClassVar[URIRef] = SIO.Base


class Buffer(LiquidSolutionComponent):
    """
    A buffer is a dissolved chemical substance that resists change in pH upon addition of small amounts of acid or
    base.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Buffer
    class_class_curie: ClassVar[str] = "sio:Buffer"
    class_name: ClassVar[str] = "Buffer"
    class_model_uri: ClassVar[URIRef] = SIO.Buffer


class LithiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LithiumAtom
    class_class_curie: ClassVar[str] = "sio:LithiumAtom"
    class_name: ClassVar[str] = "LithiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.LithiumAtom


class LutetiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LutetiumAtom
    class_class_curie: ClassVar[str] = "sio:LutetiumAtom"
    class_name: ClassVar[str] = "LutetiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.LutetiumAtom


class MagnesiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MagnesiumAtom
    class_class_curie: ClassVar[str] = "sio:MagnesiumAtom"
    class_name: ClassVar[str] = "MagnesiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.MagnesiumAtom


class ManganeseAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ManganeseAtom
    class_class_curie: ClassVar[str] = "sio:ManganeseAtom"
    class_name: ClassVar[str] = "ManganeseAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ManganeseAtom


class MassSpectrometer(DataCollectionDevice):
    """
    A mass spectrometer is a device that identifies ions based on their mass to charge ratio using an electromagnetic
    field.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MassSpectrometer
    class_class_curie: ClassVar[str] = "sio:MassSpectrometer"
    class_name: ClassVar[str] = "MassSpectrometer"
    class_model_uri: ClassVar[URIRef] = SIO.MassSpectrometer


@dataclass
class MathematicalEntity(InformationContentEntity):
    """
    A mathematical entity is an information content entity that are components of a mathematical system or can be
    defined in mathematical terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MathematicalEntity
    class_class_curie: ClassVar[str] = "sio:MathematicalEntity"
    class_name: ClassVar[str] = "MathematicalEntity"
    class_model_uri: ClassVar[URIRef] = SIO.MathematicalEntity

    hasUnit: Optional[Union[dict, "UnitOfMeasurement"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasUnit is not None and not isinstance(self.hasUnit, UnitOfMeasurement):
            self.hasUnit = UnitOfMeasurement(**as_dict(self.hasUnit))

        super().__post_init__(**kwargs)


class Algorithm(MathematicalEntity):
    """
    An algorithm is an effective method expressed as a finite list of well-defined instructions for calculating a
    function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Algorithm
    class_class_curie: ClassVar[str] = "sio:Algorithm"
    class_name: ClassVar[str] = "Algorithm"
    class_model_uri: ClassVar[URIRef] = SIO.Algorithm


class Association(MathematicalEntity):
    """
    An assocation is a relationship between two or more entities derived by some informational analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Association
    class_class_curie: ClassVar[str] = "sio:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = SIO.Association


class Chemical-diseaseAssociation(Association):
    """
    A chemical-disease association is an association between a chemical and a disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Chemical-diseaseAssociation"]
    class_class_curie: ClassVar[str] = "sio:Chemical-diseaseAssociation"
    class_name: ClassVar[str] = "Chemical-diseaseAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.Chemical-diseaseAssociation


class Chemical-geneAssocation(Association):
    """
    a chemical-gene assocation is an assocation between a chemical and a gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Chemical-geneAssocation"]
    class_class_curie: ClassVar[str] = "sio:Chemical-geneAssocation"
    class_name: ClassVar[str] = "Chemical-geneAssocation"
    class_model_uri: ClassVar[URIRef] = SIO.Chemical-geneAssocation


class Chemical-pathwayAssociation(Association):
    """
    a chemical-pathway association is an association between a chemical and a pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Chemical-pathwayAssociation"]
    class_class_curie: ClassVar[str] = "sio:Chemical-pathwayAssociation"
    class_name: ClassVar[str] = "Chemical-pathwayAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.Chemical-pathwayAssociation


class DatabaseCross-reference(Association):
    """
    A database cross-reference is an association between one data item and another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["DatabaseCross-reference"]
    class_class_curie: ClassVar[str] = "sio:DatabaseCross-reference"
    class_name: ClassVar[str] = "DatabaseCross-reference"
    class_model_uri: ClassVar[URIRef] = SIO.DatabaseCross-reference


class EpimerAssociation(Association):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EpimerAssociation
    class_class_curie: ClassVar[str] = "sio:EpimerAssociation"
    class_name: ClassVar[str] = "EpimerAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.EpimerAssociation


class Equation(MathematicalEntity):
    """
    An equation is a mathematical statement that asserts the equality of two expressions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Equation
    class_class_curie: ClassVar[str] = "sio:Equation"
    class_name: ClassVar[str] = "Equation"
    class_model_uri: ClassVar[URIRef] = SIO.Equation


class DifferentialEquation(Equation):
    """
    A differential equation is a mathematical equation for an unknown function of one or several variables that
    relates the values of the function itself and its derivatives of various orders.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DifferentialEquation
    class_class_curie: ClassVar[str] = "sio:DifferentialEquation"
    class_name: ClassVar[str] = "DifferentialEquation"
    class_model_uri: ClassVar[URIRef] = SIO.DifferentialEquation


class ExactCross-reference(DatabaseCross-reference):
    """
    An exact cross-reference is a database cross-reference in which one entity is equivalent to the other based on all
    the entitie's attributes (minus the source).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["ExactCross-reference"]
    class_class_curie: ClassVar[str] = "sio:ExactCross-reference"
    class_name: ClassVar[str] = "ExactCross-reference"
    class_model_uri: ClassVar[URIRef] = SIO.ExactCross-reference


class Gene-diseaseAssociation(Association):
    """
    A gene-disease association is an association between a gene and a disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociation"
    class_name: ClassVar[str] = "Gene-diseaseAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociation


class Gene-diseaseBiomarkerAssociation(Gene-diseaseAssociation):
    """
    A gene-disease association in which the gene/protein is involved in the etiology or maintenance of the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseBiomarkerAssociation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseBiomarkerAssociation"
    class_name: ClassVar[str] = "Gene-diseaseBiomarkerAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseBiomarkerAssociation


class Gene-diseaseAssociationLinkedWithAlteredGeneExpression(Gene-diseaseBiomarkerAssociation):
    """
    A gene-disease association in which the disease phenotype is associated with an altered expression of the gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithAlteredGeneExpression"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithAlteredGeneExpression"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithAlteredGeneExpression"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithAlteredGeneExpression


class Gene-diseaseAssociationLinkedWithGenomicAlterations(Gene-diseaseBiomarkerAssociation):
    """
    a gene-disease association that is linked with some genomic alteration
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithGenomicAlterations"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithGenomicAlterations"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithGenomicAlterations"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithGenomicAlterations


class FusionGene-diseaseAssociation(Gene-diseaseAssociationLinkedWithGenomicAlterations):
    """
    A gene-disease association in which the fusion between two different genes (promotor and/or other coding DNA
    regions) is associated with the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["FusionGene-diseaseAssociation"]
    class_class_curie: ClassVar[str] = "sio:FusionGene-diseaseAssociation"
    class_name: ClassVar[str] = "FusionGene-diseaseAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.FusionGene-diseaseAssociation


class Gene-diseaseAssociationLinkedWithChromosomalRearrangement(Gene-diseaseAssociationLinkedWithGenomicAlterations):
    """
    A gene-disease association in which the gene is included in a chromosomal rearrangement associated with a
    particular manifestation of the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithChromosomalRearrangement"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithChromosomalRearrangement"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithChromosomalRearrangement"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithChromosomalRearrangement


class Gene-diseaseAssociationLinkedWithGeneticVariation(Gene-diseaseAssociationLinkedWithGenomicAlterations):
    """
    A gene-disease association in which a sequence variation (a mutation, a SNP) is associated with the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithGeneticVariation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithGeneticVariation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithGeneticVariation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithGeneticVariation


class Gene-diseaseAssociationLinkedWithCausalMutation(Gene-diseaseAssociationLinkedWithGeneticVariation):
    """
    A gene-variant disease association in which a mutation in the gene/protein results in the development or
    maintenance of the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithCausalMutation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithCausalMutation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithCausalMutation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithCausalMutation


class Gene-diseaseAssociationLinkedWithGermlineCausalMutation(Gene-diseaseAssociationLinkedWithCausalMutation):
    """
    A gene-variant disease association in which a germline mutation in the gene/protein results in the development or
    maintenance of the disease, and it may be passed on to offspring.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithGermlineCausalMutation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithGermlineCausalMutation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithGermlineCausalMutation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithGermlineCausalMutation


class Gene-diseaseAssociationLinkedWithModifyingMutation(Gene-diseaseAssociationLinkedWithGeneticVariation):
    """
    A gene-disease association in which a gene mutation is known to modify the clinical presentation of the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithModifyingMutation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithModifyingMutation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithModifyingMutation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithModifyingMutation


class Gene-diseaseAssociationLinkedWithGermlineModifyingMutation(Gene-diseaseAssociationLinkedWithModifyingMutation):
    """
    A gene-variant disease association in which a germline mutation in the gene modifies the clinical presentation of
    the disease, and it may be passed on to offspring.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithGermlineModifyingMutation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithGermlineModifyingMutation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithGermlineModifyingMutation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithGermlineModifyingMutation


class Gene-diseaseAssociationLinkedWithPost-translationalModification(Gene-diseaseBiomarkerAssociation):
    """
    A gene-disease association in which the disease phenotype is associated with post-translational modifications in
    the protein product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithPost-translationalModification"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithPost-translationalModification"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithPost-translationalModification"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithPost-translationalModification


class Gene-diseaseAssociationLinkedWithSomaticCausalMutation(Gene-diseaseAssociationLinkedWithCausalMutation):
    """
    A gene-variant disease association in which a somatic mutation in the gene/protein results in the development or
    maintenance of the disease, and it may not be passed on to offspring.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithSomaticCausalMutation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithSomaticCausalMutation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithSomaticCausalMutation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithSomaticCausalMutation


class Gene-diseaseAssociationLinkedWithSomaticModifyingMutation(Gene-diseaseAssociationLinkedWithModifyingMutation):
    """
    A gene-variant disease association in which a somatic mutation in the gene modifies the clinical presentation of
    the disease, and it may not be passed on to offspring.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithSomaticModifyingMutation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithSomaticModifyingMutation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithSomaticModifyingMutation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithSomaticModifyingMutation


class Gene-diseaseAssociationLinkedWithSusceptibilityMutation(Gene-diseaseAssociationLinkedWithGeneticVariation):
    """
    A gene-disease association in which a germline mutation in the gene predisposes to the development of the disease,
    and it is necessary but not sufficient for the manifestation of the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Gene-diseaseAssociationLinkedWithSusceptibilityMutation"]
    class_class_curie: ClassVar[str] = "sio:Gene-diseaseAssociationLinkedWithSusceptibilityMutation"
    class_name: ClassVar[str] = "Gene-diseaseAssociationLinkedWithSusceptibilityMutation"
    class_model_uri: ClassVar[URIRef] = SIO.Gene-diseaseAssociationLinkedWithSusceptibilityMutation


class Interval(MathematicalEntity):
    """
    an interval is a set of real numbers with the property that any number that lies between two numbers in the set is
    also included in the set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Interval
    class_class_curie: ClassVar[str] = "sio:Interval"
    class_name: ClassVar[str] = "Interval"
    class_model_uri: ClassVar[URIRef] = SIO.Interval


class LeftClosedInterval(Interval):
    """
    a left closed interval is an interval in which there is a real number that is smaller than all its elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LeftClosedInterval
    class_class_curie: ClassVar[str] = "sio:LeftClosedInterval"
    class_name: ClassVar[str] = "LeftClosedInterval"
    class_model_uri: ClassVar[URIRef] = SIO.LeftClosedInterval


class ClosedInterval(LeftClosedInterval):
    """
    A closed interval is an interval that includes its endpoints, and is denoted with square brackets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ClosedInterval
    class_class_curie: ClassVar[str] = "sio:ClosedInterval"
    class_name: ClassVar[str] = "ClosedInterval"
    class_model_uri: ClassVar[URIRef] = SIO.ClosedInterval


class LeftOpenInterval(Interval):
    """
    a left open interval is an interval in which there is no element that is smaller than all other elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LeftOpenInterval
    class_class_curie: ClassVar[str] = "sio:LeftOpenInterval"
    class_name: ClassVar[str] = "LeftOpenInterval"
    class_model_uri: ClassVar[URIRef] = SIO.LeftOpenInterval


class LogicalOperator(MathematicalEntity):
    """
    A logical operator is a unary or binary relation to construct logical expressions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LogicalOperator
    class_class_curie: ClassVar[str] = "sio:LogicalOperator"
    class_name: ClassVar[str] = "LogicalOperator"
    class_model_uri: ClassVar[URIRef] = SIO.LogicalOperator


class Conjunctionand(LogicalOperator):
    """
    AND is a logical operator that has the value true if both of its operands are true, otherwise a value of false.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Conjunctionand
    class_class_curie: ClassVar[str] = "sio:Conjunctionand"
    class_name: ClassVar[str] = "Conjunctionand"
    class_model_uri: ClassVar[URIRef] = SIO.Conjunctionand


class Disjunctionor(LogicalOperator):
    """
    OR is a logical operator that results in true whenever one or more of its operands are true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Disjunctionor
    class_class_curie: ClassVar[str] = "sio:Disjunctionor"
    class_name: ClassVar[str] = "Disjunctionor"
    class_model_uri: ClassVar[URIRef] = SIO.Disjunctionor


class ExclusiveDisjunctionxor(Disjunctionor):
    """
    XOR, also called exclusive disjunction or (symbolized XOR, EOR, EXOR, or ⊕), is a type of logical disjunction on
    two operands that results in a value of true if exactly one of the operands has a value of true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ExclusiveDisjunctionxor
    class_class_curie: ClassVar[str] = "sio:ExclusiveDisjunctionxor"
    class_name: ClassVar[str] = "ExclusiveDisjunctionxor"
    class_model_uri: ClassVar[URIRef] = SIO.ExclusiveDisjunctionxor


class Implies-%3E(LogicalOperator):
    """
    Implication is a logical operator that holds between a set T of propositions and a proposition B, when every model
    (or interpretation or valuation) of T is also a model of B.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Implies-%3E"]
    class_class_curie: ClassVar[str] = "sio:Implies-%3E"
    class_name: ClassVar[str] = "Implies-%3E"
    class_model_uri: ClassVar[URIRef] = SIO.Implies-%3E


class Media(InformationContentEntity):
    """
    media are audo/visual/audiovisual modes of communicating information for mass consumption.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Media
    class_class_curie: ClassVar[str] = "sio:Media"
    class_name: ClassVar[str] = "Media"
    class_model_uri: ClassVar[URIRef] = SIO.Media


class AudioRecording(Media):
    """
    An audio recording is an electrical or mechanical inscription and re-creation of sound waves, such as spoken
    voice, singing, instrumental music, or sound effects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AudioRecording
    class_class_curie: ClassVar[str] = "sio:AudioRecording"
    class_name: ClassVar[str] = "AudioRecording"
    class_model_uri: ClassVar[URIRef] = SIO.AudioRecording


class Figure(Media):
    """
    A figure is a graphical entity which consists of a visual (n-dimentional) arrangement of information entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Figure
    class_class_curie: ClassVar[str] = "sio:Figure"
    class_name: ClassVar[str] = "Figure"
    class_model_uri: ClassVar[URIRef] = SIO.Figure


class Chart(Figure):
    """
    A chart is a figure that displays the relationship among tabular numeric data, functions or some kinds of
    qualitative structures.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Chart
    class_class_curie: ClassVar[str] = "sio:Chart"
    class_name: ClassVar[str] = "Chart"
    class_model_uri: ClassVar[URIRef] = SIO.Chart


class BubbleChart(Chart):
    """
    A bubble chart contains circles whose area corresponds to a value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BubbleChart
    class_class_curie: ClassVar[str] = "sio:BubbleChart"
    class_name: ClassVar[str] = "BubbleChart"
    class_model_uri: ClassVar[URIRef] = SIO.BubbleChart


class FigurePart(Media):
    """
    A figure part is a part of a figure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FigurePart
    class_class_curie: ClassVar[str] = "sio:FigurePart"
    class_name: ClassVar[str] = "FigurePart"
    class_model_uri: ClassVar[URIRef] = SIO.FigurePart


class File(Media):
    """
    A file is an information-bearing object that contains a physical embodiment of some information using a particular
    character encoding.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.File
    class_class_curie: ClassVar[str] = "sio:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = SIO.File


class Flowchart(Chart):
    """
    A flowchart is a diagram that represents an algorithm or process, showing the steps as boxes of various kinds, and
    their order by connecting these with arrows.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Flowchart
    class_class_curie: ClassVar[str] = "sio:Flowchart"
    class_name: ClassVar[str] = "Flowchart"
    class_model_uri: ClassVar[URIRef] = SIO.Flowchart


class GanttChart(Chart):
    """
    A Gantt chart is a bar chart that illustrates a project schedule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GanttChart
    class_class_curie: ClassVar[str] = "sio:GanttChart"
    class_name: ClassVar[str] = "GanttChart"
    class_model_uri: ClassVar[URIRef] = SIO.GanttChart


class Heatmap(Chart):
    """
    A heatmap is a graphical representation of data where the individual values contained in a matrix are represented
    as colors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Heatmap
    class_class_curie: ClassVar[str] = "sio:Heatmap"
    class_name: ClassVar[str] = "Heatmap"
    class_model_uri: ClassVar[URIRef] = SIO.Heatmap


class GeographicHeatmap(Heatmap):
    """
    A geographic heatmap is a graphical representation of data over a geographic region where individual values are
    represented as colors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeographicHeatmap
    class_class_curie: ClassVar[str] = "sio:GeographicHeatmap"
    class_name: ClassVar[str] = "GeographicHeatmap"
    class_model_uri: ClassVar[URIRef] = SIO.GeographicHeatmap


class Histogram(Chart):
    """
    A histogram is a graphical representation of data which consists of tabular frequencies, shown as adjacent
    rectangles, over discrete intervals (bins) , with an area equal to the frequency of the observations in the
    interval.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Histogram
    class_class_curie: ClassVar[str] = "sio:Histogram"
    class_name: ClassVar[str] = "Histogram"
    class_model_uri: ClassVar[URIRef] = SIO.Histogram


class BlockHistogram(Histogram):
    """
    A block histogram contains an x-axis that is divided into bins which correspond to value ranges. Each item in the
    data set is drawn as a rectangular block, and the blocks are piled into the bins to show how many values in each
    range.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BlockHistogram
    class_class_curie: ClassVar[str] = "sio:BlockHistogram"
    class_name: ClassVar[str] = "BlockHistogram"
    class_model_uri: ClassVar[URIRef] = SIO.BlockHistogram


class Image(Figure):
    """
    An image is an affine projection of a visual entity to a two dimensional surface.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Image
    class_class_curie: ClassVar[str] = "sio:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = SIO.Image


class Legend(FigurePart):
    """
    A legend is a part of a figure that associates textual descriptions with symbols pertaining to plotted entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Legend
    class_class_curie: ClassVar[str] = "sio:Legend"
    class_name: ClassVar[str] = "Legend"
    class_model_uri: ClassVar[URIRef] = SIO.Legend


class Map(Chart):
    """
    A map is a a visual representation of an area that depicts the relationship between elements of that space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Map
    class_class_curie: ClassVar[str] = "sio:Map"
    class_name: ClassVar[str] = "Map"
    class_model_uri: ClassVar[URIRef] = SIO.Map


class MatrixChart(Chart):
    """
    A matrix chart summarizes a multidimensional data set in a grid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MatrixChart
    class_class_curie: ClassVar[str] = "sio:MatrixChart"
    class_name: ClassVar[str] = "MatrixChart"
    class_model_uri: ClassVar[URIRef] = SIO.MatrixChart


class MedicalHistory(History):
    """
    A medical history is a record of the events of a recipient of medical care.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalHistory
    class_class_curie: ClassVar[str] = "sio:MedicalHistory"
    class_name: ClassVar[str] = "MedicalHistory"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalHistory


class MeitneriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MeitneriumAtom
    class_class_curie: ClassVar[str] = "sio:MeitneriumAtom"
    class_name: ClassVar[str] = "MeitneriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.MeitneriumAtom


class MendeleviumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MendeleviumAtom
    class_class_curie: ClassVar[str] = "sio:MendeleviumAtom"
    class_name: ClassVar[str] = "MendeleviumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.MendeleviumAtom


class MercuryAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MercuryAtom
    class_class_curie: ClassVar[str] = "sio:MercuryAtom"
    class_name: ClassVar[str] = "MercuryAtom"
    class_model_uri: ClassVar[URIRef] = SIO.MercuryAtom


class MereologicalChart(Chart):
    """
    A mereological chart is a chart that illustrates the parts in the context of the whole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MereologicalChart
    class_class_curie: ClassVar[str] = "sio:MereologicalChart"
    class_name: ClassVar[str] = "MereologicalChart"
    class_model_uri: ClassVar[URIRef] = SIO.MereologicalChart


class Metadata(DataItem):
    """
    metadata is data that provides information about data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Metadata
    class_class_curie: ClassVar[str] = "sio:Metadata"
    class_name: ClassVar[str] = "Metadata"
    class_model_uri: ClassVar[URIRef] = SIO.Metadata


class MicroarrayDevice(DataCollectionDevice):
    """
    A microarray device is a device that identifies the binding of a target substance to a physically immobile
    substrate placed in an array or lattice.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MicroarrayDevice
    class_class_curie: ClassVar[str] = "sio:MicroarrayDevice"
    class_name: ClassVar[str] = "MicroarrayDevice"
    class_model_uri: ClassVar[URIRef] = SIO.MicroarrayDevice


class MolecularComplex(ChemicalComplex):
    """
    A molecular complex is a chemical complex composed of at least one weakly interacting molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularComplex
    class_class_curie: ClassVar[str] = "sio:MolecularComplex"
    class_name: ClassVar[str] = "MolecularComplex"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularComplex


class Chromosome(MolecularComplex):
    """
    A chromosome is a molecular complex of circular or linear DNA and bound proteins.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Chromosome
    class_class_curie: ClassVar[str] = "sio:Chromosome"
    class_name: ClassVar[str] = "Chromosome"
    class_model_uri: ClassVar[URIRef] = SIO.Chromosome


class DoubleStrandedNucleicAcid(MolecularComplex):
    """
    double stranded nucleic acid is a molecular complex composed of two weakly connected nucleic acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DoubleStrandedNucleicAcid
    class_class_curie: ClassVar[str] = "sio:DoubleStrandedNucleicAcid"
    class_name: ClassVar[str] = "DoubleStrandedNucleicAcid"
    class_model_uri: ClassVar[URIRef] = SIO.DoubleStrandedNucleicAcid


class DoubleStrandedDNA(DoubleStrandedNucleicAcid):
    """
    double stranded nucleic acid is a molecular complex composed of two weakly connected deoxyribonucleic acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DoubleStrandedDNA
    class_class_curie: ClassVar[str] = "sio:DoubleStrandedDNA"
    class_name: ClassVar[str] = "DoubleStrandedDNA"
    class_model_uri: ClassVar[URIRef] = SIO.DoubleStrandedDNA


class DoubleStrandedRNA(DoubleStrandedNucleicAcid):
    """
    double stranded nucleic acid is a molecular complex composed of two weakly connected ribonucleic acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DoubleStrandedRNA
    class_class_curie: ClassVar[str] = "sio:DoubleStrandedRNA"
    class_name: ClassVar[str] = "DoubleStrandedRNA"
    class_model_uri: ClassVar[URIRef] = SIO.DoubleStrandedRNA


class MolecularStructureFile(File):
    """
    A molecular structure file is a file that contains a description of molecular structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularStructureFile
    class_class_curie: ClassVar[str] = "sio:MolecularStructureFile"
    class_name: ClassVar[str] = "MolecularStructureFile"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularStructureFile


class Molecule(ChemicalEntity):
    """
    A molecule is a single chemical entity composed of fully covalently bonded atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Molecule
    class_class_curie: ClassVar[str] = "sio:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = SIO.Molecule


class Antigen(Molecule):
    """
    An antigen is a molecule that can be bound by a major histocompatibility complex (MHC) and presented to a T-cell
    receptor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Antigen
    class_class_curie: ClassVar[str] = "sio:Antigen"
    class_name: ClassVar[str] = "Antigen"
    class_model_uri: ClassVar[URIRef] = SIO.Antigen


class Isomer(Molecule):
    """
    An isomer is a molecule that is compositionally identical to another molecule as a result of a different atomic
    connectivity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Isomer
    class_class_curie: ClassVar[str] = "sio:Isomer"
    class_name: ClassVar[str] = "Isomer"
    class_model_uri: ClassVar[URIRef] = SIO.Isomer


class Ligand(Molecule):
    """
    A ligand is a molecule that is part of a complex by weakly interacting with another molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ligand
    class_class_curie: ClassVar[str] = "sio:Ligand"
    class_name: ClassVar[str] = "Ligand"
    class_model_uri: ClassVar[URIRef] = SIO.Ligand


class MolecularRegulator(Molecule):
    """
    A molecular regulator is a molecule that regulates the function of another chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularRegulator
    class_class_curie: ClassVar[str] = "sio:MolecularRegulator"
    class_name: ClassVar[str] = "MolecularRegulator"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularRegulator


class Activator(MolecularRegulator):
    """
    A molecular activator is a molecular regulator that realizes its disposition to conformationally change a target
    molecule and increase its functionality.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Activator
    class_class_curie: ClassVar[str] = "sio:Activator"
    class_name: ClassVar[str] = "Activator"
    class_model_uri: ClassVar[URIRef] = SIO.Activator


class Inhibitor(MolecularRegulator):
    """
    A molecular inhibitor is a molecular regulator that realizes its disposition to conformationally change a target
    molecule and decrease its functionality.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Inhibitor
    class_class_curie: ClassVar[str] = "sio:Inhibitor"
    class_name: ClassVar[str] = "Inhibitor"
    class_model_uri: ClassVar[URIRef] = SIO.Inhibitor


class MolybdemumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolybdemumAtom
    class_class_curie: ClassVar[str] = "sio:MolybdemumAtom"
    class_name: ClassVar[str] = "MolybdemumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.MolybdemumAtom


class Morpheme(LanguageEntity):
    """
    A morpheme is the smallest semantically meaningful unit in a language.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Morpheme
    class_class_curie: ClassVar[str] = "sio:Morpheme"
    class_name: ClassVar[str] = "Morpheme"
    class_model_uri: ClassVar[URIRef] = SIO.Morpheme


class MovementEquation(Equation):
    """
    A movement equation describes the displacement of an object in space over time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MovementEquation
    class_class_curie: ClassVar[str] = "sio:MovementEquation"
    class_name: ClassVar[str] = "MovementEquation"
    class_model_uri: ClassVar[URIRef] = SIO.MovementEquation


class DiffusionEquation(MovementEquation):
    """
    A diffusion equation describes density fluctuations in a material undergoing diffusion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DiffusionEquation
    class_class_curie: ClassVar[str] = "sio:DiffusionEquation"
    class_name: ClassVar[str] = "DiffusionEquation"
    class_model_uri: ClassVar[URIRef] = SIO.DiffusionEquation


class Movie(Media):
    """
    A movie is a series of images that are displayed in rapid succession  to give the impression of movement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Movie
    class_class_curie: ClassVar[str] = "sio:Movie"
    class_name: ClassVar[str] = "Movie"
    class_model_uri: ClassVar[URIRef] = SIO.Movie


class Namespace(ComputationalEntity):
    """
    A namespace is an informational entity that defines a logical container for a set of symbols or identifiers.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Namespace
    class_class_curie: ClassVar[str] = "sio:Namespace"
    class_name: ClassVar[str] = "Namespace"
    class_model_uri: ClassVar[URIRef] = SIO.Namespace


class Negationnot(LogicalOperator):
    """
    NOT is a logical operator in that has the value true if its operand is false.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Negationnot
    class_class_curie: ClassVar[str] = "sio:Negationnot"
    class_name: ClassVar[str] = "Negationnot"
    class_model_uri: ClassVar[URIRef] = SIO.Negationnot


class NeodymiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NeodymiumAtom
    class_class_curie: ClassVar[str] = "sio:NeodymiumAtom"
    class_name: ClassVar[str] = "NeodymiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.NeodymiumAtom


class NeonAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NeonAtom
    class_class_curie: ClassVar[str] = "sio:NeonAtom"
    class_name: ClassVar[str] = "NeonAtom"
    class_model_uri: ClassVar[URIRef] = SIO.NeonAtom


class NeptuniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NeptuniumAtom
    class_class_curie: ClassVar[str] = "sio:NeptuniumAtom"
    class_name: ClassVar[str] = "NeptuniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.NeptuniumAtom


class NetworkDiagram(Chart):
    """
    A network diagram consists of a set of vertices connected by edges.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NetworkDiagram
    class_class_curie: ClassVar[str] = "sio:NetworkDiagram"
    class_name: ClassVar[str] = "NetworkDiagram"
    class_model_uri: ClassVar[URIRef] = SIO.NetworkDiagram


class DirectedAcyclicGraph(NetworkDiagram):
    """
    a directed acyclic graph or DAG is a network digram that contains directed edges in which nodes may have multiple
    parents, but there are no cycles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DirectedAcyclicGraph
    class_class_curie: ClassVar[str] = "sio:DirectedAcyclicGraph"
    class_name: ClassVar[str] = "DirectedAcyclicGraph"
    class_model_uri: ClassVar[URIRef] = SIO.DirectedAcyclicGraph


class NickelAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NickelAtom
    class_class_curie: ClassVar[str] = "sio:NickelAtom"
    class_name: ClassVar[str] = "NickelAtom"
    class_model_uri: ClassVar[URIRef] = SIO.NickelAtom


class NiobiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NiobiumAtom
    class_class_curie: ClassVar[str] = "sio:NiobiumAtom"
    class_name: ClassVar[str] = "NiobiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.NiobiumAtom


class NitrogenAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NitrogenAtom
    class_class_curie: ClassVar[str] = "sio:NitrogenAtom"
    class_name: ClassVar[str] = "NitrogenAtom"
    class_model_uri: ClassVar[URIRef] = SIO.NitrogenAtom


class NmrDevice(DataCollectionDevice):
    """
    A nuclear magnetic resonance (NMR) device is a device that applies a magnetic field to perturb nuclei with an odd
    number of protons and/or of neutrons in order to hav them absort and re-emit electromagnetic radiation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NmrDevice
    class_class_curie: ClassVar[str] = "sio:NmrDevice"
    class_name: ClassVar[str] = "NmrDevice"
    class_model_uri: ClassVar[URIRef] = SIO.NmrDevice


class NobeliumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NobeliumAtom
    class_class_curie: ClassVar[str] = "sio:NobeliumAtom"
    class_name: ClassVar[str] = "NobeliumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.NobeliumAtom


class OpenInterval(LeftOpenInterval):
    """
    an open interval is an interval that does not include its endpoints.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OpenInterval
    class_class_curie: ClassVar[str] = "sio:OpenInterval"
    class_name: ClassVar[str] = "OpenInterval"
    class_model_uri: ClassVar[URIRef] = SIO.OpenInterval


class OrdinaryDifferentialEquation(DifferentialEquation):
    """
    An ordinary differential equation (ODE) is a differential equation in which the unknown function (also known as
    the dependent variable) is a function of a single independent variable.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrdinaryDifferentialEquation
    class_class_curie: ClassVar[str] = "sio:OrdinaryDifferentialEquation"
    class_name: ClassVar[str] = "OrdinaryDifferentialEquation"
    class_model_uri: ClassVar[URIRef] = SIO.OrdinaryDifferentialEquation


class Organ(BiologicalEntity):
    """
    An organ is a collection of tissues joined in structural unit to serve a common function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Organ
    class_class_curie: ClassVar[str] = "sio:Organ"
    class_name: ClassVar[str] = "Organ"
    class_model_uri: ClassVar[URIRef] = SIO.Organ


class OrganicMolecule(Molecule):
    """
    An organic molecule is a molecule composed of organic atoms (at least carbon, hydrogen, and optionally oxygen,
    phosphorus, nitrogen, sulfur)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrganicMolecule
    class_class_curie: ClassVar[str] = "sio:OrganicMolecule"
    class_name: ClassVar[str] = "OrganicMolecule"
    class_model_uri: ClassVar[URIRef] = SIO.OrganicMolecule


class AminoAcid(OrganicMolecule):
    """
    An amino acid is an organic molecule composed of a carbon bonded to four different groups: a carboxyl group, an
    amino group, an R group, and a hydrogen atom. In the case of glycine, the R group is another hydrogen atom.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AminoAcid
    class_class_curie: ClassVar[str] = "sio:AminoAcid"
    class_name: ClassVar[str] = "AminoAcid"
    class_model_uri: ClassVar[URIRef] = SIO.AminoAcid


class Lipid(OrganicMolecule):
    """
    A lipid is a water-insoluable organic molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Lipid
    class_class_curie: ClassVar[str] = "sio:Lipid"
    class_name: ClassVar[str] = "Lipid"
    class_model_uri: ClassVar[URIRef] = SIO.Lipid


class Monosaccharide(OrganicMolecule):
    """
    A monosaccharide is an organic molecule that consists of a single polyhydroxy aldehyde or ketone group.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Monosaccharide
    class_class_curie: ClassVar[str] = "sio:Monosaccharide"
    class_name: ClassVar[str] = "Monosaccharide"
    class_model_uri: ClassVar[URIRef] = SIO.Monosaccharide


class OrganicPolymer(OrganicMolecule):
    """
    An organic polymer is an organic molecule composed of connected set of monomeric units.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrganicPolymer
    class_class_curie: ClassVar[str] = "sio:OrganicPolymer"
    class_name: ClassVar[str] = "OrganicPolymer"
    class_model_uri: ClassVar[URIRef] = SIO.OrganicPolymer


class AminoAcidPolymer(OrganicPolymer):
    """
    an amino acid polymer is an organic polymer composed of two or more amino acid residues.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AminoAcidPolymer
    class_class_curie: ClassVar[str] = "sio:AminoAcidPolymer"
    class_name: ClassVar[str] = "AminoAcidPolymer"
    class_model_uri: ClassVar[URIRef] = SIO.AminoAcidPolymer


class Biopolymer(OrganicPolymer):
    """
    A biopolymer is an organic polymer that are typically produced by the cells of living organisms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Biopolymer
    class_class_curie: ClassVar[str] = "sio:Biopolymer"
    class_name: ClassVar[str] = "Biopolymer"
    class_model_uri: ClassVar[URIRef] = SIO.Biopolymer


class Carbohydrate(OrganicPolymer):
    """
    a carbohydrate is an organic molecule composed of two or more monosaccharides.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Carbohydrate
    class_class_curie: ClassVar[str] = "sio:Carbohydrate"
    class_name: ClassVar[str] = "Carbohydrate"
    class_model_uri: ClassVar[URIRef] = SIO.Carbohydrate


class NucleicAcid(OrganicPolymer):
    """
    A nucleic acid is an organic polymer composed of a sequence of nucleotide residues.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NucleicAcid
    class_class_curie: ClassVar[str] = "sio:NucleicAcid"
    class_name: ClassVar[str] = "NucleicAcid"
    class_model_uri: ClassVar[URIRef] = SIO.NucleicAcid


class DeoxyribonucleicAcid(NucleicAcid):
    """
    A deoxyribonucleic acid is an organic polymer composed of a sequence of deoxyribonucleotide residues.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcid
    class_class_curie: ClassVar[str] = "sio:DeoxyribonucleicAcid"
    class_name: ClassVar[str] = "DeoxyribonucleicAcid"
    class_model_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcid


class DeoxyribonucleicAcidTemplate(DeoxyribonucleicAcid):
    """
    A deoxyribonucleic acid template is a deoxyribonucleic acid that provides the template to synthesize a
    complementary strand of DNA through transcription.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcidTemplate
    class_class_curie: ClassVar[str] = "sio:DeoxyribonucleicAcidTemplate"
    class_name: ClassVar[str] = "DeoxyribonucleicAcidTemplate"
    class_model_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcidTemplate


class NucleicAcidStrand(NucleicAcid):
    """
    A nucleic acid strand is a single-stranded nucleic acid that is part of a double stranded nucleic acid complex.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NucleicAcidStrand
    class_class_curie: ClassVar[str] = "sio:NucleicAcidStrand"
    class_name: ClassVar[str] = "NucleicAcidStrand"
    class_model_uri: ClassVar[URIRef] = SIO.NucleicAcidStrand


class NegativeNucleicAcidStrand(NucleicAcidStrand):
    """
    The negative nucleic acid strand is the strand that is that is complimentary to the forward strand and appears
    from 3' to 5'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NegativeNucleicAcidStrand
    class_class_curie: ClassVar[str] = "sio:NegativeNucleicAcidStrand"
    class_name: ClassVar[str] = "NegativeNucleicAcidStrand"
    class_model_uri: ClassVar[URIRef] = SIO.NegativeNucleicAcidStrand


class Oligopeptide(AminoAcidPolymer):
    """
    an oligopeptide is an organic polymer composed of fewer than 10 or 15 amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Oligopeptide
    class_class_curie: ClassVar[str] = "sio:Oligopeptide"
    class_name: ClassVar[str] = "Oligopeptide"
    class_model_uri: ClassVar[URIRef] = SIO.Oligopeptide


class Organism(BiologicalEntity):
    """
    A biological organisn is a biological entity that consists of one or more cells and is capable of genomic
    replication (independently or not).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Organism
    class_class_curie: ClassVar[str] = "sio:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = SIO.Organism


class CellularOrganism(Organism):
    """
    A cellular organism is an organism that contains one or more cells.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CellularOrganism
    class_class_curie: ClassVar[str] = "sio:CellularOrganism"
    class_name: ClassVar[str] = "CellularOrganism"
    class_model_uri: ClassVar[URIRef] = SIO.CellularOrganism


class Host(Organism):
    """
    A host is an organism that harbors a parasite, or a mutual or commensal symbiont, typically providing nourishment
    and shelter.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Host
    class_class_curie: ClassVar[str] = "sio:Host"
    class_name: ClassVar[str] = "Host"
    class_model_uri: ClassVar[URIRef] = SIO.Host


class MulticellularOrganism(CellularOrganism):
    """
    A multi-cellular organism is an organism that consists of more than one cell.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MulticellularOrganism
    class_class_curie: ClassVar[str] = "sio:MulticellularOrganism"
    class_name: ClassVar[str] = "MulticellularOrganism"
    class_model_uri: ClassVar[URIRef] = SIO.MulticellularOrganism


class Human(MulticellularOrganism):
    """
    A human is a primates of the family Hominidae and are characterized by having a large brain relative to body size,
    with a well developed neocortex, prefrontal cortex and temporal lobes, making them capable of abstract reasoning,
    language, introspection, problem solving and culture through social learning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Human
    class_class_curie: ClassVar[str] = "sio:Human"
    class_name: ClassVar[str] = "Human"
    class_model_uri: ClassVar[URIRef] = SIO.Human


class Mouse(MulticellularOrganism):
    """
    A mouse is a small mammal belonging to the order of rodents, characteristically having a pointed snout, small
    rounded ears, and a long naked or almost hairless tail.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Mouse
    class_class_curie: ClassVar[str] = "sio:Mouse"
    class_name: ClassVar[str] = "Mouse"
    class_model_uri: ClassVar[URIRef] = SIO.Mouse


class Non-cellularOrganism(Organism):
    """
    A non-cellular organism is an organism that does not contain a cell.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Non-cellularOrganism"]
    class_class_curie: ClassVar[str] = "sio:Non-cellularOrganism"
    class_name: ClassVar[str] = "Non-cellularOrganism"
    class_model_uri: ClassVar[URIRef] = SIO.Non-cellularOrganism


class OsmiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OsmiumAtom
    class_class_curie: ClassVar[str] = "sio:OsmiumAtom"
    class_name: ClassVar[str] = "OsmiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.OsmiumAtom


class Ovopub(ComputationalEntity):
    """
    An ovopub is an information content entity that contains and links to one or more resources and/or statements,
    including those describing its provenance, and is itself a dereferenceable resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ovopub
    class_class_curie: ClassVar[str] = "sio:Ovopub"
    class_name: ClassVar[str] = "Ovopub"
    class_model_uri: ClassVar[URIRef] = SIO.Ovopub


class AssertionOvopub(Ovopub):
    """
    An assertion ovopub is an ovopub that contains and links to an assertion subgraph with one or more statements that
    may be true or false, as well as statements describing its provenance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AssertionOvopub
    class_class_curie: ClassVar[str] = "sio:AssertionOvopub"
    class_name: ClassVar[str] = "AssertionOvopub"
    class_model_uri: ClassVar[URIRef] = SIO.AssertionOvopub


class CollectionOvopub(Ovopub):
    """
    A collection ovopub is an ovopub that contains and links to one or more assertion subgraphs and/or ovopubs, as
    well as statements describing its provenance. It is used to share a specific set of items or restrict a search to
    the resources contained therein.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CollectionOvopub
    class_class_curie: ClassVar[str] = "sio:CollectionOvopub"
    class_name: ClassVar[str] = "CollectionOvopub"
    class_model_uri: ClassVar[URIRef] = SIO.CollectionOvopub


class OxygenAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OxygenAtom
    class_class_curie: ClassVar[str] = "sio:OxygenAtom"
    class_name: ClassVar[str] = "OxygenAtom"
    class_model_uri: ClassVar[URIRef] = SIO.OxygenAtom


class PDBFile(MolecularStructureFile):
    """
    A PDB file is a molecular structure file specified by the Protein DataBank (PDB).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PDBFile
    class_class_curie: ClassVar[str] = "sio:PDBFile"
    class_name: ClassVar[str] = "PDBFile"
    class_model_uri: ClassVar[URIRef] = SIO.PDBFile


class PageRange(Interval):
    """
    A page range denotes the start and end page in some document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PageRange
    class_class_curie: ClassVar[str] = "sio:PageRange"
    class_name: ClassVar[str] = "PageRange"
    class_model_uri: ClassVar[URIRef] = SIO.PageRange


class PalladiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PalladiumAtom
    class_class_curie: ClassVar[str] = "sio:PalladiumAtom"
    class_name: ClassVar[str] = "PalladiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PalladiumAtom


class PartialDifferentialEquation(DifferentialEquation):
    """
    A partial differential equation (PDE) is a differential equation in which the unknown function is a function of
    multiple independent variables and the equation involves its partial derivatives.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PartialDifferentialEquation
    class_class_curie: ClassVar[str] = "sio:PartialDifferentialEquation"
    class_name: ClassVar[str] = "PartialDifferentialEquation"
    class_model_uri: ClassVar[URIRef] = SIO.PartialDifferentialEquation


class Pathogen(Organism):
    """
    A pathogen or infectious agent  is a microorganism that causes disease in its host.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pathogen
    class_class_curie: ClassVar[str] = "sio:Pathogen"
    class_name: ClassVar[str] = "Pathogen"
    class_model_uri: ClassVar[URIRef] = SIO.Pathogen


class Pattern(MathematicalEntity):
    """
    A pattern is a generalized representation of some repeatable concrete or informational item.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pattern
    class_class_curie: ClassVar[str] = "sio:Pattern"
    class_name: ClassVar[str] = "Pattern"
    class_model_uri: ClassVar[URIRef] = SIO.Pattern


class Peptide(AminoAcidPolymer):
    """
    a peptide is an organic polymer composed of between two and fifty amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Peptide
    class_class_curie: ClassVar[str] = "sio:Peptide"
    class_name: ClassVar[str] = "Peptide"
    class_model_uri: ClassVar[URIRef] = SIO.Peptide


class PharmaceuticalDrug(Drug):
    """
    A pharmaceutical preparation is a chemical substance that is approved for use in the medical diagnosis, cure,
    treatment, or prevention of disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PharmaceuticalDrug
    class_class_curie: ClassVar[str] = "sio:PharmaceuticalDrug"
    class_name: ClassVar[str] = "PharmaceuticalDrug"
    class_model_uri: ClassVar[URIRef] = SIO.PharmaceuticalDrug


class Biologic(PharmaceuticalDrug):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Biologic
    class_class_curie: ClassVar[str] = "sio:Biologic"
    class_name: ClassVar[str] = "Biologic"
    class_model_uri: ClassVar[URIRef] = SIO.Biologic


class PharmaceuticalIngredient(Ingredient):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PharmaceuticalIngredient
    class_class_curie: ClassVar[str] = "sio:PharmaceuticalIngredient"
    class_name: ClassVar[str] = "PharmaceuticalIngredient"
    class_model_uri: ClassVar[URIRef] = SIO.PharmaceuticalIngredient


class ActiveIngredient(PharmaceuticalIngredient):
    """
    An active ingredient is a molecular entity that exhibits biological activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ActiveIngredient
    class_class_curie: ClassVar[str] = "sio:ActiveIngredient"
    class_name: ClassVar[str] = "ActiveIngredient"
    class_model_uri: ClassVar[URIRef] = SIO.ActiveIngredient


class InactiveIngredient(PharmaceuticalIngredient):
    """
    Aninactive ingredient is a molecular entity that does not exhibit biological activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InactiveIngredient
    class_class_curie: ClassVar[str] = "sio:InactiveIngredient"
    class_name: ClassVar[str] = "InactiveIngredient"
    class_model_uri: ClassVar[URIRef] = SIO.InactiveIngredient


class PhosphorusAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PhosphorusAtom
    class_class_curie: ClassVar[str] = "sio:PhosphorusAtom"
    class_name: ClassVar[str] = "PhosphorusAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PhosphorusAtom


class Photograph(Image):
    """
    A photograph is an image created by light falling on a light-sensitive surface.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Photograph
    class_class_curie: ClassVar[str] = "sio:Photograph"
    class_name: ClassVar[str] = "Photograph"
    class_model_uri: ClassVar[URIRef] = SIO.Photograph


class GeographicImage(Photograph):
    """
    A geographic image is a photograph of some geographical area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeographicImage
    class_class_curie: ClassVar[str] = "sio:GeographicImage"
    class_name: ClassVar[str] = "GeographicImage"
    class_model_uri: ClassVar[URIRef] = SIO.GeographicImage


class Phrase(LanguageEntity):
    """
    A phrase is a group of words functioning as a single unit in the syntax of a sentence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Phrase
    class_class_curie: ClassVar[str] = "sio:Phrase"
    class_name: ClassVar[str] = "Phrase"
    class_model_uri: ClassVar[URIRef] = SIO.Phrase


class PieChart(MereologicalChart):
    """
    A pie chart is a circular chart divided into sectors each of whose length is proportional to the quantity it
    represents.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PieChart
    class_class_curie: ClassVar[str] = "sio:PieChart"
    class_name: ClassVar[str] = "PieChart"
    class_model_uri: ClassVar[URIRef] = SIO.PieChart


class Placebo(HeterogeneousSubstance):
    """
    A placebo is a medically ineffectual treatment for a medical condition intended to deceive the recipient.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Placebo
    class_class_curie: ClassVar[str] = "sio:Placebo"
    class_name: ClassVar[str] = "Placebo"
    class_model_uri: ClassVar[URIRef] = SIO.Placebo


class PlatinumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PlatinumAtom
    class_class_curie: ClassVar[str] = "sio:PlatinumAtom"
    class_name: ClassVar[str] = "PlatinumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PlatinumAtom


class Plot(FigurePart):
    """
    A plot is a part of a figure that corresponds to the spatial region between the set of axes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Plot
    class_class_curie: ClassVar[str] = "sio:Plot"
    class_name: ClassVar[str] = "Plot"
    class_model_uri: ClassVar[URIRef] = SIO.Plot


class PlutoniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PlutoniumAtom
    class_class_curie: ClassVar[str] = "sio:PlutoniumAtom"
    class_name: ClassVar[str] = "PlutoniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PlutoniumAtom


class Point(GeometricEntity):
    """
    A point is a geometric entity that is located in a zero-dimensional spatial region and whose position is defined
    by its coordinates in some coordinate system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Point
    class_class_curie: ClassVar[str] = "sio:Point"
    class_name: ClassVar[str] = "Point"
    class_model_uri: ClassVar[URIRef] = SIO.Point


class 1DCartesianPoint(Point):
    """
    A 1D cartesian point is a point whose position is specified along a single dimension using Cartesian coordinates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["1DCartesianPoint"]
    class_class_curie: ClassVar[str] = "sio:1DCartesianPoint"
    class_name: ClassVar[str] = "1DCartesianPoint"
    class_model_uri: ClassVar[URIRef] = SIO.1DCartesianPoint


class 2DCartesianPoint(Point):
    """
    A 2D cartesian point is a point whose position is specified along two  dimensions using Cartesian coordinates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["2DCartesianPoint"]
    class_class_curie: ClassVar[str] = "sio:2DCartesianPoint"
    class_name: ClassVar[str] = "2DCartesianPoint"
    class_model_uri: ClassVar[URIRef] = SIO.2DCartesianPoint


class 3DCartesianPoint(Point):
    """
    A 3D cartesian point is a point whose position is specified along three  dimensions using Cartesian coordinates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["3DCartesianPoint"]
    class_class_curie: ClassVar[str] = "sio:3DCartesianPoint"
    class_name: ClassVar[str] = "3DCartesianPoint"
    class_model_uri: ClassVar[URIRef] = SIO.3DCartesianPoint


class DataPoint(Point):
    """
    A data point is a point that which corresponds to the projection of the values of measurement data against the
    axes of a statistical graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataPoint
    class_class_curie: ClassVar[str] = "sio:DataPoint"
    class_name: ClassVar[str] = "DataPoint"
    class_model_uri: ClassVar[URIRef] = SIO.DataPoint


class Node(Point):
    """
    a node or vertex is a point in a graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Node
    class_class_curie: ClassVar[str] = "sio:Node"
    class_name: ClassVar[str] = "Node"
    class_model_uri: ClassVar[URIRef] = SIO.Node


class Poison(Drug):
    """
    A poison is a drug that is harzardous or toxic to an organism when ingested at a certain quantity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Poison
    class_class_curie: ClassVar[str] = "sio:Poison"
    class_name: ClassVar[str] = "Poison"
    class_model_uri: ClassVar[URIRef] = SIO.Poison


class PoloniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PoloniumAtom
    class_class_curie: ClassVar[str] = "sio:PoloniumAtom"
    class_name: ClassVar[str] = "PoloniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PoloniumAtom


class Polygon(GeometricEntity):
    """
    A polygon is a planar entity that is bounded by a closed path or circuit, composed of a finite connected sequence3
    of straight line segments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Polygon
    class_class_curie: ClassVar[str] = "sio:Polygon"
    class_name: ClassVar[str] = "Polygon"
    class_model_uri: ClassVar[URIRef] = SIO.Polygon


class PolygonEdge(LineSegment):
    """
    A polygon edge is a line segment joining two polygon vertices.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolygonEdge
    class_class_curie: ClassVar[str] = "sio:PolygonEdge"
    class_name: ClassVar[str] = "PolygonEdge"
    class_model_uri: ClassVar[URIRef] = SIO.PolygonEdge


class PolygonVertex(Node):
    """
    A polygon vertex is a terminal point at which two polygon edges meet and are part of a polygon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolygonVertex
    class_class_curie: ClassVar[str] = "sio:PolygonVertex"
    class_name: ClassVar[str] = "PolygonVertex"
    class_model_uri: ClassVar[URIRef] = SIO.PolygonVertex


class PolygonalFace(GeometricEntity):
    """
    A polygonal face is a polygon bounded by a circuit of polygon edges, and includes the flat (plane) region inside
    the boundary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolygonalFace
    class_class_curie: ClassVar[str] = "sio:PolygonalFace"
    class_name: ClassVar[str] = "PolygonalFace"
    class_model_uri: ClassVar[URIRef] = SIO.PolygonalFace


class PolyhedralSkeleton(GeometricEntity):
    """
    A polyhedral skeleton is a collection of polygon edges.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolyhedralSkeleton
    class_class_curie: ClassVar[str] = "sio:PolyhedralSkeleton"
    class_name: ClassVar[str] = "PolyhedralSkeleton"
    class_model_uri: ClassVar[URIRef] = SIO.PolyhedralSkeleton


class PolyhedralSurface(GeometricEntity):
    """
    A polyhedral surface is composed of polygonal faces.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolyhedralSurface
    class_class_curie: ClassVar[str] = "sio:PolyhedralSurface"
    class_name: ClassVar[str] = "PolyhedralSurface"
    class_model_uri: ClassVar[URIRef] = SIO.PolyhedralSurface


class Polyline(GeometricEntity):
    """
    A polyline is a connected sequence of line segments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Polyline
    class_class_curie: ClassVar[str] = "sio:Polyline"
    class_name: ClassVar[str] = "Polyline"
    class_model_uri: ClassVar[URIRef] = SIO.Polyline


class Polymer(Molecule):
    """
    A polymer is a molecule composed of a connected set of monomeric residues.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Polymer
    class_class_curie: ClassVar[str] = "sio:Polymer"
    class_name: ClassVar[str] = "Polymer"
    class_model_uri: ClassVar[URIRef] = SIO.Polymer


class Polypeptide(AminoAcidPolymer):
    """
    A polypeptide is an organic polymer composed of amino acid residues, typically of less than 50 amino acids in
    length.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Polypeptide
    class_class_curie: ClassVar[str] = "sio:Polypeptide"
    class_name: ClassVar[str] = "Polypeptide"
    class_model_uri: ClassVar[URIRef] = SIO.Polypeptide


class PositionallyOrientedLine(Line):
    """
    A positionally oriented line is a line that is positioned against some axis of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PositionallyOrientedLine
    class_class_curie: ClassVar[str] = "sio:PositionallyOrientedLine"
    class_name: ClassVar[str] = "PositionallyOrientedLine"
    class_model_uri: ClassVar[URIRef] = SIO.PositionallyOrientedLine


class HorizontalLine(PositionallyOrientedLine):
    """
    A horizontal line is a line that is positionally oriented with the horizon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HorizontalLine
    class_class_curie: ClassVar[str] = "sio:HorizontalLine"
    class_name: ClassVar[str] = "HorizontalLine"
    class_model_uri: ClassVar[URIRef] = SIO.HorizontalLine


class PositiveNucleicAcidStrand(NucleicAcidStrand):
    """
    The positive nucleic acid strand refers to the strand that is to be read 5' to 3'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PositiveNucleicAcidStrand
    class_class_curie: ClassVar[str] = "sio:PositiveNucleicAcidStrand"
    class_name: ClassVar[str] = "PositiveNucleicAcidStrand"
    class_model_uri: ClassVar[URIRef] = SIO.PositiveNucleicAcidStrand


class PotassiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PotassiumAtom
    class_class_curie: ClassVar[str] = "sio:PotassiumAtom"
    class_name: ClassVar[str] = "PotassiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PotassiumAtom


class PraseodymiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PraseodymiumAtom
    class_class_curie: ClassVar[str] = "sio:PraseodymiumAtom"
    class_name: ClassVar[str] = "PraseodymiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PraseodymiumAtom


class PrimaryCategoryAxis(CategoryAxis):
    """
    A primary category axis is a category axis that either defines the sole value range or holds the larger set of
    categorical values specified by the secondary category axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PrimaryCategoryAxis
    class_class_curie: ClassVar[str] = "sio:PrimaryCategoryAxis"
    class_name: ClassVar[str] = "PrimaryCategoryAxis"
    class_model_uri: ClassVar[URIRef] = SIO.PrimaryCategoryAxis


class PrimaryDatabaseKey(DatabaseKey):
    """
    A primary database key is a database key that identifies every row of a table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PrimaryDatabaseKey
    class_class_curie: ClassVar[str] = "sio:PrimaryDatabaseKey"
    class_name: ClassVar[str] = "PrimaryDatabaseKey"
    class_model_uri: ClassVar[URIRef] = SIO.PrimaryDatabaseKey


class Primer(YAMLRoot):
    """
    A primer is a nucleic acid that enables the synthesis of a complement strand of DNA by binding to it and acting as
    a point of transcription initiation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Primer
    class_class_curie: ClassVar[str] = "sio:Primer"
    class_name: ClassVar[str] = "Primer"
    class_model_uri: ClassVar[URIRef] = SIO.Primer


class DeoxyribonucleicAcidPrimer(Primer):
    """
    A deoxyribonucleic acid primer is a deoxyribonucleic acid that enables the synthesis of a complement strand of DNA
    by binding to it and acting as a point of transcription initiation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcidPrimer
    class_class_curie: ClassVar[str] = "sio:DeoxyribonucleicAcidPrimer"
    class_name: ClassVar[str] = "DeoxyribonucleicAcidPrimer"
    class_model_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcidPrimer


@dataclass
class Process(Entity):
    """
    A process is an entity that is identifiable only through the unfolding of time, has temporal parts, and unless
    otherwise specified/predicted, cannot be identified from any instant of time in which it exists.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Process
    class_class_curie: ClassVar[str] = "sio:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = SIO.Process

    hasParticipant: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasParticipant is not None and not isinstance(self.hasParticipant, Entity):
            self.hasParticipant = Entity(**as_dict(self.hasParticipant))

        super().__post_init__(**kwargs)


class Behaviour(Process):
    """
    Behaviour is the set of actions and mannerisms made by systems (biological or otherwise) in response to stimuli or
    inputs, whether internal or external, conscious or subconscious, overt or covert, and voluntary or involuntary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Behaviour
    class_class_curie: ClassVar[str] = "sio:Behaviour"
    class_name: ClassVar[str] = "Behaviour"
    class_model_uri: ClassVar[URIRef] = SIO.Behaviour


class Emotion(Behaviour):
    """
    An emotion is a process (experience) that arises internally or from an involuntary physiological response to a
    stimulus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Emotion
    class_class_curie: ClassVar[str] = "sio:Emotion"
    class_name: ClassVar[str] = "Emotion"
    class_model_uri: ClassVar[URIRef] = SIO.Emotion


class Indifference(Emotion):
    """
    indifference is an emotion characterized by lack of interest, concern, or sympathy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Indifference
    class_class_curie: ClassVar[str] = "sio:Indifference"
    class_name: ClassVar[str] = "Indifference"
    class_model_uri: ClassVar[URIRef] = SIO.Indifference


class Apathy(Indifference):
    """
    apathy is an emotion characterized by lack of interest, enthusiasm, or concern.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Apathy
    class_class_curie: ClassVar[str] = "sio:Apathy"
    class_name: ClassVar[str] = "Apathy"
    class_model_uri: ClassVar[URIRef] = SIO.Apathy


class Interacting(Process):
    """
    interacting is a process characterized by the interaction between two or more entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Interacting
    class_class_curie: ClassVar[str] = "sio:Interacting"
    class_name: ClassVar[str] = "Interacting"
    class_model_uri: ClassVar[URIRef] = SIO.Interacting


class ChemicalInteraction(Interacting):
    """
    A chemical interaction is a biochemical process in which chemical entities interact through some set of attractive
    forces.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalInteraction
    class_class_curie: ClassVar[str] = "sio:ChemicalInteraction"
    class_name: ClassVar[str] = "ChemicalInteraction"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalInteraction


class ChemicalEffect(ChemicalInteraction):
    """
    A chemical effect is a chemical interaction in which a chemical elicits a marked characteristic of a biological
    system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalEffect
    class_class_curie: ClassVar[str] = "sio:ChemicalEffect"
    class_name: ClassVar[str] = "ChemicalEffect"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalEffect


class ChemicalExposure(ChemicalInteraction):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalExposure
    class_class_curie: ClassVar[str] = "sio:ChemicalExposure"
    class_name: ClassVar[str] = "ChemicalExposure"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalExposure


class ChemicalReaction(ChemicalInteraction):
    """
    A chemical reaction is a process that leads to the transformation of one set of chemical substances to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalReaction
    class_class_curie: ClassVar[str] = "sio:ChemicalReaction"
    class_name: ClassVar[str] = "ChemicalReaction"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalReaction


class Acid-baseReaction(ChemicalReaction):
    """
    An acid-base reaction is a chemical reaction between an acid and a base.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Acid-baseReaction"]
    class_class_curie: ClassVar[str] = "sio:Acid-baseReaction"
    class_name: ClassVar[str] = "Acid-baseReaction"
    class_model_uri: ClassVar[URIRef] = SIO.Acid-baseReaction


class CatalyzedReaction(ChemicalReaction):
    """
    A catalyzed reaction is a chemical reaction that is facilitated by a catalyst.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CatalyzedReaction
    class_class_curie: ClassVar[str] = "sio:CatalyzedReaction"
    class_name: ClassVar[str] = "CatalyzedReaction"
    class_model_uri: ClassVar[URIRef] = SIO.CatalyzedReaction


class BiochemicalReaction(CatalyzedReaction):
    """
    A biochemical reaction is a biochemical process that involves the conversion of at least one chemical participant
    (target) into another (product) by an enzyme (agent).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiochemicalReaction
    class_class_curie: ClassVar[str] = "sio:BiochemicalReaction"
    class_name: ClassVar[str] = "BiochemicalReaction"
    class_model_uri: ClassVar[URIRef] = SIO.BiochemicalReaction


class Communicating(Interacting):
    """
    communicating is the process of conveying information through the exchange of thoughts, messages, or information,
    as by speech, visuals, signals, writing, or behaviour.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Communicating
    class_class_curie: ClassVar[str] = "sio:Communicating"
    class_name: ClassVar[str] = "Communicating"
    class_model_uri: ClassVar[URIRef] = SIO.Communicating


class Comparing(Interacting):
    """
    comparing is the process of examining a set of objects and determining their equality or inequality based on one
    or more features.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Comparing
    class_class_curie: ClassVar[str] = "sio:Comparing"
    class_name: ClassVar[str] = "Comparing"
    class_model_uri: ClassVar[URIRef] = SIO.Comparing


class Conversing(Communicating):
    """
    conversing a form of interactive, spontaneous communication between two or more agents who are following rules of
    etiquette.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Conversing
    class_class_curie: ClassVar[str] = "sio:Conversing"
    class_name: ClassVar[str] = "Conversing"
    class_model_uri: ClassVar[URIRef] = SIO.Conversing


class Creating(Interacting):
    """
    creating is the process in which an entity comes into existence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Creating
    class_class_curie: ClassVar[str] = "sio:Creating"
    class_name: ClassVar[str] = "Creating"
    class_model_uri: ClassVar[URIRef] = SIO.Creating


class Birthing(Creating):
    """
    birthing is the process by which a biological organism is brought into existence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Birthing
    class_class_curie: ClassVar[str] = "sio:Birthing"
    class_name: ClassVar[str] = "Birthing"
    class_model_uri: ClassVar[URIRef] = SIO.Birthing


class ChemicalSynthesis(Creating):
    """
    chemical synthesis is synthesis of a chemical entity from physical precursors through one or more chemical
    interactions or reactions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalSynthesis
    class_class_curie: ClassVar[str] = "sio:ChemicalSynthesis"
    class_name: ClassVar[str] = "ChemicalSynthesis"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalSynthesis


class Biosynthesis(ChemicalSynthesis):
    """
    biosynthesis is the synthesis of an organic compound in a living organism, usually aided by enzymes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Biosynthesis
    class_class_curie: ClassVar[str] = "sio:Biosynthesis"
    class_name: ClassVar[str] = "Biosynthesis"
    class_model_uri: ClassVar[URIRef] = SIO.Biosynthesis


class Destroying(Interacting):
    """
    destroying is a process in which something is broken down and/or ceases to exist.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Destroying
    class_class_curie: ClassVar[str] = "sio:Destroying"
    class_name: ClassVar[str] = "Destroying"
    class_model_uri: ClassVar[URIRef] = SIO.Destroying


class ChemicalDestruction(Destroying):
    """
    chemical destruction is destruction of a chemical entity to its chemical constituents through one ormore chemical
    interactions or reactions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalDestruction
    class_class_curie: ClassVar[str] = "sio:ChemicalDestruction"
    class_name: ClassVar[str] = "ChemicalDestruction"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalDestruction


class DecreasedChemicalDestruction(ChemicalDestruction):
    """
    decreased chemical destruction is a process in which there is a decrease in the amount of chemical destroyed
    relative to some reference process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedChemicalDestruction
    class_class_curie: ClassVar[str] = "sio:DecreasedChemicalDestruction"
    class_name: ClassVar[str] = "DecreasedChemicalDestruction"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedChemicalDestruction


class DrugDrugInteraction(ChemicalEffect):
    """
    A drug-drug interaction is an interaction in which two drugs interact in such a way to produce a non-additive
    biological response.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DrugDrugInteraction
    class_class_curie: ClassVar[str] = "sio:DrugDrugInteraction"
    class_name: ClassVar[str] = "DrugDrugInteraction"
    class_model_uri: ClassVar[URIRef] = SIO.DrugDrugInteraction


class Dying(Destroying):
    """
    dying is a process in which a biological entity ceases to exist.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Dying
    class_class_curie: ClassVar[str] = "sio:Dying"
    class_name: ClassVar[str] = "Dying"
    class_model_uri: ClassVar[URIRef] = SIO.Dying


class Evolving(Creating):
    """
    evolving is a process that elicits change across successive generations in the inherited characteristics of
    biological populations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Evolving
    class_class_curie: ClassVar[str] = "sio:Evolving"
    class_name: ClassVar[str] = "Evolving"
    class_model_uri: ClassVar[URIRef] = SIO.Evolving


class Gesturing(Communicating):
    """
    gesturing is a form of non-verbal communication in which visible bodily actions communicate particular messages,
    either in place of speech or together and in parallel with spoken words. Gestures include movement of the hands,
    face, or other parts of the body.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Gesturing
    class_class_curie: ClassVar[str] = "sio:Gesturing"
    class_name: ClassVar[str] = "Gesturing"
    class_model_uri: ClassVar[URIRef] = SIO.Gesturing


class IncreasedChemicalDestruction(ChemicalDestruction):
    """
    increased chemical destruction is a process in which there is an increase in the amount of chemical destroyed
    relative to some reference process
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedChemicalDestruction
    class_class_curie: ClassVar[str] = "sio:IncreasedChemicalDestruction"
    class_name: ClassVar[str] = "IncreasedChemicalDestruction"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedChemicalDestruction


class InorganicReaction(ChemicalReaction):
    """
    An inorganic reaction is a chemical reaction that involves the transformation of inorganic molecules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InorganicReaction
    class_class_curie: ClassVar[str] = "sio:InorganicReaction"
    class_name: ClassVar[str] = "InorganicReaction"
    class_model_uri: ClassVar[URIRef] = SIO.InorganicReaction


class DecompositionReaction(InorganicReaction):
    """
    A decomposition reaction is an inorganic reaction in which molecule is fragmented into submolecules or atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecompositionReaction
    class_class_curie: ClassVar[str] = "sio:DecompositionReaction"
    class_name: ClassVar[str] = "DecompositionReaction"
    class_model_uri: ClassVar[URIRef] = SIO.DecompositionReaction


class DisplacementReaction(InorganicReaction):
    """
    A displacement reaction is an inorganic reaction in which a elementary substance displaces and sets free a
    constituent atom from a molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DisplacementReaction
    class_class_curie: ClassVar[str] = "sio:DisplacementReaction"
    class_name: ClassVar[str] = "DisplacementReaction"
    class_model_uri: ClassVar[URIRef] = SIO.DisplacementReaction


class DoubleDisplacementReaction(DisplacementReaction):
    """
    A double displacement reaction is a displacement reaction in which two molecules swap ions, effectively displacing
    each other to form two new molecules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DoubleDisplacementReaction
    class_class_curie: ClassVar[str] = "sio:DoubleDisplacementReaction"
    class_name: ClassVar[str] = "DoubleDisplacementReaction"
    class_model_uri: ClassVar[URIRef] = SIO.DoubleDisplacementReaction


class IsomerizationReaction(ChemicalReaction):
    """
    An isomerization reaction is a chemical reaction in which a molecule is converted into its isomer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IsomerizationReaction
    class_class_curie: ClassVar[str] = "sio:IsomerizationReaction"
    class_name: ClassVar[str] = "IsomerizationReaction"
    class_model_uri: ClassVar[URIRef] = SIO.IsomerizationReaction


class Learning(Creating):
    """
    learning is the agentive process of acquiring knowledge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Learning
    class_class_curie: ClassVar[str] = "sio:Learning"
    class_name: ClassVar[str] = "Learning"
    class_model_uri: ClassVar[URIRef] = SIO.Learning


class Measuring(Interacting):
    """
    measuring is the process of determining the size, amount, or degree of (something) by using an instrument or
    device marked in standard units
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Measuring
    class_class_curie: ClassVar[str] = "sio:Measuring"
    class_name: ClassVar[str] = "Measuring"
    class_model_uri: ClassVar[URIRef] = SIO.Measuring


class Metabolism(ChemicalInteraction):
    """
    Metabolism is the set of chemical processes that occur within a living organism in order to maintain life.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Metabolism
    class_class_curie: ClassVar[str] = "sio:Metabolism"
    class_name: ClassVar[str] = "Metabolism"
    class_model_uri: ClassVar[URIRef] = SIO.Metabolism


class Anabolism(Metabolism):
    """
    Anabolism is the set of metabolic processes that construct larger chemical entities units from smaller chemical
    entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Anabolism
    class_class_curie: ClassVar[str] = "sio:Anabolism"
    class_name: ClassVar[str] = "Anabolism"
    class_model_uri: ClassVar[URIRef] = SIO.Anabolism


class Catabolism(Metabolism):
    """
    Anabolism is the set of metabolic processes that take apart larger chemical entities units into smaller chemical
    entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Catabolism
    class_class_curie: ClassVar[str] = "sio:Catabolism"
    class_name: ClassVar[str] = "Catabolism"
    class_model_uri: ClassVar[URIRef] = SIO.Catabolism


class Modifying(Interacting):
    """
    modifying is the process by which an entity gains or loses parts, qualities, roles, dispositions, functions, etc,
    but maintains their identity through these changes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Modifying
    class_class_curie: ClassVar[str] = "sio:Modifying"
    class_name: ClassVar[str] = "Modifying"
    class_model_uri: ClassVar[URIRef] = SIO.Modifying


class MolecularComplexDissociation(ChemicalDestruction):
    """
    molecular complex disassociation is the process of dissambly of a molecular complex into its constitutent parts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularComplexDissociation
    class_class_curie: ClassVar[str] = "sio:MolecularComplexDissociation"
    class_name: ClassVar[str] = "MolecularComplexDissociation"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularComplexDissociation


class MolecularComplexFormation(ChemicalSynthesis):
    """
    molecular complex formation is the process of forming a molecular complex from its constituent parts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularComplexFormation
    class_class_curie: ClassVar[str] = "sio:MolecularComplexFormation"
    class_name: ClassVar[str] = "MolecularComplexFormation"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularComplexFormation


class MolecularModification(ChemicalReaction):
    """
    Molecular modification is chemical alteration of a known and previously characterized lead compound for the
    purpose of enhancing its usefulness as a drug. This could mean enhancing its specificity for a particular body
    target site, increasing its potency, improving its rate and extent of absorption, modifying to advantage its time
    course in the body, reducing its toxicity, changing its physical or chemical properties (like solubility) to
    provide desired features.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularModification
    class_class_curie: ClassVar[str] = "sio:MolecularModification"
    class_name: ClassVar[str] = "MolecularModification"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularModification


class Movement(Process):
    """
    movement is the process in which an object is spatially displaced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Movement
    class_class_curie: ClassVar[str] = "sio:Movement"
    class_name: ClassVar[str] = "Movement"
    class_model_uri: ClassVar[URIRef] = SIO.Movement


class ActiveMovement(Movement):
    """
    active movement is the process in which an object is spatially displaced using some chemical energy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ActiveMovement
    class_class_curie: ClassVar[str] = "sio:ActiveMovement"
    class_name: ClassVar[str] = "ActiveMovement"
    class_model_uri: ClassVar[URIRef] = SIO.ActiveMovement


class Locomotion(ActiveMovement):
    """
    The self-propelled movement of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Locomotion
    class_class_curie: ClassVar[str] = "sio:Locomotion"
    class_name: ClassVar[str] = "Locomotion"
    class_model_uri: ClassVar[URIRef] = SIO.Locomotion


class NegativeEmotion(Emotion):
    """
    negative emotion is an emotion that does not feel good.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NegativeEmotion
    class_class_curie: ClassVar[str] = "sio:NegativeEmotion"
    class_name: ClassVar[str] = "NegativeEmotion"
    class_model_uri: ClassVar[URIRef] = SIO.NegativeEmotion


class Annoyance(NegativeEmotion):
    """
    Annoyance is an unpleasant emtion that is characterized by a abnormal or excessive sensitivity to some external
    stimulus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Annoyance
    class_class_curie: ClassVar[str] = "sio:Annoyance"
    class_name: ClassVar[str] = "Annoyance"
    class_model_uri: ClassVar[URIRef] = SIO.Annoyance


class Apprehension(NegativeEmotion):
    """
    apprehension is the negative emotion that something unpleasant will occur.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Apprehension
    class_class_curie: ClassVar[str] = "sio:Apprehension"
    class_name: ClassVar[str] = "Apprehension"
    class_model_uri: ClassVar[URIRef] = SIO.Apprehension


class Anxiety(Apprehension):
    """
    anxiety is an emotion charactersized by intense feeling of fear and concern coupled with a physical response.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Anxiety
    class_class_curie: ClassVar[str] = "sio:Anxiety"
    class_name: ClassVar[str] = "Anxiety"
    class_model_uri: ClassVar[URIRef] = SIO.Anxiety


class Angst(Anxiety):
    """
    angst is the intense feeling of apprehension, anxiety or inner turmoil.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Angst
    class_class_curie: ClassVar[str] = "sio:Angst"
    class_name: ClassVar[str] = "Angst"
    class_model_uri: ClassVar[URIRef] = SIO.Angst


class Boredom(NegativeEmotion):
    """
    boredom is the emotion experience by those not interested in their surroundings or available activities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Boredom
    class_class_curie: ClassVar[str] = "sio:Boredom"
    class_name: ClassVar[str] = "Boredom"
    class_model_uri: ClassVar[URIRef] = SIO.Boredom


class Disappointment(NegativeEmotion):
    """
    disappointment is the feeling of dissatisfaction that follows the failure of expectations or hopes to manifest.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Disappointment
    class_class_curie: ClassVar[str] = "sio:Disappointment"
    class_name: ClassVar[str] = "Disappointment"
    class_model_uri: ClassVar[URIRef] = SIO.Disappointment


class Discouragement(NegativeEmotion):
    """
    Discouragement is the emtion of having lost confidence or enthusiasm.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Discouragement
    class_class_curie: ClassVar[str] = "sio:Discouragement"
    class_name: ClassVar[str] = "Discouragement"
    class_model_uri: ClassVar[URIRef] = SIO.Discouragement


class Embarassment(NegativeEmotion):
    """
    Embarrassment is the emotion of intense discomfort with oneself, experienced upon having a socially unacceptable
    act or condition witnessed by or revealed to other.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Embarassment
    class_class_curie: ClassVar[str] = "sio:Embarassment"
    class_name: ClassVar[str] = "Embarassment"
    class_model_uri: ClassVar[URIRef] = SIO.Embarassment


class Envy(NegativeEmotion):
    """
    envy is an emotion that occurs when a person lacks another's (perceived) superior quality, achievement or
    possession and wishes that the other lacked it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Envy
    class_class_curie: ClassVar[str] = "sio:Envy"
    class_name: ClassVar[str] = "Envy"
    class_model_uri: ClassVar[URIRef] = SIO.Envy


class Fear(Apprehension):
    """
    Fear is a negative emotion induced by a perceived threat that induces one to hide or move quickly away from the
    location of the perceived threat.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Fear
    class_class_curie: ClassVar[str] = "sio:Fear"
    class_name: ClassVar[str] = "Fear"
    class_model_uri: ClassVar[URIRef] = SIO.Fear


class Dread(Fear):
    """
    dread is the instense negative emotion that induces fear and apprehension.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Dread
    class_class_curie: ClassVar[str] = "sio:Dread"
    class_name: ClassVar[str] = "Dread"
    class_model_uri: ClassVar[URIRef] = SIO.Dread


class Frustration(Annoyance):
    """
    Frustration is an emotion that arises from the perceived resistance to the fulfillment of individual will.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Frustration
    class_class_curie: ClassVar[str] = "sio:Frustration"
    class_name: ClassVar[str] = "Frustration"
    class_model_uri: ClassVar[URIRef] = SIO.Frustration


class Guilt(NegativeEmotion):
    """
    Guilt is the emotion borne from feeling responsible for the commission of an offense and arises out of public
    humiliation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Guilt
    class_class_curie: ClassVar[str] = "sio:Guilt"
    class_name: ClassVar[str] = "Guilt"
    class_model_uri: ClassVar[URIRef] = SIO.Guilt


class Hostility(NegativeEmotion):
    """
    Hostility is the intense negative emotion of being in conflict or opposition to someone or something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hostility
    class_class_curie: ClassVar[str] = "sio:Hostility"
    class_name: ClassVar[str] = "Hostility"
    class_model_uri: ClassVar[URIRef] = SIO.Hostility


class Disgust(Hostility):
    """
    Disgust is a feeling of revulsion or profound disapproval aroused by something unpleasant or offensive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Disgust
    class_class_curie: ClassVar[str] = "sio:Disgust"
    class_name: ClassVar[str] = "Disgust"
    class_model_uri: ClassVar[URIRef] = SIO.Disgust


class Anger(Disgust):
    """
    anger is disgust directed toward an equal status individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Anger
    class_class_curie: ClassVar[str] = "sio:Anger"
    class_name: ClassVar[str] = "Anger"
    class_model_uri: ClassVar[URIRef] = SIO.Anger


class Contempt(Disgust):
    """
    contempt is disgust towards a lower status individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Contempt
    class_class_curie: ClassVar[str] = "sio:Contempt"
    class_name: ClassVar[str] = "Contempt"
    class_model_uri: ClassVar[URIRef] = SIO.Contempt


class Hate(Disgust):
    """
    Hate is a deep and emotional extreme dislike, directed against a certain object or class of objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hate
    class_class_curie: ClassVar[str] = "sio:Hate"
    class_name: ClassVar[str] = "Hate"
    class_model_uri: ClassVar[URIRef] = SIO.Hate


class Hunger(NegativeEmotion):
    """
    hunger is the craving for food.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hunger
    class_class_curie: ClassVar[str] = "sio:Hunger"
    class_name: ClassVar[str] = "Hunger"
    class_model_uri: ClassVar[URIRef] = SIO.Hunger


class Hurt(NegativeEmotion):
    """
    hurt is an unpleasant feeling, emotion or sensation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hurt
    class_class_curie: ClassVar[str] = "sio:Hurt"
    class_name: ClassVar[str] = "Hurt"
    class_model_uri: ClassVar[URIRef] = SIO.Hurt


class Humiliation(Hurt):
    """
    Humiliation is the abasement of pride, which creates mortification or leads to a state of being humbled or reduced
    to lowliness or submission.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Humiliation
    class_class_curie: ClassVar[str] = "sio:Humiliation"
    class_name: ClassVar[str] = "Humiliation"
    class_model_uri: ClassVar[URIRef] = SIO.Humiliation


class Hysteria(NegativeEmotion):
    """
    Hysteria is an unmanageable emotion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hysteria
    class_class_curie: ClassVar[str] = "sio:Hysteria"
    class_name: ClassVar[str] = "Hysteria"
    class_model_uri: ClassVar[URIRef] = SIO.Hysteria


class Indecision(NegativeEmotion):
    """
    indecision is the emotion of being unable to choose between two or more possible courses of action.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Indecision
    class_class_curie: ClassVar[str] = "sio:Indecision"
    class_name: ClassVar[str] = "Indecision"
    class_model_uri: ClassVar[URIRef] = SIO.Indecision


class Irritability(NegativeEmotion):
    """
    irritability is the negative emotion of quick excitability to annoyance, impatience, or anger.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Irritability
    class_class_curie: ClassVar[str] = "sio:Irritability"
    class_name: ClassVar[str] = "Irritability"
    class_model_uri: ClassVar[URIRef] = SIO.Irritability


class Jealousy(Envy):
    """
    jealousy is an emotion and typically refers to the negative thoughts and feelings of insecurity, fear, and anxiety
    over an anticipated loss of something that the person values, particularly in reference to a human connection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Jealousy
    class_class_curie: ClassVar[str] = "sio:Jealousy"
    class_name: ClassVar[str] = "Jealousy"
    class_model_uri: ClassVar[URIRef] = SIO.Jealousy


class Loathing(Disgust):
    """
    loathing is an intense dislike or disgust.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Loathing
    class_class_curie: ClassVar[str] = "sio:Loathing"
    class_name: ClassVar[str] = "Loathing"
    class_model_uri: ClassVar[URIRef] = SIO.Loathing


class Loneliness(NegativeEmotion):
    """
    Loneliness is an unpleasant emotion in which a person feels a strong sense of emptiness, yearning distress and
    solitude resulting from inadequate quantity or quality of social relationships.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Loneliness
    class_class_curie: ClassVar[str] = "sio:Loneliness"
    class_name: ClassVar[str] = "Loneliness"
    class_model_uri: ClassVar[URIRef] = SIO.Loneliness


class Observing(Interacting):
    """
    observing is a process of passive interaction in which one entity makes note of attributes of one or more entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Observing
    class_class_curie: ClassVar[str] = "sio:Observing"
    class_name: ClassVar[str] = "Observing"
    class_model_uri: ClassVar[URIRef] = SIO.Observing


class OrganicReaction(ChemicalReaction):
    """
    An organic reaction is a chemical reaction involving at least one organic molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrganicReaction
    class_class_curie: ClassVar[str] = "sio:OrganicReaction"
    class_name: ClassVar[str] = "OrganicReaction"
    class_model_uri: ClassVar[URIRef] = SIO.OrganicReaction


class AdditionReaction(OrganicReaction):
    """
    An addition reaction is an organic reaction where two or more molecules combine to form a larger one. Addition
    reactions are limited to chemical compounds that have multiply-bonded atoms:
    * Molecules with carbon-carbon double bonds or triple bonds
    * Molecules with carbon - hetero double bonds like C=O or C=N
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AdditionReaction
    class_class_curie: ClassVar[str] = "sio:AdditionReaction"
    class_name: ClassVar[str] = "AdditionReaction"
    class_model_uri: ClassVar[URIRef] = SIO.AdditionReaction


class Non-polarAdditionReaction(AdditionReaction):
    """
    A non-polar addition reaction is an addition reaction involving non-polar residues.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Non-polarAdditionReaction"]
    class_class_curie: ClassVar[str] = "sio:Non-polarAdditionReaction"
    class_name: ClassVar[str] = "Non-polarAdditionReaction"
    class_model_uri: ClassVar[URIRef] = SIO.Non-polarAdditionReaction


class FreeRadicalAddition(Non-polarAdditionReaction):
    """
    A free radical addition is a non-polar addition reaction involving free radicals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FreeRadicalAddition
    class_class_curie: ClassVar[str] = "sio:FreeRadicalAddition"
    class_name: ClassVar[str] = "FreeRadicalAddition"
    class_model_uri: ClassVar[URIRef] = SIO.FreeRadicalAddition


class Pain(Hurt):
    """
    Pain is an unpleasant sensory and emotional experience associated with actual or potential tissue damage, or
    described in terms of such damage.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pain
    class_class_curie: ClassVar[str] = "sio:Pain"
    class_name: ClassVar[str] = "Pain"
    class_model_uri: ClassVar[URIRef] = SIO.Pain


class Panic(Fear):
    """
    Panic is a sudden emotion of fear which is so strong as to dominate or prevent reason and logical thinking,
    replacing it with overwhelming feelings of anxiety and frantic agitation consistent with an animalistic
    fight-or-flight reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Panic
    class_class_curie: ClassVar[str] = "sio:Panic"
    class_name: ClassVar[str] = "Panic"
    class_model_uri: ClassVar[URIRef] = SIO.Panic


class PassiveMovement(Movement):
    """
    passive movement is the process in which an object is spatially displaced without an expenditure of energy
    contained in molecular bonds.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PassiveMovement
    class_class_curie: ClassVar[str] = "sio:PassiveMovement"
    class_name: ClassVar[str] = "PassiveMovement"
    class_model_uri: ClassVar[URIRef] = SIO.PassiveMovement


class Diffusion(PassiveMovement):
    """
    diffusion is motion of particles at temperatures above absolute zero.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Diffusion
    class_class_curie: ClassVar[str] = "sio:Diffusion"
    class_name: ClassVar[str] = "Diffusion"
    class_model_uri: ClassVar[URIRef] = SIO.Diffusion


class BrownianMotion(Diffusion):
    """
    Brownian motion is the seemlingly random movement of particles suspended in a fluid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BrownianMotion
    class_class_curie: ClassVar[str] = "sio:BrownianMotion"
    class_name: ClassVar[str] = "BrownianMotion"
    class_model_uri: ClassVar[URIRef] = SIO.BrownianMotion


class Osmosis(Diffusion):
    """
    osmosis is the movement of water molecules through a selectively-permeable membrane down a water potential
    gradient.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Osmosis
    class_class_curie: ClassVar[str] = "sio:Osmosis"
    class_name: ClassVar[str] = "Osmosis"
    class_model_uri: ClassVar[URIRef] = SIO.Osmosis


class Perception(Observing):
    """
    perception is the organization, identification, and interpretation of sensory information in order to fabricate a
    mental representation through the process of transduction, which sensors in the body transform signals from the
    environment into encoded neural signals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Perception
    class_class_curie: ClassVar[str] = "sio:Perception"
    class_name: ClassVar[str] = "Perception"
    class_model_uri: ClassVar[URIRef] = SIO.Perception


class Pity(NegativeEmotion):
    """
    Pity is the emotion of sadness or sorrow for another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pity
    class_class_curie: ClassVar[str] = "sio:Pity"
    class_name: ClassVar[str] = "Pity"
    class_model_uri: ClassVar[URIRef] = SIO.Pity


class Planning(Creating):
    """
    planning is the agentive process of developing a plan that specifies a set of actions in order to meet a set of
    goals or objectives.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Planning
    class_class_curie: ClassVar[str] = "sio:Planning"
    class_name: ClassVar[str] = "Planning"
    class_model_uri: ClassVar[URIRef] = SIO.Planning


class PolarAdditionReaction(AdditionReaction):
    """
    A polar addition reaction is an addition reaction involving polar residues.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolarAdditionReaction
    class_class_curie: ClassVar[str] = "sio:PolarAdditionReaction"
    class_name: ClassVar[str] = "PolarAdditionReaction"
    class_model_uri: ClassVar[URIRef] = SIO.PolarAdditionReaction


class ElectrophilicAdditionReaction(PolarAdditionReaction):
    """
    An electrophilic addition reaction is a polar addition reaction where a pi bond is removed by the creation of two
    new covalent bonds.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ElectrophilicAdditionReaction
    class_class_curie: ClassVar[str] = "sio:ElectrophilicAdditionReaction"
    class_name: ClassVar[str] = "ElectrophilicAdditionReaction"
    class_model_uri: ClassVar[URIRef] = SIO.ElectrophilicAdditionReaction


class NucleophilicAdditionReaction(PolarAdditionReaction):
    """
    A nucleophilic addition reaction is an addition reaction where a pi bond is removed by the creation of two new
    covalent bonds by the addition from a nucleophile.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NucleophilicAdditionReaction
    class_class_curie: ClassVar[str] = "sio:NucleophilicAdditionReaction"
    class_name: ClassVar[str] = "NucleophilicAdditionReaction"
    class_model_uri: ClassVar[URIRef] = SIO.NucleophilicAdditionReaction


class PositiveEmotion(Emotion):
    """
    A positive emotion is an emotion that feels good.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PositiveEmotion
    class_class_curie: ClassVar[str] = "sio:PositiveEmotion"
    class_name: ClassVar[str] = "PositiveEmotion"
    class_model_uri: ClassVar[URIRef] = SIO.PositiveEmotion


class Affection(PositiveEmotion):
    """
    affection is an emotion characterized with a feeling or type of love for another living thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Affection
    class_class_curie: ClassVar[str] = "sio:Affection"
    class_name: ClassVar[str] = "Affection"
    class_model_uri: ClassVar[URIRef] = SIO.Affection


class Arousal(PositiveEmotion):
    """
    arousal is an emotion characterized by state of reactive to stimuli. It involves the activation of the reticular
    activating system in the brain stem, the autonomic nervous system and the endocrine system, leading to increased
    heart rate and blood pressure and a condition of sensory alertness, mobility and readiness to respond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Arousal
    class_class_curie: ClassVar[str] = "sio:Arousal"
    class_name: ClassVar[str] = "Arousal"
    class_model_uri: ClassVar[URIRef] = SIO.Arousal


class Awe(PositiveEmotion):
    """
    awe is an emotion produced by that which is grand, sublime or powerful and is characterized by a combination of
    joy, fear and admiration/reverence/respect.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Awe
    class_class_curie: ClassVar[str] = "sio:Awe"
    class_name: ClassVar[str] = "Awe"
    class_model_uri: ClassVar[URIRef] = SIO.Awe


class Boldness(PositiveEmotion):
    """
    boldness is the trait of being willing to undertake things that involve risk or danger.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Boldness
    class_class_curie: ClassVar[str] = "sio:Boldness"
    class_name: ClassVar[str] = "Boldness"
    class_model_uri: ClassVar[URIRef] = SIO.Boldness


class Ecstasy(PositiveEmotion):
    """
    ecstacy is an emotion characterized by a heightened state of consciousness with total involvement of a subject.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ecstasy
    class_class_curie: ClassVar[str] = "sio:Ecstasy"
    class_name: ClassVar[str] = "Ecstasy"
    class_model_uri: ClassVar[URIRef] = SIO.Ecstasy


class Excitement(PositiveEmotion):
    """
    excitement is a positive emotion of feeling great enthusiasm and eagerness.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Excitement
    class_class_curie: ClassVar[str] = "sio:Excitement"
    class_name: ClassVar[str] = "Excitement"
    class_model_uri: ClassVar[URIRef] = SIO.Excitement


class Gratitude(PositiveEmotion):
    """
    Gratitude, thankfulness, gratefulness, or appreciation is a feeling, emotion or attitude in acknowledgment of a
    benefit that one has received or will receive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Gratitude
    class_class_curie: ClassVar[str] = "sio:Gratitude"
    class_name: ClassVar[str] = "Gratitude"
    class_model_uri: ClassVar[URIRef] = SIO.Gratitude


class Happiness(PositiveEmotion):
    """
    happiness is an emotion characterized by positive or pleasant emotions ranging from contentment to intense joy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Happiness
    class_class_curie: ClassVar[str] = "sio:Happiness"
    class_name: ClassVar[str] = "Happiness"
    class_model_uri: ClassVar[URIRef] = SIO.Happiness


class Contentment(Happiness):
    """
    contentment is an emotion characterized by acknowledgement and satisfaction of the current state of affairs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Contentment
    class_class_curie: ClassVar[str] = "sio:Contentment"
    class_name: ClassVar[str] = "Contentment"
    class_model_uri: ClassVar[URIRef] = SIO.Contentment


class Euphoria(Happiness):
    """
    euphoria is an emotion characterized by intense feelings of well-being, elation, happiness, ecstasy, excitement,
    and joy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Euphoria
    class_class_curie: ClassVar[str] = "sio:Euphoria"
    class_name: ClassVar[str] = "Euphoria"
    class_model_uri: ClassVar[URIRef] = SIO.Euphoria


class Hope(PositiveEmotion):
    """
    hope is an emotion of belief in a positive outcome related to events and circumstances in one's life.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hope
    class_class_curie: ClassVar[str] = "sio:Hope"
    class_name: ClassVar[str] = "Hope"
    class_model_uri: ClassVar[URIRef] = SIO.Hope


class Interest(PositiveEmotion):
    """
    interest is the emotion of wanting to know or learn about something or someone.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Interest
    class_class_curie: ClassVar[str] = "sio:Interest"
    class_name: ClassVar[str] = "Interest"
    class_model_uri: ClassVar[URIRef] = SIO.Interest


class Desire(Interest):
    """
    desire is a strong emotion of wanting to have something or wishing for something to happen.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Desire
    class_class_curie: ClassVar[str] = "sio:Desire"
    class_name: ClassVar[str] = "Desire"
    class_model_uri: ClassVar[URIRef] = SIO.Desire


class Curiosity(Desire):
    """
    curiosity is the strong desire to know or learn something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Curiosity
    class_class_curie: ClassVar[str] = "sio:Curiosity"
    class_name: ClassVar[str] = "Curiosity"
    class_model_uri: ClassVar[URIRef] = SIO.Curiosity


class Intent(Desire):
    """
    intent is a desire to realize a particular outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Intent
    class_class_curie: ClassVar[str] = "sio:Intent"
    class_name: ClassVar[str] = "Intent"
    class_model_uri: ClassVar[URIRef] = SIO.Intent


class Joy(Happiness):
    """
    joy is an emotion of intense happiness.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Joy
    class_class_curie: ClassVar[str] = "sio:Joy"
    class_name: ClassVar[str] = "Joy"
    class_model_uri: ClassVar[URIRef] = SIO.Joy


class Love(PositiveEmotion):
    """
    love is an emotion of a strong affection and personal attachment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Love
    class_class_curie: ClassVar[str] = "sio:Love"
    class_name: ClassVar[str] = "Love"
    class_model_uri: ClassVar[URIRef] = SIO.Love


class Lust(Desire):
    """
    lust is the strong desire for sex.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Lust
    class_class_curie: ClassVar[str] = "sio:Lust"
    class_name: ClassVar[str] = "Lust"
    class_model_uri: ClassVar[URIRef] = SIO.Lust


class Passion(Desire):
    """
    passion is the intense desire for something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Passion
    class_class_curie: ClassVar[str] = "sio:Passion"
    class_name: ClassVar[str] = "Passion"
    class_model_uri: ClassVar[URIRef] = SIO.Passion


class Pleasure(Happiness):
    """
    pleasure is an emotion of happy satisfaction and enjoyment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pleasure
    class_class_curie: ClassVar[str] = "sio:Pleasure"
    class_name: ClassVar[str] = "Pleasure"
    class_model_uri: ClassVar[URIRef] = SIO.Pleasure


class Predicting(Creating):
    """
    predicting is the process of formulating a proposition about a state of affairs which might be realized in the
    future.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Predicting
    class_class_curie: ClassVar[str] = "sio:Predicting"
    class_name: ClassVar[str] = "Predicting"
    class_model_uri: ClassVar[URIRef] = SIO.Predicting


class Procedure(Process):
    """
    A procedure is a process that attempts to achieve one or more objectives by following an established set of
    actions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Procedure
    class_class_curie: ClassVar[str] = "sio:Procedure"
    class_name: ClassVar[str] = "Procedure"
    class_model_uri: ClassVar[URIRef] = SIO.Procedure


class Assay(Procedure):
    """
    An assay is an investigative (analytic) procedure in laboratory medicine, pharmacology, environmental biology, and
    molecular biology for qualitatively assessing or quantitatively measuring the presence or amount or the functional
    activity of a target entity (the analyte) which can be a drug or biochemical substance or a cell in an organism or
    organic sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Assay
    class_class_curie: ClassVar[str] = "sio:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = SIO.Assay


class InformationProcessing(Procedure):
    """
    information processing is a process that involves the generation or use of information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationProcessing
    class_class_curie: ClassVar[str] = "sio:InformationProcessing"
    class_name: ClassVar[str] = "InformationProcessing"
    class_model_uri: ClassVar[URIRef] = SIO.InformationProcessing


class DataAnalysis(InformationProcessing):
    """
    data analysis is a process of inspecting, cleaning, transforming, and modeling data with the goal of highlighting
    useful information, suggesting conclusions, and supporting decision making.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataAnalysis
    class_class_curie: ClassVar[str] = "sio:DataAnalysis"
    class_name: ClassVar[str] = "DataAnalysis"
    class_model_uri: ClassVar[URIRef] = SIO.DataAnalysis


class DataCollection(InformationProcessing):
    """
    data collection is the process of acquiring information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataCollection
    class_class_curie: ClassVar[str] = "sio:DataCollection"
    class_name: ClassVar[str] = "DataCollection"
    class_model_uri: ClassVar[URIRef] = SIO.DataCollection


class DataTransformation(InformationProcessing):
    """
    data transformation is the process of applying an algorithmic procedure to some input data and producing some
    output data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataTransformation
    class_class_curie: ClassVar[str] = "sio:DataTransformation"
    class_name: ClassVar[str] = "DataTransformation"
    class_model_uri: ClassVar[URIRef] = SIO.DataTransformation


class InformationTranslation(InformationProcessing):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationTranslation
    class_class_curie: ClassVar[str] = "sio:InformationTranslation"
    class_name: ClassVar[str] = "InformationTranslation"
    class_model_uri: ClassVar[URIRef] = SIO.InformationTranslation


class InformationDecoding(InformationTranslation):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationDecoding
    class_class_curie: ClassVar[str] = "sio:InformationDecoding"
    class_name: ClassVar[str] = "InformationDecoding"
    class_model_uri: ClassVar[URIRef] = SIO.InformationDecoding


class InformationEncoding(InformationTranslation):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationEncoding
    class_class_curie: ClassVar[str] = "sio:InformationEncoding"
    class_name: ClassVar[str] = "InformationEncoding"
    class_model_uri: ClassVar[URIRef] = SIO.InformationEncoding


class Investigation(Procedure):
    """
    investigation is the process of carrying out a plan or procedure so as to discover facts or information about the
    object of study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Investigation
    class_class_curie: ClassVar[str] = "sio:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = SIO.Investigation


class Experiment(Investigation):
    """
    An experiment is an investigation that has the goal of verifying, falsifying, or establishing the validity of a
    hypothesis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Experiment
    class_class_curie: ClassVar[str] = "sio:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = SIO.Experiment


class InterventionStudy(Experiment):
    """
    An intervention study has the objective of improving the condition of an individual or a group of individuals, and
    demonstrates the magnitude of that capability by comparing it to a control group.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InterventionStudy
    class_class_curie: ClassVar[str] = "sio:InterventionStudy"
    class_name: ClassVar[str] = "InterventionStudy"
    class_model_uri: ClassVar[URIRef] = SIO.InterventionStudy


class ClinicalTrial(InterventionStudy):
    """
    A clinical trial is an intervention trial to determine the safety and efficacy of medical interventions (e.g.,
    drugs, diagnostics, devices, therapy protocols).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ClinicalTrial
    class_class_curie: ClassVar[str] = "sio:ClinicalTrial"
    class_name: ClassVar[str] = "ClinicalTrial"
    class_model_uri: ClassVar[URIRef] = SIO.ClinicalTrial


class LiteratureCuration(InformationProcessing):
    """
    literature curation is the process of an agent selecting and extracting terms and phrases from a document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LiteratureCuration
    class_class_curie: ClassVar[str] = "sio:LiteratureCuration"
    class_name: ClassVar[str] = "LiteratureCuration"
    class_model_uri: ClassVar[URIRef] = SIO.LiteratureCuration


class MassSpectrometryExperiment(Experiment):
    """
    A mass spectrometry experiment is an experiment that involves the use of a mass spectrometer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MassSpectrometryExperiment
    class_class_curie: ClassVar[str] = "sio:MassSpectrometryExperiment"
    class_name: ClassVar[str] = "MassSpectrometryExperiment"
    class_model_uri: ClassVar[URIRef] = SIO.MassSpectrometryExperiment


class MedicalProcedure(Procedure):
    """
    A medical procedure is a procedure to identify, examine, alleviate or eliminate an undesirable biological disease
    or disorder.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalProcedure
    class_class_curie: ClassVar[str] = "sio:MedicalProcedure"
    class_name: ClassVar[str] = "MedicalProcedure"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalProcedure


class DiagnosticTest(MedicalProcedure):
    """
    A diagnostic test is a procedure performed to confirm, or determine the presence of disease in an individual
    suspected of having the disease, usually following the report of symptoms, or based on the results of other
    medical tests.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DiagnosticTest
    class_class_curie: ClassVar[str] = "sio:DiagnosticTest"
    class_name: ClassVar[str] = "DiagnosticTest"
    class_model_uri: ClassVar[URIRef] = SIO.DiagnosticTest


class DifferentialDiagnosis(MedicalProcedure):
    """
    A differential diagnosis (sometimes abbreviated DDx, ddx, DD, D/Dx, or ΔΔ) is a systematic diagnostic method used
    to identify the presence of an entity where multiple alternatives are possible (and the process may be termed
    differential diagnostic procedure), and may also refer to any of the included candidate alternatives (which may
    also be termed candidate condition).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DifferentialDiagnosis
    class_class_curie: ClassVar[str] = "sio:DifferentialDiagnosis"
    class_name: ClassVar[str] = "DifferentialDiagnosis"
    class_model_uri: ClassVar[URIRef] = SIO.DifferentialDiagnosis


class MedicalDiagnosis(MedicalProcedure):
    """
    A medical diagnosis (often simply termed diagnosis) refers to the process of attempting to determine or identify a
    possible disease or disorder.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalDiagnosis
    class_class_curie: ClassVar[str] = "sio:MedicalDiagnosis"
    class_name: ClassVar[str] = "MedicalDiagnosis"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalDiagnosis


class MedicalIntervention(MedicalProcedure):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalIntervention
    class_class_curie: ClassVar[str] = "sio:MedicalIntervention"
    class_name: ClassVar[str] = "MedicalIntervention"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalIntervention


class MedicalScreening(MedicalProcedure):
    """
    A medical screening is a medical test or series used to detect or predict the presence of disease in individuals
    at risk for disease within a defined group, such as a population, family, or workforce
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalScreening
    class_class_curie: ClassVar[str] = "sio:MedicalScreening"
    class_name: ClassVar[str] = "MedicalScreening"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalScreening


class MicroarrayExperiment(Experiment):
    """
    A microarray experiment is an experiment that involves a microarray device to measure the expression of one or
    more genes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MicroarrayExperiment
    class_class_curie: ClassVar[str] = "sio:MicroarrayExperiment"
    class_name: ClassVar[str] = "MicroarrayExperiment"
    class_model_uri: ClassVar[URIRef] = SIO.MicroarrayExperiment


class ObservationalStudy(Experiment):
    """
    observational study draws inferences about the possible effect of a treatment on subjects, where the assignment of
    subjects into a treated group versus a control group is outside the control of the investigator
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ObservationalStudy
    class_class_curie: ClassVar[str] = "sio:ObservationalStudy"
    class_name: ClassVar[str] = "ObservationalStudy"
    class_model_uri: ClassVar[URIRef] = SIO.ObservationalStudy


class ControlledObservationalCohortStudy(ObservationalStudy):
    """
    In a controlled observational cohort study, two groups of subjects are selected from two populations that are
    thought to differ in only one characteristic. The groups of subjects are studied for a specific period and
    contrasted at the end of the study period.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ControlledObservationalCohortStudy
    class_class_curie: ClassVar[str] = "sio:ControlledObservationalCohortStudy"
    class_name: ClassVar[str] = "ControlledObservationalCohortStudy"
    class_model_uri: ClassVar[URIRef] = SIO.ControlledObservationalCohortStudy


class ParameterizedDataTransformation(DataTransformation):
    """
    A parameterized data transformation is a data transformation whose behaviour may be modified by one or more
    parameters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ParameterizedDataTransformation
    class_class_curie: ClassVar[str] = "sio:ParameterizedDataTransformation"
    class_name: ClassVar[str] = "ParameterizedDataTransformation"
    class_model_uri: ClassVar[URIRef] = SIO.ParameterizedDataTransformation


class Product(Molecule):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Product
    class_class_curie: ClassVar[str] = "sio:Product"
    class_name: ClassVar[str] = "Product"
    class_model_uri: ClassVar[URIRef] = SIO.Product


class PromethiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PromethiumAtom
    class_class_curie: ClassVar[str] = "sio:PromethiumAtom"
    class_name: ClassVar[str] = "PromethiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.PromethiumAtom


class Proposition(Description):
    """
    A proposition is a sentence expressing something true or false.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Proposition
    class_class_curie: ClassVar[str] = "sio:Proposition"
    class_name: ClassVar[str] = "Proposition"
    class_model_uri: ClassVar[URIRef] = SIO.Proposition


class Argument(Proposition):
    """
    An argument is a set of one or more declarative sentences (or propositions) known as the premises along with
    another declarative sentence (or proposition) known as the conclusion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Argument
    class_class_curie: ClassVar[str] = "sio:Argument"
    class_name: ClassVar[str] = "Argument"
    class_model_uri: ClassVar[URIRef] = SIO.Argument


class Belief(Proposition):
    """
    A belief is a proposition that is believed to be true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Belief
    class_class_curie: ClassVar[str] = "sio:Belief"
    class_name: ClassVar[str] = "Belief"
    class_model_uri: ClassVar[URIRef] = SIO.Belief


class Comment(Proposition):
    """
    A comment is a verbal or written remark often related to an added piece of information, or an observation or
    statement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Comment
    class_class_curie: ClassVar[str] = "sio:Comment"
    class_name: ClassVar[str] = "Comment"
    class_model_uri: ClassVar[URIRef] = SIO.Comment


class Conclusion(Proposition):
    """
    A conclusion is a proposition which is reached after considering the evidence, arguments or premises.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Conclusion
    class_class_curie: ClassVar[str] = "sio:Conclusion"
    class_name: ClassVar[str] = "Conclusion"
    class_model_uri: ClassVar[URIRef] = SIO.Conclusion


class DeductiveArgument(Argument):
    """
    A deductive argument is an argument that asserts that the truth of the conclusion is a logical consequence of the
    premises.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DeductiveArgument
    class_class_curie: ClassVar[str] = "sio:DeductiveArgument"
    class_name: ClassVar[str] = "DeductiveArgument"
    class_model_uri: ClassVar[URIRef] = SIO.DeductiveArgument


class Diagnosis(Conclusion):
    """
    A diagnosis is the result of a medical investigation to identify a disorder from its signs and symptoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Diagnosis
    class_class_curie: ClassVar[str] = "sio:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = SIO.Diagnosis


class Evidence(Proposition):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Evidence
    class_class_curie: ClassVar[str] = "sio:Evidence"
    class_name: ClassVar[str] = "Evidence"
    class_model_uri: ClassVar[URIRef] = SIO.Evidence


class Hypothesis(Proposition):
    """
    A hypothesis is a proposed explanation for a phenomenon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hypothesis
    class_class_curie: ClassVar[str] = "sio:Hypothesis"
    class_name: ClassVar[str] = "Hypothesis"
    class_model_uri: ClassVar[URIRef] = SIO.Hypothesis


class Idea(Proposition):
    """
    An idea is a proposition about some object of conceptual thought.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Idea
    class_class_curie: ClassVar[str] = "sio:Idea"
    class_name: ClassVar[str] = "Idea"
    class_model_uri: ClassVar[URIRef] = SIO.Idea


class InductiveArgument(Argument):
    """
    An inductive argument is an argument that asserts that the truth of the conclusion is supported by the premises.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InductiveArgument
    class_class_curie: ClassVar[str] = "sio:InductiveArgument"
    class_name: ClassVar[str] = "InductiveArgument"
    class_model_uri: ClassVar[URIRef] = SIO.InductiveArgument


class InvalidArgument(Argument):
    """
    An invalid argument is an argument where the truth of the conclusion is false because it is not a logical
    consequence of the premises.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InvalidArgument
    class_class_curie: ClassVar[str] = "sio:InvalidArgument"
    class_name: ClassVar[str] = "InvalidArgument"
    class_model_uri: ClassVar[URIRef] = SIO.InvalidArgument


class Justification(Proposition):
    """
    A justification is a proposition that defends, explains or excuses some argument.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Justification
    class_class_curie: ClassVar[str] = "sio:Justification"
    class_name: ClassVar[str] = "Justification"
    class_model_uri: ClassVar[URIRef] = SIO.Justification


class Objective(Proposition):
    """
    An objective is a proposition that indicates a planned or anticipated outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Objective
    class_class_curie: ClassVar[str] = "sio:Objective"
    class_name: ClassVar[str] = "Objective"
    class_model_uri: ClassVar[URIRef] = SIO.Objective


class Opinion(Belief):
    """
    An opinion is a belief that is the result of emotion or interpretation of facts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Opinion
    class_class_curie: ClassVar[str] = "sio:Opinion"
    class_name: ClassVar[str] = "Opinion"
    class_model_uri: ClassVar[URIRef] = SIO.Opinion


class DiagnosticOpinion(Opinion):
    """
    A diagnostic opinion is an opinion resulting from a medical diagnostic procedure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DiagnosticOpinion
    class_class_curie: ClassVar[str] = "sio:DiagnosticOpinion"
    class_name: ClassVar[str] = "DiagnosticOpinion"
    class_model_uri: ClassVar[URIRef] = SIO.DiagnosticOpinion


class Premise(Proposition):
    """
    A premise is a proposition of an argument from which the conclusion is drawn.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Premise
    class_class_curie: ClassVar[str] = "sio:Premise"
    class_name: ClassVar[str] = "Premise"
    class_model_uri: ClassVar[URIRef] = SIO.Premise


class Prognosis(Proposition):
    """
    A prognosis is a proposition about the likely course of a disease, the chance of recovery or recurrence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Prognosis
    class_class_curie: ClassVar[str] = "sio:Prognosis"
    class_name: ClassVar[str] = "Prognosis"
    class_model_uri: ClassVar[URIRef] = SIO.Prognosis


class ProtactiniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProtactiniumAtom
    class_class_curie: ClassVar[str] = "sio:ProtactiniumAtom"
    class_name: ClassVar[str] = "ProtactiniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ProtactiniumAtom


class Protein(AminoAcidPolymer):
    """
    A protein is an organic polymer that is composed of one or more linear polymers of amino acids.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Protein
    class_class_curie: ClassVar[str] = "sio:Protein"
    class_name: ClassVar[str] = "Protein"
    class_model_uri: ClassVar[URIRef] = SIO.Protein


class Enzyme(Protein):
    """
    An enzyme is a protein or protein complex that realizes its disposition to covalently modify some molecule during
    a chemical reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Enzyme
    class_class_curie: ClassVar[str] = "sio:Enzyme"
    class_name: ClassVar[str] = "Enzyme"
    class_model_uri: ClassVar[URIRef] = SIO.Enzyme


class ProteinComplex(MolecularComplex):
    """
    A protein complex is a molecular complex composed of at least two polypeptide chains.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinComplex
    class_class_curie: ClassVar[str] = "sio:ProteinComplex"
    class_name: ClassVar[str] = "ProteinComplex"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinComplex


class Antibody(ProteinComplex):
    """
    An antibody (also known as immunoglobulins, abbreviated Ig) are gamma globulin proteins that are used by the
    immune system to identify and neutralize foreign objects. They are typically made of two large heavy chains and
    two small light chains.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Antibody
    class_class_curie: ClassVar[str] = "sio:Antibody"
    class_name: ClassVar[str] = "Antibody"
    class_model_uri: ClassVar[URIRef] = SIO.Antibody


class Quadrilateral(Polygon):
    """
    A quadrilateral is a polygon with composed of four points and four line segments, in which each point is fully
    connected to two other points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Quadrilateral
    class_class_curie: ClassVar[str] = "sio:Quadrilateral"
    class_name: ClassVar[str] = "Quadrilateral"
    class_model_uri: ClassVar[URIRef] = SIO.Quadrilateral


@dataclass
class Quality(Attribute):
    """
    A quality is an attribute that is intrinsically associated with its bearer (or its parts), but whose
    presence/absence and observed/measured value may vary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Quality
    class_class_curie: ClassVar[str] = "sio:Quality"
    class_name: ClassVar[str] = "Quality"
    class_model_uri: ClassVar[URIRef] = SIO.Quality

    isQualityOf: Optional[Union[dict, Entity]] = None
    isBaseFor: Optional[Union[dict, "RealizableEntity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isQualityOf is not None and not isinstance(self.isQualityOf, Entity):
            self.isQualityOf = Entity(**as_dict(self.isQualityOf))

        if self.isBaseFor is not None and not isinstance(self.isBaseFor, RealizableEntity):
            self.isBaseFor = RealizableEntity(**as_dict(self.isBaseFor))

        super().__post_init__(**kwargs)


class AssertionalQualifier(Quality):
    """
    An assertional qualifier is the quality of affirmation, either being positive or negative.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AssertionalQualifier
    class_class_curie: ClassVar[str] = "sio:AssertionalQualifier"
    class_name: ClassVar[str] = "AssertionalQualifier"
    class_model_uri: ClassVar[URIRef] = SIO.AssertionalQualifier


class ExistenceQuality(Quality):
    """
    existence quality is the quality of an entity that describe in what environment it is known to exist.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ExistenceQuality
    class_class_curie: ClassVar[str] = "sio:ExistenceQuality"
    class_name: ClassVar[str] = "ExistenceQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ExistenceQuality


class Hypothetical(ExistenceQuality):
    """
    hypothetical is the quality of an entity that is conjectured to exist.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hypothetical
    class_class_curie: ClassVar[str] = "sio:Hypothetical"
    class_name: ClassVar[str] = "Hypothetical"
    class_model_uri: ClassVar[URIRef] = SIO.Hypothetical


class Fictional(Hypothetical):
    """
    fictional is the quality of an entity that exists only in a creative work of fiction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Fictional
    class_class_curie: ClassVar[str] = "sio:Fictional"
    class_name: ClassVar[str] = "Fictional"
    class_model_uri: ClassVar[URIRef] = SIO.Fictional


class InformationalQuality(Quality):
    """
    An informational quality is a quality that pertains to information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationalQuality
    class_class_curie: ClassVar[str] = "sio:InformationalQuality"
    class_name: ClassVar[str] = "InformationalQuality"
    class_model_uri: ClassVar[URIRef] = SIO.InformationalQuality


class AgreementQuality(InformationalQuality):
    """
    agreement quality is a quality that exhibits the degree of consensus for some set of assertions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AgreementQuality
    class_class_curie: ClassVar[str] = "sio:AgreementQuality"
    class_name: ClassVar[str] = "AgreementQuality"
    class_model_uri: ClassVar[URIRef] = SIO.AgreementQuality


class Agreement(AgreementQuality):
    """
    agreement is the result of consensus decision making when members of the group agree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Agreement
    class_class_curie: ClassVar[str] = "sio:Agreement"
    class_name: ClassVar[str] = "Agreement"
    class_model_uri: ClassVar[URIRef] = SIO.Agreement


class Consensus(Agreement):
    """
    consensus is an acceptable resolution, one that can be supported, even if not the preferred outcome for each
    individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Consensus
    class_class_curie: ClassVar[str] = "sio:Consensus"
    class_name: ClassVar[str] = "Consensus"
    class_model_uri: ClassVar[URIRef] = SIO.Consensus


class Disagreement(AgreementQuality):
    """
    agreement is the result of consensus decision making when members of the group do not all agree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Disagreement
    class_class_curie: ClassVar[str] = "sio:Disagreement"
    class_name: ClassVar[str] = "Disagreement"
    class_model_uri: ClassVar[URIRef] = SIO.Disagreement


class FullAgreement(Agreement):
    """
    full agreement is the result of consensus decision making when members of the group unanimously agree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FullAgreement
    class_class_curie: ClassVar[str] = "sio:FullAgreement"
    class_name: ClassVar[str] = "FullAgreement"
    class_model_uri: ClassVar[URIRef] = SIO.FullAgreement


class FullDisagreement(Disagreement):
    """
    full agreement is the result of consensus decision making when members of the group unanimously disagree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FullDisagreement
    class_class_curie: ClassVar[str] = "sio:FullDisagreement"
    class_name: ClassVar[str] = "FullDisagreement"
    class_model_uri: ClassVar[URIRef] = SIO.FullDisagreement


class Intensity(Quality):
    """
    intensity is a quality that represents the strength or degree of something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Intensity
    class_class_curie: ClassVar[str] = "sio:Intensity"
    class_name: ClassVar[str] = "Intensity"
    class_model_uri: ClassVar[URIRef] = SIO.Intensity


class Fatal(Intensity):
    """
    fatal is a qualitative intensity value that is more intense than severe, leading to the death/non-functioning of a
    system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Fatal
    class_class_curie: ClassVar[str] = "sio:Fatal"
    class_name: ClassVar[str] = "Fatal"
    class_model_uri: ClassVar[URIRef] = SIO.Fatal


class Mild(Intensity):
    """
    mild is a qualitative intensity value that is more intense than weak, but less intense than moderate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Mild
    class_class_curie: ClassVar[str] = "sio:Mild"
    class_name: ClassVar[str] = "Mild"
    class_model_uri: ClassVar[URIRef] = SIO.Mild


class Moderate(Intensity):
    """
    moderate is a qualitative intensity value that is more intense than mild, but less intense than strong.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Moderate
    class_class_curie: ClassVar[str] = "sio:Moderate"
    class_name: ClassVar[str] = "Moderate"
    class_model_uri: ClassVar[URIRef] = SIO.Moderate


class Negative(AssertionalQualifier):
    """
    negative is an assertional qualifier that expresses the falsity or lack of truth of a basic assertion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Negative
    class_class_curie: ClassVar[str] = "sio:Negative"
    class_name: ClassVar[str] = "Negative"
    class_model_uri: ClassVar[URIRef] = SIO.Negative


class Normality(Quality):
    """
    normality is the quality in which the value may differ from normal or average
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Normality
    class_class_curie: ClassVar[str] = "sio:Normality"
    class_name: ClassVar[str] = "Normality"
    class_model_uri: ClassVar[URIRef] = SIO.Normality


class Abnormal(Normality):
    """
    A quality that has a value that is outside normal or average.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Abnormal
    class_class_curie: ClassVar[str] = "sio:Abnormal"
    class_name: ClassVar[str] = "Abnormal"
    class_model_uri: ClassVar[URIRef] = SIO.Abnormal


class Decreased(Abnormal):
    """
    A quality that has a value that is decreased compared to normal or average.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Decreased
    class_class_curie: ClassVar[str] = "sio:Decreased"
    class_name: ClassVar[str] = "Decreased"
    class_model_uri: ClassVar[URIRef] = SIO.Decreased


class Increased(Abnormal):
    """
    A quality that has a value that is increased compared to normal or average.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Increased
    class_class_curie: ClassVar[str] = "sio:Increased"
    class_name: ClassVar[str] = "Increased"
    class_model_uri: ClassVar[URIRef] = SIO.Increased


class Normal(Normality):
    """
    A quality that has a value that is normal or average.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Normal
    class_class_curie: ClassVar[str] = "sio:Normal"
    class_name: ClassVar[str] = "Normal"
    class_model_uri: ClassVar[URIRef] = SIO.Normal


class ObjectQuality(Quality):
    """
    An object quality is quality of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ObjectQuality
    class_class_curie: ClassVar[str] = "sio:ObjectQuality"
    class_name: ClassVar[str] = "ObjectQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ObjectQuality


class BiologicalQuality(ObjectQuality):
    """
    A biological quality is a quality held by a biological entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiologicalQuality
    class_class_curie: ClassVar[str] = "sio:BiologicalQuality"
    class_name: ClassVar[str] = "BiologicalQuality"
    class_model_uri: ClassVar[URIRef] = SIO.BiologicalQuality


class BiologicalSex(BiologicalQuality):
    """
    biological sex is the quality of a biological organism based on reproductive function or organs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiologicalSex
    class_class_curie: ClassVar[str] = "sio:BiologicalSex"
    class_name: ClassVar[str] = "BiologicalSex"
    class_model_uri: ClassVar[URIRef] = SIO.BiologicalSex


class CellularQuality(BiologicalQuality):
    """
    cellular quality is the quality of a cell
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CellularQuality
    class_class_curie: ClassVar[str] = "sio:CellularQuality"
    class_name: ClassVar[str] = "CellularQuality"
    class_model_uri: ClassVar[URIRef] = SIO.CellularQuality


class ChemicalQuality(ObjectQuality):
    """
    chemical quality is the quality of a chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalQuality
    class_class_curie: ClassVar[str] = "sio:ChemicalQuality"
    class_name: ClassVar[str] = "ChemicalQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalQuality


class ChargeQuality(ChemicalQuality):
    """
    charge quality is the quality pertaining to electric charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChargeQuality
    class_class_curie: ClassVar[str] = "sio:ChargeQuality"
    class_name: ClassVar[str] = "ChargeQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ChargeQuality


class Charged(ChargeQuality):
    """
    The quality of having a charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Charged
    class_class_curie: ClassVar[str] = "sio:Charged"
    class_name: ClassVar[str] = "Charged"
    class_model_uri: ClassVar[URIRef] = SIO.Charged


class CodingFrameOffset(ChemicalQuality):
    """
    a coding frame offset is a numeric value that indicates the number of bases from a reference start codon position.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CodingFrameOffset
    class_class_curie: ClassVar[str] = "sio:CodingFrameOffset"
    class_name: ClassVar[str] = "CodingFrameOffset"
    class_model_uri: ClassVar[URIRef] = SIO.CodingFrameOffset


class CompleteCharge(Charged):
    """
    A complete charge is a charge where the value of the charge is a multiple of 1.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CompleteCharge
    class_class_curie: ClassVar[str] = "sio:CompleteCharge"
    class_name: ClassVar[str] = "CompleteCharge"
    class_model_uri: ClassVar[URIRef] = SIO.CompleteCharge


class CompositionalQuality(ObjectQuality):
    """
    composition quality is a quality that describes its composition or anatomy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CompositionalQuality
    class_class_curie: ClassVar[str] = "sio:CompositionalQuality"
    class_name: ClassVar[str] = "CompositionalQuality"
    class_model_uri: ClassVar[URIRef] = SIO.CompositionalQuality


class Disease(BiologicalQuality):
    """
    disease is the outward manifestation of one or more disorders.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Disease
    class_class_curie: ClassVar[str] = "sio:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = SIO.Disease


class Ethnicity(BiologicalQuality):
    """
    ethnicity is the biological quality of membership in a social group based on a common heritage.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ethnicity
    class_class_curie: ClassVar[str] = "sio:Ethnicity"
    class_name: ClassVar[str] = "Ethnicity"
    class_model_uri: ClassVar[URIRef] = SIO.Ethnicity


class Female(BiologicalSex):
    """
    female is a biological sex of an individual with female sexual organs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Female
    class_class_curie: ClassVar[str] = "sio:Female"
    class_name: ClassVar[str] = "Female"
    class_model_uri: ClassVar[URIRef] = SIO.Female


class Fitness(ObjectQuality):
    """
    fitness is the quality of an object with respect to some stated functions or evolutionary adaptation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Fitness
    class_class_curie: ClassVar[str] = "sio:Fitness"
    class_name: ClassVar[str] = "Fitness"
    class_model_uri: ClassVar[URIRef] = SIO.Fitness


class Heterogeneous(CompositionalQuality):
    """
    homogeneous is a quality that describes the varied composition of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Heterogeneous
    class_class_curie: ClassVar[str] = "sio:Heterogeneous"
    class_name: ClassVar[str] = "Heterogeneous"
    class_model_uri: ClassVar[URIRef] = SIO.Heterogeneous


class Homogeneous(CompositionalQuality):
    """
    homogeneous is a quality that describes the uniform composition of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Homogeneous
    class_class_curie: ClassVar[str] = "sio:Homogeneous"
    class_name: ClassVar[str] = "Homogeneous"
    class_model_uri: ClassVar[URIRef] = SIO.Homogeneous


class Intersex(BiologicalSex):
    """
    intersex is a biological sex characterised by birth with genitalia and/or secondary sexual characteristics of
    indeterminate sex, or which combine features of both sexes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Intersex
    class_class_curie: ClassVar[str] = "sio:Intersex"
    class_name: ClassVar[str] = "Intersex"
    class_model_uri: ClassVar[URIRef] = SIO.Intersex


class Hermaphrodite(Intersex):
    """
    hermaphrodite is a biological sex of an individual with both male and female sexual organs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hermaphrodite
    class_class_curie: ClassVar[str] = "sio:Hermaphrodite"
    class_name: ClassVar[str] = "Hermaphrodite"
    class_model_uri: ClassVar[URIRef] = SIO.Hermaphrodite


class LifeStatus(BiologicalQuality):
    """
    life status is the quality of whether something is alive or dead.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LifeStatus
    class_class_curie: ClassVar[str] = "sio:LifeStatus"
    class_name: ClassVar[str] = "LifeStatus"
    class_model_uri: ClassVar[URIRef] = SIO.LifeStatus


class Alive(LifeStatus):
    """
    alive is the state of a biological organism that exhibits biological functions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Alive
    class_class_curie: ClassVar[str] = "sio:Alive"
    class_name: ClassVar[str] = "Alive"
    class_model_uri: ClassVar[URIRef] = SIO.Alive


class Dead(LifeStatus):
    """
    dead is the quality of an object in which there is a cessation of all biological functions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Dead
    class_class_curie: ClassVar[str] = "sio:Dead"
    class_name: ClassVar[str] = "Dead"
    class_model_uri: ClassVar[URIRef] = SIO.Dead


class Healthy(Alive):
    """
    healthy is an organismal state of complete physical, mental and social well-being.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Healthy
    class_class_curie: ClassVar[str] = "sio:Healthy"
    class_name: ClassVar[str] = "Healthy"
    class_model_uri: ClassVar[URIRef] = SIO.Healthy


class Male(BiologicalSex):
    """
    male is a biological sex of an individual with male sexual organs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Male
    class_class_curie: ClassVar[str] = "sio:Male"
    class_name: ClassVar[str] = "Male"
    class_model_uri: ClassVar[URIRef] = SIO.Male


class MereologicalQuality(ObjectQuality):
    """
    a mereological quality is a quality of an entity vis-a-vis containment or parthood
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MereologicalQuality
    class_class_curie: ClassVar[str] = "sio:MereologicalQuality"
    class_name: ClassVar[str] = "MereologicalQuality"
    class_model_uri: ClassVar[URIRef] = SIO.MereologicalQuality


class ContainmentQuality(MereologicalQuality):
    """
    a containment quality is a quality of being able to contain another entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ContainmentQuality
    class_class_curie: ClassVar[str] = "sio:ContainmentQuality"
    class_name: ClassVar[str] = "ContainmentQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ContainmentQuality


class Empty(ContainmentQuality):
    """
    empty is the quality of not containing some thing
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Empty
    class_class_curie: ClassVar[str] = "sio:Empty"
    class_name: ClassVar[str] = "Empty"
    class_model_uri: ClassVar[URIRef] = SIO.Empty


class Full(ContainmentQuality):
    """
    full is the quality of contain an entity such that there is no more space for any additional entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Full
    class_class_curie: ClassVar[str] = "sio:Full"
    class_name: ClassVar[str] = "Full"
    class_model_uri: ClassVar[URIRef] = SIO.Full


class MolecularOrbital(ChemicalQuality):
    """
    A molecular orbital (or MO) is a mathematical function describing the wave-like behavior of an electron in a
    molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularOrbital
    class_class_curie: ClassVar[str] = "sio:MolecularOrbital"
    class_name: ClassVar[str] = "MolecularOrbital"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularOrbital


class MolecularStructureDescriptor(ChemicalQuality):
    """
    molecular structure descriptor is data that describes some aspect of the molecular structure (composition) and is
    about some chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularStructureDescriptor
    class_class_curie: ClassVar[str] = "sio:MolecularStructureDescriptor"
    class_name: ClassVar[str] = "MolecularStructureDescriptor"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularStructureDescriptor


class BiomolecularStructureDescriptor(MolecularStructureDescriptor):
    """
    A biomolecular structure descriptor is structure description for organic compounds.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiomolecularStructureDescriptor
    class_class_curie: ClassVar[str] = "sio:BiomolecularStructureDescriptor"
    class_name: ClassVar[str] = "BiomolecularStructureDescriptor"
    class_model_uri: ClassVar[URIRef] = SIO.BiomolecularStructureDescriptor


class NegativeCharge(CompleteCharge):
    """
    A negative charge is a charge where the value is negative.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NegativeCharge
    class_class_curie: ClassVar[str] = "sio:NegativeCharge"
    class_name: ClassVar[str] = "NegativeCharge"
    class_model_uri: ClassVar[URIRef] = SIO.NegativeCharge


class ObjectRelationalQuality(ObjectQuality):
    """
    object relational quality refers to a quality in relation to one or more objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ObjectRelationalQuality
    class_class_curie: ClassVar[str] = "sio:ObjectRelationalQuality"
    class_name: ClassVar[str] = "ObjectRelationalQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ObjectRelationalQuality


class ParentalTransmission(BiologicalQuality):
    """
    parental transmition is the quality of a biological organism in which the (genetic) material is transmitted from a
    parental unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ParentalTransmission
    class_class_curie: ClassVar[str] = "sio:ParentalTransmission"
    class_name: ClassVar[str] = "ParentalTransmission"
    class_model_uri: ClassVar[URIRef] = SIO.ParentalTransmission


class MaternallyTransmitted(ParentalTransmission):
    """
    maternally transmitted is the quality of a biological organism in which the (genetic) material is transmitted from
    the maternal line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaternallyTransmitted
    class_class_curie: ClassVar[str] = "sio:MaternallyTransmitted"
    class_name: ClassVar[str] = "MaternallyTransmitted"
    class_model_uri: ClassVar[URIRef] = SIO.MaternallyTransmitted


class PartialCharge(Charged):
    """
    The quality of having a charge that is not a full multiple of 1 unit charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PartialCharge
    class_class_curie: ClassVar[str] = "sio:PartialCharge"
    class_name: ClassVar[str] = "PartialCharge"
    class_model_uri: ClassVar[URIRef] = SIO.PartialCharge


class PartialNegativeCharge(PartialCharge):
    """
    A partial positive charge is a partial charge where the value of the charge is positive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PartialNegativeCharge
    class_class_curie: ClassVar[str] = "sio:PartialNegativeCharge"
    class_name: ClassVar[str] = "PartialNegativeCharge"
    class_model_uri: ClassVar[URIRef] = SIO.PartialNegativeCharge


class PartialPositiveCharge(PartialCharge):
    """
    A partial negative charge is a negative charge where the value of the charge is negative.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PartialPositiveCharge
    class_class_curie: ClassVar[str] = "sio:PartialPositiveCharge"
    class_name: ClassVar[str] = "PartialPositiveCharge"
    class_model_uri: ClassVar[URIRef] = SIO.PartialPositiveCharge


class PaternallyTransmitted(ParentalTransmission):
    """
    paternally transmitted is the quality of a biological organism in which the (genetic) material is transmitted from
    the paternal line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PaternallyTransmitted
    class_class_curie: ClassVar[str] = "sio:PaternallyTransmitted"
    class_name: ClassVar[str] = "PaternallyTransmitted"
    class_model_uri: ClassVar[URIRef] = SIO.PaternallyTransmitted


class Phenotype(BiologicalQuality):
    """
    A phenotype is an observable characteristic of an individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Phenotype
    class_class_curie: ClassVar[str] = "sio:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = SIO.Phenotype


class Ploidy(CellularQuality):
    """
    ploidy is the cellular quality relating to the amount of DNA contained in a cell.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ploidy
    class_class_curie: ClassVar[str] = "sio:Ploidy"
    class_name: ClassVar[str] = "Ploidy"
    class_model_uri: ClassVar[URIRef] = SIO.Ploidy


class PolarQuality(ChemicalQuality):
    """
    The quality of being polar or not polar.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolarQuality
    class_class_curie: ClassVar[str] = "sio:PolarQuality"
    class_name: ClassVar[str] = "PolarQuality"
    class_model_uri: ClassVar[URIRef] = SIO.PolarQuality


class Non-polar(PolarQuality):
    """
    non-polar is the quality of not having a dipole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Non-polar"]
    class_class_curie: ClassVar[str] = "sio:Non-polar"
    class_name: ClassVar[str] = "Non-polar"
    class_model_uri: ClassVar[URIRef] = SIO.Non-polar


class Polar(PolarQuality):
    """
    polar is the quality of having a dipole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Polar
    class_class_curie: ClassVar[str] = "sio:Polar"
    class_name: ClassVar[str] = "Polar"
    class_model_uri: ClassVar[URIRef] = SIO.Polar


class Positive(AssertionalQualifier):
    """
    positive is an assertional qualifier that expresses the validity or truth of a basic assertion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Positive
    class_class_curie: ClassVar[str] = "sio:Positive"
    class_name: ClassVar[str] = "Positive"
    class_model_uri: ClassVar[URIRef] = SIO.Positive


class PositiveCharge(CompleteCharge):
    """
    A positive charge is a charge where the value is positive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PositiveCharge
    class_class_curie: ClassVar[str] = "sio:PositiveCharge"
    class_name: ClassVar[str] = "PositiveCharge"
    class_model_uri: ClassVar[URIRef] = SIO.PositiveCharge


class Predicted(Hypothetical):
    """
    predicted is the quality of an entity that is thought to exist, as evidenced by some rational procedure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Predicted
    class_class_curie: ClassVar[str] = "sio:Predicted"
    class_name: ClassVar[str] = "Predicted"
    class_model_uri: ClassVar[URIRef] = SIO.Predicted


class PrimaryStructureDescriptor(BiomolecularStructureDescriptor):
    """
    A primary structure descriptor describes a biomolecular object in terms of a 1D or 2D topology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PrimaryStructureDescriptor
    class_class_curie: ClassVar[str] = "sio:PrimaryStructureDescriptor"
    class_name: ClassVar[str] = "PrimaryStructureDescriptor"
    class_model_uri: ClassVar[URIRef] = SIO.PrimaryStructureDescriptor


class BiopolymerSequence(PrimaryStructureDescriptor):
    """
    A sequence is a primary structure descriptor in which each of the letters in the string represents a monomeric
    unit (residue) in which adjacent letters represent the connectivity between the monomeric units.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiopolymerSequence
    class_class_curie: ClassVar[str] = "sio:BiopolymerSequence"
    class_name: ClassVar[str] = "BiopolymerSequence"
    class_model_uri: ClassVar[URIRef] = SIO.BiopolymerSequence


class NucleicAcidSequence(BiopolymerSequence):
    """
    A nucleic acid sequence is a symbolic representation of the sequence of nucleic acid residues in a nucleic acid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NucleicAcidSequence
    class_class_curie: ClassVar[str] = "sio:NucleicAcidSequence"
    class_name: ClassVar[str] = "NucleicAcidSequence"
    class_model_uri: ClassVar[URIRef] = SIO.NucleicAcidSequence


class CodingSequence(NucleicAcidSequence):
    """
    a coding sequence is a sequence of nucleotides which encode a RNA or protein product..
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CodingSequence
    class_class_curie: ClassVar[str] = "sio:CodingSequence"
    class_name: ClassVar[str] = "CodingSequence"
    class_model_uri: ClassVar[URIRef] = SIO.CodingSequence


class DeoxyribonucleicAcidSequence(NucleicAcidSequence):
    """
    A deoxyribonucleic acid sequence is a symbolic representation of the sequence of deoxyribonucleic acid residues in
    a deoxyribonucleic acid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcidSequence
    class_class_curie: ClassVar[str] = "sio:DeoxyribonucleicAcidSequence"
    class_name: ClassVar[str] = "DeoxyribonucleicAcidSequence"
    class_model_uri: ClassVar[URIRef] = SIO.DeoxyribonucleicAcidSequence


class ProcessQuality(Quality):
    """
    A process quality is quality that is associated with a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProcessQuality
    class_class_curie: ClassVar[str] = "sio:ProcessQuality"
    class_name: ClassVar[str] = "ProcessQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessQuality


class ProcessStatus(ProcessQuality):
    """
    process status is a process quality that describes the state of a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProcessStatus
    class_class_curie: ClassVar[str] = "sio:ProcessStatus"
    class_name: ClassVar[str] = "ProcessStatus"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessStatus


class Aborted(ProcessStatus):
    """
    aborted is a process status in which a started process will not complete as intended.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Aborted
    class_class_curie: ClassVar[str] = "sio:Aborted"
    class_name: ClassVar[str] = "Aborted"
    class_model_uri: ClassVar[URIRef] = SIO.Aborted


class Completed(ProcessStatus):
    """
    completed is that status of a process that successfully unfolds.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Completed
    class_class_curie: ClassVar[str] = "sio:Completed"
    class_name: ClassVar[str] = "Completed"
    class_model_uri: ClassVar[URIRef] = SIO.Completed


class NotStarted(ProcessStatus):
    """
    not started is the status of a process that is predicted to exist but has not yet begun.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NotStarted
    class_class_curie: ClassVar[str] = "sio:NotStarted"
    class_name: ClassVar[str] = "NotStarted"
    class_model_uri: ClassVar[URIRef] = SIO.NotStarted


class Cancelled(NotStarted):
    """
    cancelled is a process status in which the process, while planned to occur, will not occur.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Cancelled
    class_class_curie: ClassVar[str] = "sio:Cancelled"
    class_name: ClassVar[str] = "Cancelled"
    class_model_uri: ClassVar[URIRef] = SIO.Cancelled


class Ongoing(ProcessStatus):
    """
    ongoing is the status of a process that is not yet complete.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ongoing
    class_class_curie: ClassVar[str] = "sio:Ongoing"
    class_name: ClassVar[str] = "Ongoing"
    class_model_uri: ClassVar[URIRef] = SIO.Ongoing


class Planned(NotStarted):
    """
    planned is a process status for a process that has not yet started, but is referred to in a plan.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Planned
    class_class_curie: ClassVar[str] = "sio:Planned"
    class_name: ClassVar[str] = "Planned"
    class_model_uri: ClassVar[URIRef] = SIO.Planned


class ProteinSequence(BiopolymerSequence):
    """
    A protein acid sequence is the character representation of the molecular structure of a protein.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinSequence
    class_class_curie: ClassVar[str] = "sio:ProteinSequence"
    class_name: ClassVar[str] = "ProteinSequence"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinSequence


class QualityDescriptor(InformationalQuality):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.QualityDescriptor
    class_class_curie: ClassVar[str] = "sio:QualityDescriptor"
    class_name: ClassVar[str] = "QualityDescriptor"
    class_model_uri: ClassVar[URIRef] = SIO.QualityDescriptor


class ExcellentQuality(QualityDescriptor):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ExcellentQuality
    class_class_curie: ClassVar[str] = "sio:ExcellentQuality"
    class_name: ClassVar[str] = "ExcellentQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ExcellentQuality


class GoodQuality(QualityDescriptor):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GoodQuality
    class_class_curie: ClassVar[str] = "sio:GoodQuality"
    class_name: ClassVar[str] = "GoodQuality"
    class_model_uri: ClassVar[URIRef] = SIO.GoodQuality


class NeitherGoodNorPoorQuality(QualityDescriptor):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NeitherGoodNorPoorQuality
    class_class_curie: ClassVar[str] = "sio:NeitherGoodNorPoorQuality"
    class_name: ClassVar[str] = "NeitherGoodNorPoorQuality"
    class_model_uri: ClassVar[URIRef] = SIO.NeitherGoodNorPoorQuality


class PoorQuality(QualityDescriptor):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PoorQuality
    class_class_curie: ClassVar[str] = "sio:PoorQuality"
    class_name: ClassVar[str] = "PoorQuality"
    class_model_uri: ClassVar[URIRef] = SIO.PoorQuality


class QuantityModifier(InformationalQuality):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.QuantityModifier
    class_class_curie: ClassVar[str] = "sio:QuantityModifier"
    class_name: ClassVar[str] = "QuantityModifier"
    class_model_uri: ClassVar[URIRef] = SIO.QuantityModifier


class ALittleQuantifier(QuantityModifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ALittleQuantifier
    class_class_curie: ClassVar[str] = "sio:ALittleQuantifier"
    class_name: ClassVar[str] = "ALittleQuantifier"
    class_model_uri: ClassVar[URIRef] = SIO.ALittleQuantifier


class CompletelyQuantifier(QuantityModifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CompletelyQuantifier
    class_class_curie: ClassVar[str] = "sio:CompletelyQuantifier"
    class_name: ClassVar[str] = "CompletelyQuantifier"
    class_model_uri: ClassVar[URIRef] = SIO.CompletelyQuantifier


class ModeratelyQuantifier(QuantityModifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ModeratelyQuantifier
    class_class_curie: ClassVar[str] = "sio:ModeratelyQuantifier"
    class_name: ClassVar[str] = "ModeratelyQuantifier"
    class_model_uri: ClassVar[URIRef] = SIO.ModeratelyQuantifier


class MostlyQuantifier(QuantityModifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MostlyQuantifier
    class_class_curie: ClassVar[str] = "sio:MostlyQuantifier"
    class_name: ClassVar[str] = "MostlyQuantifier"
    class_model_uri: ClassVar[URIRef] = SIO.MostlyQuantifier


class NoneQuantifier(QuantityModifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NoneQuantifier
    class_class_curie: ClassVar[str] = "sio:NoneQuantifier"
    class_name: ClassVar[str] = "NoneQuantifier"
    class_model_uri: ClassVar[URIRef] = SIO.NoneQuantifier


class QuaternaryStructure(BiomolecularStructureDescriptor):
    """
    A quaternary structure descriptor describes topological patterns in a multi-unit biopolymer complex.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.QuaternaryStructure
    class_class_curie: ClassVar[str] = "sio:QuaternaryStructure"
    class_name: ClassVar[str] = "QuaternaryStructure"
    class_model_uri: ClassVar[URIRef] = SIO.QuaternaryStructure


class Race(BiologicalQuality):
    """
    race is a characteristic of an individual by heritable phenotypic characteristics, geographic ancestry, physical
    appearance, ethnicity, and social status.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Race
    class_class_curie: ClassVar[str] = "sio:Race"
    class_name: ClassVar[str] = "Race"
    class_model_uri: ClassVar[URIRef] = SIO.Race


class Radar(Device):
    """
    A radar is an object-detection system which uses radio waves to determine the range, altitude, direction, or speed
    of objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Radar
    class_class_curie: ClassVar[str] = "sio:Radar"
    class_name: ClassVar[str] = "Radar"
    class_model_uri: ClassVar[URIRef] = SIO.Radar


class RadioReceiver(CommunicationDevice):
    """
    A radio receiver is a communication device that receives its input from an antenna, uses electronic filters to
    separate a wanted radio signal from all other signals picked up by this antenna, amplifies it to a level suitable
    for further processing, and finally converts through demodulation and decoding the signal into a form usable for
    the consumer, such as sound, pictures, digital data, measurement values, navigational positions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RadioReceiver
    class_class_curie: ClassVar[str] = "sio:RadioReceiver"
    class_name: ClassVar[str] = "RadioReceiver"
    class_model_uri: ClassVar[URIRef] = SIO.RadioReceiver


class RadiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RadiumAtom
    class_class_curie: ClassVar[str] = "sio:RadiumAtom"
    class_name: ClassVar[str] = "RadiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RadiumAtom


class RadonAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RadonAtom
    class_class_curie: ClassVar[str] = "sio:RadonAtom"
    class_name: ClassVar[str] = "RadonAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RadonAtom


class Rage(Anger):
    """
    Rage is a feeling of intense anger that is associated with the Fight-or-flight response.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Rage
    class_class_curie: ClassVar[str] = "sio:Rage"
    class_name: ClassVar[str] = "Rage"
    class_model_uri: ClassVar[URIRef] = SIO.Rage


class Rat(MulticellularOrganism):
    """
    A rat is a medium-sized, long-tailed rodent of the superfamily Muroidea.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Rat
    class_class_curie: ClassVar[str] = "sio:Rat"
    class_name: ClassVar[str] = "Rat"
    class_model_uri: ClassVar[URIRef] = SIO.Rat


class Ray(Line):
    """
    A ray is a line which that is bounded by a startpoint and extends outwards infinitely along one dimension.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ray
    class_class_curie: ClassVar[str] = "sio:Ray"
    class_name: ClassVar[str] = "Ray"
    class_model_uri: ClassVar[URIRef] = SIO.Ray


class Reagent(HeterogeneousSubstance):
    """
    A reagent is a substance that is added to a system in order to bring about a chemical reaction, or added to see if
    a reaction occurs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Reagent
    class_class_curie: ClassVar[str] = "sio:Reagent"
    class_name: ClassVar[str] = "Reagent"
    class_model_uri: ClassVar[URIRef] = SIO.Reagent


class Real(ExistenceQuality):
    """
    real is the quality of an entity that exists in real space and time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Real
    class_class_curie: ClassVar[str] = "sio:Real"
    class_name: ClassVar[str] = "Real"
    class_model_uri: ClassVar[URIRef] = SIO.Real


@dataclass
class RealizableEntity(Attribute):
    """
    A realizable entity is an attribute that is exhibited under some condition and is realized in some process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RealizableEntity
    class_class_curie: ClassVar[str] = "sio:RealizableEntity"
    class_name: ClassVar[str] = "RealizableEntity"
    class_model_uri: ClassVar[URIRef] = SIO.RealizableEntity

    hasBasis: Optional[Union[dict, Quality]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasBasis is not None and not isinstance(self.hasBasis, Quality):
            self.hasBasis = Quality(**as_dict(self.hasBasis))

        super().__post_init__(**kwargs)


@dataclass
class Capability(RealizableEntity):
    """
    A capability is a realizable entity whose basis lies in one or more parts or qualities and reflects possibility of
    an entity to behave in a specified way under certain conditions or in response to a certain stimulus (trigger).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Capability
    class_class_curie: ClassVar[str] = "sio:Capability"
    class_name: ClassVar[str] = "Capability"
    class_model_uri: ClassVar[URIRef] = SIO.Capability

    isCapabilityOf: Optional[Union[dict, "Entity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isCapabilityOf is not None and not isinstance(self.isCapabilityOf, Entity):
            self.isCapabilityOf = Entity(**as_dict(self.isCapabilityOf))

        super().__post_init__(**kwargs)


@dataclass
class Disposition(Capability):
    """
    A disposition is the tendency of a capability to be exhibited under certain conditions or in response to a certain
    stimulus (trigger).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Disposition
    class_class_curie: ClassVar[str] = "sio:Disposition"
    class_name: ClassVar[str] = "Disposition"
    class_model_uri: ClassVar[URIRef] = SIO.Disposition

    isDispositionOf: Optional[Union[dict, "Entity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isDispositionOf is not None and not isinstance(self.isDispositionOf, Entity):
            self.isDispositionOf = Entity(**as_dict(self.isDispositionOf))

        super().__post_init__(**kwargs)


class Dysfunction(Capability):
    """
    dysfunction is a capability to act in a manner that is abnormal or opposite  to the object's typical function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Dysfunction
    class_class_curie: ClassVar[str] = "sio:Dysfunction"
    class_name: ClassVar[str] = "Dysfunction"
    class_model_uri: ClassVar[URIRef] = SIO.Dysfunction


@dataclass
class Function(Capability):
    """
    A function is a capability that satisfies some agentive objective, or (evolutionary) optimization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Function
    class_class_curie: ClassVar[str] = "sio:Function"
    class_name: ClassVar[str] = "Function"
    class_model_uri: ClassVar[URIRef] = SIO.Function

    isFunctionOf: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isFunctionOf is not None and not isinstance(self.isFunctionOf, Entity):
            self.isFunctionOf = Entity(**as_dict(self.isFunctionOf))

        super().__post_init__(**kwargs)


class MutualDisposition(Disposition):
    """
    A mutual disposition is a disposition that simulataneously invokes another disposition when realized.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MutualDisposition
    class_class_curie: ClassVar[str] = "sio:MutualDisposition"
    class_name: ClassVar[str] = "MutualDisposition"
    class_model_uri: ClassVar[URIRef] = SIO.MutualDisposition


class Reason(Justification):
    """
    A reason is a justification that specifies the motive for an action or a determination.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Reason
    class_class_curie: ClassVar[str] = "sio:Reason"
    class_name: ClassVar[str] = "Reason"
    class_model_uri: ClassVar[URIRef] = SIO.Reason


class Purpose(Reason):
    """
    purpose is the reason for which something is done or created or for which something exists.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Purpose
    class_class_curie: ClassVar[str] = "sio:Purpose"
    class_name: ClassVar[str] = "Purpose"
    class_model_uri: ClassVar[URIRef] = SIO.Purpose


class Reasoning(Creating):
    """
    reasoning is the agentive process of using knowledge to evaluate the truth value of a proposition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Reasoning
    class_class_curie: ClassVar[str] = "sio:Reasoning"
    class_name: ClassVar[str] = "Reasoning"
    class_model_uri: ClassVar[URIRef] = SIO.Reasoning


class Rectangle(Quadrilateral):
    """
    A rectangle is a quadrilateral in which one pair of line segments are parallel and the other pair are
    perpendicular to the first pair.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Rectangle
    class_class_curie: ClassVar[str] = "sio:Rectangle"
    class_name: ClassVar[str] = "Rectangle"
    class_model_uri: ClassVar[URIRef] = SIO.Rectangle


class Bar(Rectangle):
    """
    A bar is a rectangle that is located in the plot of a statistical graph in which its length is proportional to the
    values that it represents.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Bar
    class_class_curie: ClassVar[str] = "sio:Bar"
    class_name: ClassVar[str] = "Bar"
    class_model_uri: ClassVar[URIRef] = SIO.Bar


class RedoxReaction(ChemicalReaction):
    """
    A redox reaction is a chemical reaction in which there is a net movement of electrons from one reactant to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RedoxReaction
    class_class_curie: ClassVar[str] = "sio:RedoxReaction"
    class_name: ClassVar[str] = "RedoxReaction"
    class_model_uri: ClassVar[URIRef] = SIO.RedoxReaction


class ReferencingCell(Cellinformational):
    """
    A referenceing cell is a cell of a cellular automata that refers to another cell.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ReferencingCell
    class_class_curie: ClassVar[str] = "sio:ReferencingCell"
    class_name: ClassVar[str] = "ReferencingCell"
    class_model_uri: ClassVar[URIRef] = SIO.ReferencingCell


class ReferentCell(Cellinformational):
    """
    A referent cell is a cell that is the referent of some function or pointer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ReferentCell
    class_class_curie: ClassVar[str] = "sio:ReferentCell"
    class_name: ClassVar[str] = "ReferentCell"
    class_model_uri: ClassVar[URIRef] = SIO.ReferentCell


class Regulating(Interacting):
    """
    regulating is a process that modulates the attributes of an object or process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Regulating
    class_class_curie: ClassVar[str] = "sio:Regulating"
    class_name: ClassVar[str] = "Regulating"
    class_model_uri: ClassVar[URIRef] = SIO.Regulating


class RegulationOfCapability(Regulating):
    """
    regulation of capability is the regulation of the ability of one party by another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfCapability
    class_class_curie: ClassVar[str] = "sio:RegulationOfCapability"
    class_name: ClassVar[str] = "RegulationOfCapability"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfCapability


class RegulationOfCatalyticCapability(RegulationOfCapability):
    """
    the regulation of the enzymatic activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfCatalyticCapability
    class_class_curie: ClassVar[str] = "sio:RegulationOfCatalyticCapability"
    class_name: ClassVar[str] = "RegulationOfCatalyticCapability"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfCatalyticCapability


class BiochemicalActivation(RegulationOfCatalyticCapability):
    """
    biochemical activation is a molecular interaction that increases the catalytic rate of the target enzyme.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiochemicalActivation
    class_class_curie: ClassVar[str] = "sio:BiochemicalActivation"
    class_name: ClassVar[str] = "BiochemicalActivation"
    class_model_uri: ClassVar[URIRef] = SIO.BiochemicalActivation


class BiochemicalInhibition(RegulationOfCatalyticCapability):
    """
    biochemical inhibition is a molecular interaction that decreases the catalytic rate of the target enzyme.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiochemicalInhibition
    class_class_curie: ClassVar[str] = "sio:BiochemicalInhibition"
    class_name: ClassVar[str] = "BiochemicalInhibition"
    class_model_uri: ClassVar[URIRef] = SIO.BiochemicalInhibition


class RegulationOfProcess(Regulating):
    """
    regulation of a process is a process that modulates the duration, frequency, spatial extent of a target process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfProcess
    class_class_curie: ClassVar[str] = "sio:RegulationOfProcess"
    class_name: ClassVar[str] = "RegulationOfProcess"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfProcess


class ProcessDown-regulation(RegulationOfProcess):
    """
    process down-regulation is a process that decreases the frequency, rate or extent of one or more processes in
    relation to a reference state.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["ProcessDown-regulation"]
    class_class_curie: ClassVar[str] = "sio:ProcessDown-regulation"
    class_name: ClassVar[str] = "ProcessDown-regulation"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessDown-regulation


class ProcessMaintenance(RegulationOfProcess):
    """
    The process of maintaining some the frequency, rate or extent of another process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProcessMaintenance
    class_class_curie: ClassVar[str] = "sio:ProcessMaintenance"
    class_name: ClassVar[str] = "ProcessMaintenance"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessMaintenance


class InformationMaintenance(ProcessMaintenance):
    """
    the regulation or maintenance of information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationMaintenance
    class_class_curie: ClassVar[str] = "sio:InformationMaintenance"
    class_name: ClassVar[str] = "InformationMaintenance"
    class_model_uri: ClassVar[URIRef] = SIO.InformationMaintenance


class ProcessUp-regulation(RegulationOfProcess):
    """
    process up-regulation is a process that increases the frequency, rate or extent of one or more processes in
    relation to a reference state.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["ProcessUp-regulation"]
    class_class_curie: ClassVar[str] = "sio:ProcessUp-regulation"
    class_name: ClassVar[str] = "ProcessUp-regulation"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessUp-regulation


class RegulationOfBiochemicalProcess(RegulationOfProcess):
    """
    regulation of biochemical process is a process that changes the frequency, rate or extent of a target biochemical
    process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfBiochemicalProcess
    class_class_curie: ClassVar[str] = "sio:RegulationOfBiochemicalProcess"
    class_name: ClassVar[str] = "RegulationOfBiochemicalProcess"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfBiochemicalProcess


class RegulationOfObjectQuantity(RegulationOfProcess):
    """
    regulation of a participant quantity is the regulation of a process in which the quantity of its partcipants is
    changed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfObjectQuantity
    class_class_curie: ClassVar[str] = "sio:RegulationOfObjectQuantity"
    class_name: ClassVar[str] = "RegulationOfObjectQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfObjectQuantity


class RegulationOfMolecularQuantity(RegulationOfObjectQuantity):
    """
    A process that modulates the frequency, rate or extent of process involved in the creation or destruction of a
    molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfMolecularQuantity
    class_class_curie: ClassVar[str] = "sio:RegulationOfMolecularQuantity"
    class_name: ClassVar[str] = "RegulationOfMolecularQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfMolecularQuantity


class RegulationOfMolecularDegradation(RegulationOfMolecularQuantity):
    """
    A process that modulates the frequency, rate or extent of process involved in the destruction of a molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfMolecularDegradation
    class_class_curie: ClassVar[str] = "sio:RegulationOfMolecularDegradation"
    class_name: ClassVar[str] = "RegulationOfMolecularDegradation"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfMolecularDegradation


class DecreasedMolecularDegradationFromDecreasedRegulation(RegulationOfMolecularDegradation):
    """
    A process that decreases the frequency, rate or extent of process involved in the destruction of a molecule as a
    result of decreased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedMolecularDegradationFromDecreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedMolecularDegradationFromDecreasedRegulation"
    class_name: ClassVar[str] = "DecreasedMolecularDegradationFromDecreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedMolecularDegradationFromDecreasedRegulation


class DecreasedMolecularDegradationFromIncreasedRegulation(RegulationOfMolecularDegradation):
    """
    A process that decreases the frequency, rate or extent of process involved in the destruction of a molecule as a
    result of increased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedMolecularDegradationFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedMolecularDegradationFromIncreasedRegulation"
    class_name: ClassVar[str] = "DecreasedMolecularDegradationFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedMolecularDegradationFromIncreasedRegulation


class IncreasedMolecularDegradationFromDecreasedRegulation(RegulationOfMolecularDegradation):
    """
    A process that increases the frequency, rate or extent of process involved in the destruction of a molecule as a
    result of decreased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedMolecularDegradationFromDecreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedMolecularDegradationFromDecreasedRegulation"
    class_name: ClassVar[str] = "IncreasedMolecularDegradationFromDecreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedMolecularDegradationFromDecreasedRegulation


class IncreasedMolecularDegradationFromIncreasedRegulation(RegulationOfMolecularDegradation):
    """
    A process that increases the frequency, rate or extent of process involved in the destruction of a molecule as a
    result of increased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedMolecularDegradationFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedMolecularDegradationFromIncreasedRegulation"
    class_name: ClassVar[str] = "IncreasedMolecularDegradationFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedMolecularDegradationFromIncreasedRegulation


class RegulationOfMolecularProduction(RegulationOfMolecularQuantity):
    """
    A process that modulates the frequency, rate or extent of process involved in the production of a molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfMolecularProduction
    class_class_curie: ClassVar[str] = "sio:RegulationOfMolecularProduction"
    class_name: ClassVar[str] = "RegulationOfMolecularProduction"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfMolecularProduction


class DecreasedMolecularProductionFromDecreasedRegulation(RegulationOfMolecularProduction):
    """
    A process that decreases the frequency, rate or extent of process involved in the production of a molecule as a
    result of decreased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedMolecularProductionFromDecreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedMolecularProductionFromDecreasedRegulation"
    class_name: ClassVar[str] = "DecreasedMolecularProductionFromDecreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedMolecularProductionFromDecreasedRegulation


class DecreasedMolecularProductionFromIncreasedRegulation(RegulationOfMolecularProduction):
    """
    A process that decreases the frequency, rate or extent of process involved in the production of a molecule as a
    result of increased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedMolecularProductionFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedMolecularProductionFromIncreasedRegulation"
    class_name: ClassVar[str] = "DecreasedMolecularProductionFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedMolecularProductionFromIncreasedRegulation


class IncreasedMolecularProductionFromDecreasedRegulation(RegulationOfMolecularProduction):
    """
    A process that increases the frequency, rate or extent of process involved in the production of a molecule as a
    result of decreased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedMolecularProductionFromDecreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedMolecularProductionFromDecreasedRegulation"
    class_name: ClassVar[str] = "IncreasedMolecularProductionFromDecreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedMolecularProductionFromDecreasedRegulation


class IncreasedMolecularProductionFromIncreasedRegulation(RegulationOfMolecularProduction):
    """
    A process that increases the frequency, rate or extent of process involved in the production of a molecule as a
    result of increased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedMolecularProductionFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedMolecularProductionFromIncreasedRegulation"
    class_name: ClassVar[str] = "IncreasedMolecularProductionFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedMolecularProductionFromIncreasedRegulation


class RegulationOfObjectConsumption(RegulationOfObjectQuantity):
    """
    A process that modulates the frequency, rate or extent of process involved in the consumption of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfObjectConsumption
    class_class_curie: ClassVar[str] = "sio:RegulationOfObjectConsumption"
    class_name: ClassVar[str] = "RegulationOfObjectConsumption"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfObjectConsumption


class DecreasedObjectConsumptionFromIncreasedRegulation(RegulationOfObjectConsumption):
    """
    increased regulation leads to an decrease in the consumption of an object of specified type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedObjectConsumptionFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedObjectConsumptionFromIncreasedRegulation"
    class_name: ClassVar[str] = "DecreasedObjectConsumptionFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedObjectConsumptionFromIncreasedRegulation


class IncreasedObjectConsumptionFromIncreasedRegulation(RegulationOfObjectConsumption):
    """
    increased regulation leads to an increase in the consumption of an object of specified type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedObjectConsumptionFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedObjectConsumptionFromIncreasedRegulation"
    class_name: ClassVar[str] = "IncreasedObjectConsumptionFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedObjectConsumptionFromIncreasedRegulation


class MaintenanceOfLevelOfObjectConsumption(RegulationOfObjectConsumption):
    """
    regulation of a participant quantity is the regulation of a process in which the quantity of a selected
    participant is maintained at a steady level.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaintenanceOfLevelOfObjectConsumption
    class_class_curie: ClassVar[str] = "sio:MaintenanceOfLevelOfObjectConsumption"
    class_name: ClassVar[str] = "MaintenanceOfLevelOfObjectConsumption"
    class_model_uri: ClassVar[URIRef] = SIO.MaintenanceOfLevelOfObjectConsumption


class RegulationOfObjectProduction(RegulationOfObjectQuantity):
    """
    regulation of a participant quantity is the regulation of a process in which the quantity of a selected
    participant is increased.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfObjectProduction
    class_class_curie: ClassVar[str] = "sio:RegulationOfObjectProduction"
    class_name: ClassVar[str] = "RegulationOfObjectProduction"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfObjectProduction


class DecreasedObjectProductionFromIncreasedRegulation(RegulationOfObjectProduction):
    """
    increased regulation leads to a decrease in the number of target objects of a specified type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedObjectProductionFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedObjectProductionFromIncreasedRegulation"
    class_name: ClassVar[str] = "DecreasedObjectProductionFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedObjectProductionFromIncreasedRegulation


class IncreasedObjectProductionFromIncreasedRegulation(RegulationOfObjectProduction):
    """
    increased regulation leads to an increase in the number of target objects of a specified type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedObjectProductionFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedObjectProductionFromIncreasedRegulation"
    class_name: ClassVar[str] = "IncreasedObjectProductionFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedObjectProductionFromIncreasedRegulation


class MaintenanceOfQuantityOfObjectProduction(RegulationOfObjectProduction):
    """
    maintenance of quantity of object production is a regulation of object production in which the number of objects
    produced is held more or less constant.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaintenanceOfQuantityOfObjectProduction
    class_class_curie: ClassVar[str] = "sio:MaintenanceOfQuantityOfObjectProduction"
    class_name: ClassVar[str] = "MaintenanceOfQuantityOfObjectProduction"
    class_model_uri: ClassVar[URIRef] = SIO.MaintenanceOfQuantityOfObjectProduction


class RegulationOfProcessDuration(RegulationOfProcess):
    """
    regulation of a process duration is a process that modulates the duration of another process relative to some
    reference process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfProcessDuration
    class_class_curie: ClassVar[str] = "sio:RegulationOfProcessDuration"
    class_name: ClassVar[str] = "RegulationOfProcessDuration"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfProcessDuration


class DecreasedDurationOfProcessFromIncreasedRegulation(RegulationOfProcessDuration):
    """
    decreased duration of process from increased regulation is a process in which the duration of the target process
    is decreased as a result of increased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedDurationOfProcessFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedDurationOfProcessFromIncreasedRegulation"
    class_name: ClassVar[str] = "DecreasedDurationOfProcessFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedDurationOfProcessFromIncreasedRegulation


class IncreasedDurationOfProcessFromIncreasedRegulation(RegulationOfProcessDuration):
    """
    increased duration of process from increased regulation is a process in which the duration of the target process
    is increased as a result of increased regulation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedDurationOfProcessFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedDurationOfProcessFromIncreasedRegulation"
    class_name: ClassVar[str] = "IncreasedDurationOfProcessFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedDurationOfProcessFromIncreasedRegulation


class MaintenanceOfDurationOfProcess(RegulationOfProcessDuration):
    """
    maintenance of duration of process is a process that regulates a target process to maintain its duration within an
    expected interval.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaintenanceOfDurationOfProcess
    class_class_curie: ClassVar[str] = "sio:MaintenanceOfDurationOfProcess"
    class_name: ClassVar[str] = "MaintenanceOfDurationOfProcess"
    class_model_uri: ClassVar[URIRef] = SIO.MaintenanceOfDurationOfProcess


class RegulationOfProcessFrequency(RegulationOfProcess):
    """
    regulation of a process duration is a process that modulates the frequency of another process relative to some
    reference process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfProcessFrequency
    class_class_curie: ClassVar[str] = "sio:RegulationOfProcessFrequency"
    class_name: ClassVar[str] = "RegulationOfProcessFrequency"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfProcessFrequency


class DecreasedFrequencyOfProcessFromIncreasedRegulation(RegulationOfProcessFrequency):
    """
    The increase of regulation leads to a decreased occurence of processes of the target process type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedFrequencyOfProcessFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedFrequencyOfProcessFromIncreasedRegulation"
    class_name: ClassVar[str] = "DecreasedFrequencyOfProcessFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedFrequencyOfProcessFromIncreasedRegulation


class IncreasedFrequencyOfProcessFromIncreasedRegulation(RegulationOfProcessFrequency):
    """
    The increase of regulation leads to a increased occurence of processes of the target type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedFrequencyOfProcessFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedFrequencyOfProcessFromIncreasedRegulation"
    class_name: ClassVar[str] = "IncreasedFrequencyOfProcessFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedFrequencyOfProcessFromIncreasedRegulation


class MaintenanceOfFrequencyOfProcess(RegulationOfProcessFrequency):
    """
    maintenance of frequency of process is a process that regulates the number of occurences of a target process type
    to a specified number or interval.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaintenanceOfFrequencyOfProcess
    class_class_curie: ClassVar[str] = "sio:MaintenanceOfFrequencyOfProcess"
    class_name: ClassVar[str] = "MaintenanceOfFrequencyOfProcess"
    class_model_uri: ClassVar[URIRef] = SIO.MaintenanceOfFrequencyOfProcess


class RegulationOfProcessSpatialExtent(RegulationOfProcess):
    """
    regulation of a process spatial extent is a process that modulates the spatial extent of another process relative
    to some reference process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfProcessSpatialExtent
    class_class_curie: ClassVar[str] = "sio:RegulationOfProcessSpatialExtent"
    class_name: ClassVar[str] = "RegulationOfProcessSpatialExtent"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfProcessSpatialExtent


class DecreasedSpatialExtentOfProcessFromDecreasedRegulation(RegulationOfProcessSpatialExtent):
    """
    The increase of regulation leads to a decreased spatial extent of the target process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasedSpatialExtentOfProcessFromDecreasedRegulation
    class_class_curie: ClassVar[str] = "sio:DecreasedSpatialExtentOfProcessFromDecreasedRegulation"
    class_name: ClassVar[str] = "DecreasedSpatialExtentOfProcessFromDecreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasedSpatialExtentOfProcessFromDecreasedRegulation


class IncreasedSpatialExtentOfProcessFromIncreasedRegulation(RegulationOfProcessSpatialExtent):
    """
    The increase of regulation leads to a increased spatial extent of the target process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasedSpatialExtentOfProcessFromIncreasedRegulation
    class_class_curie: ClassVar[str] = "sio:IncreasedSpatialExtentOfProcessFromIncreasedRegulation"
    class_name: ClassVar[str] = "IncreasedSpatialExtentOfProcessFromIncreasedRegulation"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasedSpatialExtentOfProcessFromIncreasedRegulation


class MaintenanceOfSpatialExtentOfProcess(RegulationOfProcessSpatialExtent):
    """
    maintenance of spatial extent of process is a regulation of a process' spatial extent within some specified
    parameter.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaintenanceOfSpatialExtentOfProcess
    class_class_curie: ClassVar[str] = "sio:MaintenanceOfSpatialExtentOfProcess"
    class_name: ClassVar[str] = "MaintenanceOfSpatialExtentOfProcess"
    class_model_uri: ClassVar[URIRef] = SIO.MaintenanceOfSpatialExtentOfProcess


class RegulationOfTranscription(RegulationOfBiochemicalProcess):
    """
    A process that modulates the frequency, rate or extent of transcription.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfTranscription
    class_class_curie: ClassVar[str] = "sio:RegulationOfTranscription"
    class_name: ClassVar[str] = "RegulationOfTranscription"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfTranscription


class RegulationOfTranslation(RegulationOfBiochemicalProcess):
    """
    A process that modulates the frequency, rate or extent of translation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulationOfTranslation
    class_class_curie: ClassVar[str] = "sio:RegulationOfTranslation"
    class_name: ClassVar[str] = "RegulationOfTranslation"
    class_model_uri: ClassVar[URIRef] = SIO.RegulationOfTranslation


class ProteinMediatedRegulationOfTranslation(RegulationOfTranslation):
    """
    A process mediated by a protein that modulates the frequency, rate or extent of translation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinMediatedRegulationOfTranslation
    class_class_curie: ClassVar[str] = "sio:ProteinMediatedRegulationOfTranslation"
    class_name: ClassVar[str] = "ProteinMediatedRegulationOfTranslation"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinMediatedRegulationOfTranslation


class ReplicaQuality(ObjectRelationalQuality):
    """
    replica quality is the quality of an object that is an exact copy of another object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ReplicaQuality
    class_class_curie: ClassVar[str] = "sio:ReplicaQuality"
    class_name: ClassVar[str] = "ReplicaQuality"
    class_model_uri: ClassVar[URIRef] = SIO.ReplicaQuality


class Representation(InformationContentEntity):
    """
    A representation is a entity that in some way represents another entity (or attribute thereof).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Representation
    class_class_curie: ClassVar[str] = "sio:Representation"
    class_name: ClassVar[str] = "Representation"
    class_model_uri: ClassVar[URIRef] = SIO.Representation


class Model(Representation):
    """
    A model is a representation of some thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Model
    class_class_curie: ClassVar[str] = "sio:Model"
    class_name: ClassVar[str] = "Model"
    class_model_uri: ClassVar[URIRef] = SIO.Model


class ObjectModel(Model):
    """
    An object model is a representation of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ObjectModel
    class_class_curie: ClassVar[str] = "sio:ObjectModel"
    class_name: ClassVar[str] = "ObjectModel"
    class_model_uri: ClassVar[URIRef] = SIO.ObjectModel


class ProcessModel(Model):
    """
    A process model is a representation of some process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProcessModel
    class_class_curie: ClassVar[str] = "sio:ProcessModel"
    class_name: ClassVar[str] = "ProcessModel"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessModel


class Reproducing(Creating):
    """
    reproducing is a process characterized by creation of an entity that is similar or exactly the same as the
    template from which it is derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Reproducing
    class_class_curie: ClassVar[str] = "sio:Reproducing"
    class_name: ClassVar[str] = "Reproducing"
    class_model_uri: ClassVar[URIRef] = SIO.Reproducing


class BiologicalReproduction(Reproducing):
    """
    biological reproduction is the biological process by which one or more biological organisms are produced from
    their "parents".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiologicalReproduction
    class_class_curie: ClassVar[str] = "sio:BiologicalReproduction"
    class_name: ClassVar[str] = "BiologicalReproduction"
    class_model_uri: ClassVar[URIRef] = SIO.BiologicalReproduction


class Resentment(Disgust):
    """
    resentment is disgust directed toward a higher status individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Resentment
    class_class_curie: ClassVar[str] = "sio:Resentment"
    class_name: ClassVar[str] = "Resentment"
    class_model_uri: ClassVar[URIRef] = SIO.Resentment


class RheniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RheniumAtom
    class_class_curie: ClassVar[str] = "sio:RheniumAtom"
    class_name: ClassVar[str] = "RheniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RheniumAtom


class RhodiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RhodiumAtom
    class_class_curie: ClassVar[str] = "sio:RhodiumAtom"
    class_name: ClassVar[str] = "RhodiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RhodiumAtom


class RibonucleicAcid(NucleicAcid):
    """
    A ribonucleic acid is an organic polymer composed of a sequence of ribonucleotide residues.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RibonucleicAcid
    class_class_curie: ClassVar[str] = "sio:RibonucleicAcid"
    class_name: ClassVar[str] = "RibonucleicAcid"
    class_model_uri: ClassVar[URIRef] = SIO.RibonucleicAcid


class RNATranscript(RibonucleicAcid):
    """
    An RNA transcript is an RNA molecule that is produced from transcription of a nucleic acid template.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RNATranscript
    class_class_curie: ClassVar[str] = "sio:RNATranscript"
    class_name: ClassVar[str] = "RNATranscript"
    class_model_uri: ClassVar[URIRef] = SIO.RNATranscript


class MessengerRNA(RNATranscript):
    """
    A messenger RNA is a ribonucleic acid that contains an untranslated region (UTR) and protein coding sequence and
    lacks introns.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MessengerRNA
    class_class_curie: ClassVar[str] = "sio:MessengerRNA"
    class_name: ClassVar[str] = "MessengerRNA"
    class_model_uri: ClassVar[URIRef] = SIO.MessengerRNA


class MRNASpliceVariant(MessengerRNA):
    """
    An mRNA splice variant is an mRNA molecule that varies from another mRNA molecule of the same gene origin but
    having a different final sequence due to differences in its assembly from splice sites.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MRNASpliceVariant
    class_class_curie: ClassVar[str] = "sio:MRNASpliceVariant"
    class_name: ClassVar[str] = "MRNASpliceVariant"
    class_model_uri: ClassVar[URIRef] = SIO.MRNASpliceVariant


class MatureMRNA(MessengerRNA):
    """
    A mature RNA is a ribonucleic acid that contains an untranslated region (UTR) and protein coding sequence and
    lacks introns.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MatureMRNA
    class_class_curie: ClassVar[str] = "sio:MatureMRNA"
    class_name: ClassVar[str] = "MatureMRNA"
    class_model_uri: ClassVar[URIRef] = SIO.MatureMRNA


class Non-proteinCodingRNAncRNA(RNATranscript):
    """
    A non-protein coding RNA (ncRNA) is a RNA molecular that cannot be used as a template for generating a protein
    product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Non-proteinCodingRNAncRNA"]
    class_class_curie: ClassVar[str] = "sio:Non-proteinCodingRNAncRNA"
    class_name: ClassVar[str] = "Non-proteinCodingRNAncRNA"
    class_model_uri: ClassVar[URIRef] = SIO.Non-proteinCodingRNAncRNA


class MicroRNAmiRNA(Non-proteinCodingRNAncRNA):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MicroRNAmiRNA
    class_class_curie: ClassVar[str] = "sio:MicroRNAmiRNA"
    class_name: ClassVar[str] = "MicroRNAmiRNA"
    class_model_uri: ClassVar[URIRef] = SIO.MicroRNAmiRNA


class Pre-mRNA(MessengerRNA):
    """
    Precursor mRNA (pre-mRNA) is a single strand of messenger ribonucleic acid (mRNA) that is synthesized from a DNA
    template throught transcription.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Pre-mRNA"]
    class_class_curie: ClassVar[str] = "sio:Pre-mRNA"
    class_name: ClassVar[str] = "Pre-mRNA"
    class_model_uri: ClassVar[URIRef] = SIO.Pre-mRNA


class RibonucleicAcidSequence(NucleicAcidSequence):
    """
    A ribonucleic acid sequence is a symbolic representation of the sequence of ribonucleic acid residues in a
    ribonucleic acid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RibonucleicAcidSequence
    class_class_curie: ClassVar[str] = "sio:RibonucleicAcidSequence"
    class_name: ClassVar[str] = "RibonucleicAcidSequence"
    class_model_uri: ClassVar[URIRef] = SIO.RibonucleicAcidSequence


class RightClosedInterval(Interval):
    """
    a right closed interval is an interval in which there is a real number that is larger than all of its elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RightClosedInterval
    class_class_curie: ClassVar[str] = "sio:RightClosedInterval"
    class_name: ClassVar[str] = "RightClosedInterval"
    class_model_uri: ClassVar[URIRef] = SIO.RightClosedInterval


class RightOpenInterval(Interval):
    """
    a right open interval is an interval in which there is no element that is greater than all other elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RightOpenInterval
    class_class_curie: ClassVar[str] = "sio:RightOpenInterval"
    class_name: ClassVar[str] = "RightOpenInterval"
    class_model_uri: ClassVar[URIRef] = SIO.RightOpenInterval


class RnaMediatedRegulationOfTranslation(RegulationOfTranslation):
    """
    A process mediated by rna that modulates the frequency, rate or extent of translation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RnaMediatedRegulationOfTranslation
    class_class_curie: ClassVar[str] = "sio:RnaMediatedRegulationOfTranslation"
    class_name: ClassVar[str] = "RnaMediatedRegulationOfTranslation"
    class_model_uri: ClassVar[URIRef] = SIO.RnaMediatedRegulationOfTranslation


class RoentgeniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RoentgeniumAtom
    class_class_curie: ClassVar[str] = "sio:RoentgeniumAtom"
    class_name: ClassVar[str] = "RoentgeniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RoentgeniumAtom


@dataclass
class Role(RealizableEntity):
    """
    A role is a realizable entity that describes behaviours, rights and obligations of an entity in some particular
    circumstance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Role
    class_class_curie: ClassVar[str] = "sio:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = SIO.Role

    isRoleOf: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isRoleOf is not None and not isinstance(self.isRoleOf, Entity):
            self.isRoleOf = Entity(**as_dict(self.isRoleOf))

        super().__post_init__(**kwargs)


class AbstractRole(Role):
    """
    An abstract role is a role whose basis lies in spatial/temporal or comparative relations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AbstractRole
    class_class_curie: ClassVar[str] = "sio:AbstractRole"
    class_name: ClassVar[str] = "AbstractRole"
    class_model_uri: ClassVar[URIRef] = SIO.AbstractRole


class ComparativeRole(AbstractRole):
    """
    A comparative role is an abstract role which holds by comparing some attribute of another object of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ComparativeRole
    class_class_curie: ClassVar[str] = "sio:ComparativeRole"
    class_name: ClassVar[str] = "ComparativeRole"
    class_model_uri: ClassVar[URIRef] = SIO.ComparativeRole


class DuplicateRole(ComparativeRole):
    """
    a duplicate role is a comparative role that holds when one item is an exact copy of another in a specific set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DuplicateRole
    class_class_curie: ClassVar[str] = "sio:DuplicateRole"
    class_name: ClassVar[str] = "DuplicateRole"
    class_model_uri: ClassVar[URIRef] = SIO.DuplicateRole


class PositionalRole(AbstractRole):
    """
    A positional role is an abstract role which holds by comparing position to another object of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PositionalRole
    class_class_curie: ClassVar[str] = "sio:PositionalRole"
    class_name: ClassVar[str] = "PositionalRole"
    class_model_uri: ClassVar[URIRef] = SIO.PositionalRole


class ProcessualRole(Role):
    """
    A processual role is a role that can only be realized in a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProcessualRole
    class_class_curie: ClassVar[str] = "sio:ProcessualRole"
    class_name: ClassVar[str] = "ProcessualRole"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessualRole


class ChemicalEntityRole(ProcessualRole):
    """
    A chemical role is a processual role held by a chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalEntityRole
    class_class_curie: ClassVar[str] = "sio:ChemicalEntityRole"
    class_name: ClassVar[str] = "ChemicalEntityRole"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalEntityRole


class ChemicalSubstanceRole(ChemicalEntityRole):
    """
    A chemical substance role is a chemical entity role held by a chemical substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalSubstanceRole
    class_class_curie: ClassVar[str] = "sio:ChemicalSubstanceRole"
    class_name: ClassVar[str] = "ChemicalSubstanceRole"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalSubstanceRole


class BufferRole(ChemicalSubstanceRole):
    """
    A buffer role is the role of a chemical substance which maintains a pH at a near constant value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BufferRole
    class_class_curie: ClassVar[str] = "sio:BufferRole"
    class_name: ClassVar[str] = "BufferRole"
    class_model_uri: ClassVar[URIRef] = SIO.BufferRole


class HostRole(ChemicalSubstanceRole):
    """
    The role of an organism in providing resources to maintain the survival and/or reproduction of another organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HostRole
    class_class_curie: ClassVar[str] = "sio:HostRole"
    class_name: ClassVar[str] = "HostRole"
    class_model_uri: ClassVar[URIRef] = SIO.HostRole


class InvestigationalRole(ProcessualRole):
    """
    An investigational role is a role held by participants involved in an investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InvestigationalRole
    class_class_curie: ClassVar[str] = "sio:InvestigationalRole"
    class_name: ClassVar[str] = "InvestigationalRole"
    class_model_uri: ClassVar[URIRef] = SIO.InvestigationalRole


class EvaluationRole(InvestigationalRole):
    """
    An evaluation role is a processual role held by an entity during some evaluation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EvaluationRole
    class_class_curie: ClassVar[str] = "sio:EvaluationRole"
    class_name: ClassVar[str] = "EvaluationRole"
    class_model_uri: ClassVar[URIRef] = SIO.EvaluationRole


class ControlRole(EvaluationRole):
    """
    A control role is the role of an individual that is part of a study, but is not subject to the intervention that
    is to be tested.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ControlRole
    class_class_curie: ClassVar[str] = "sio:ControlRole"
    class_name: ClassVar[str] = "ControlRole"
    class_model_uri: ClassVar[URIRef] = SIO.ControlRole


class MolecularEntityRole(ChemicalEntityRole):
    """
    A molecular entity role is a chemical entity role held by a molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularEntityRole
    class_class_curie: ClassVar[str] = "sio:MolecularEntityRole"
    class_name: ClassVar[str] = "MolecularEntityRole"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularEntityRole


class CofactorRole(MolecularEntityRole):
    """
    The role of a chemical entity involved in the mechanism for enzyme-mediated catalysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CofactorRole
    class_class_curie: ClassVar[str] = "sio:CofactorRole"
    class_name: ClassVar[str] = "CofactorRole"
    class_model_uri: ClassVar[URIRef] = SIO.CofactorRole


class ProductRole(MolecularEntityRole):
    """
    The role of a chemical entity present at the end of a chemical reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProductRole
    class_class_curie: ClassVar[str] = "sio:ProductRole"
    class_name: ClassVar[str] = "ProductRole"
    class_model_uri: ClassVar[URIRef] = SIO.ProductRole


class ReactantRole(MolecularEntityRole):
    """
    The role of a chemical entity present at the beginning of a chemical reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ReactantRole
    class_class_curie: ClassVar[str] = "sio:ReactantRole"
    class_name: ClassVar[str] = "ReactantRole"
    class_model_uri: ClassVar[URIRef] = SIO.ReactantRole


class MolecularTracerRole(ReactantRole):
    """
    A molecular tracer role is a reactant role of a molecular entity that serves as a marker for the presence,
    abundance, or location of a molecular target that it associates with.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularTracerRole
    class_class_curie: ClassVar[str] = "sio:MolecularTracerRole"
    class_name: ClassVar[str] = "MolecularTracerRole"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularTracerRole


class ReagentRole(ChemicalSubstanceRole):
    """
    A role of a chemical substance that participates in a chemical reaction as part of some scientific investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ReagentRole
    class_class_curie: ClassVar[str] = "sio:ReagentRole"
    class_name: ClassVar[str] = "ReagentRole"
    class_model_uri: ClassVar[URIRef] = SIO.ReagentRole


class RegulatorRole(MolecularEntityRole):
    """
    The role of a chemical entity that modifies the rate of reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulatorRole
    class_class_curie: ClassVar[str] = "sio:RegulatorRole"
    class_name: ClassVar[str] = "RegulatorRole"
    class_model_uri: ClassVar[URIRef] = SIO.RegulatorRole


class ActivatorRole(RegulatorRole):
    """
    The role of a chemical entity that increases the rate of reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ActivatorRole
    class_class_curie: ClassVar[str] = "sio:ActivatorRole"
    class_name: ClassVar[str] = "ActivatorRole"
    class_model_uri: ClassVar[URIRef] = SIO.ActivatorRole


class CatalyticRole(RegulatorRole):
    """
    The role of a chemical participant that serves to increase the rate of reaction by lowering the activiation energy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CatalyticRole
    class_class_curie: ClassVar[str] = "sio:CatalyticRole"
    class_name: ClassVar[str] = "CatalyticRole"
    class_model_uri: ClassVar[URIRef] = SIO.CatalyticRole


class InhibitorRole(RegulatorRole):
    """
    The role of a chemical entity that reduces the rate of reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InhibitorRole
    class_class_curie: ClassVar[str] = "sio:InhibitorRole"
    class_name: ClassVar[str] = "InhibitorRole"
    class_model_uri: ClassVar[URIRef] = SIO.InhibitorRole


class ReplicateRole(ComparativeRole):
    """
    a replicate role is a comparative role that holds when one item is a reproduction, facsimile, or a copy of
    another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ReplicateRole
    class_class_curie: ClassVar[str] = "sio:ReplicateRole"
    class_name: ClassVar[str] = "ReplicateRole"
    class_model_uri: ClassVar[URIRef] = SIO.ReplicateRole


class Row(ComputationalEntity):
    """
    A row represents a single, implicitly structured data item in a table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Row
    class_class_curie: ClassVar[str] = "sio:Row"
    class_name: ClassVar[str] = "Row"
    class_model_uri: ClassVar[URIRef] = SIO.Row


class DatabaseRow(Row):
    """
    A database row is a row that is part of a database table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DatabaseRow
    class_class_curie: ClassVar[str] = "sio:DatabaseRow"
    class_name: ClassVar[str] = "DatabaseRow"
    class_model_uri: ClassVar[URIRef] = SIO.DatabaseRow


class RubidiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RubidiumAtom
    class_class_curie: ClassVar[str] = "sio:RubidiumAtom"
    class_name: ClassVar[str] = "RubidiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RubidiumAtom


class RutheniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RutheniumAtom
    class_class_curie: ClassVar[str] = "sio:RutheniumAtom"
    class_name: ClassVar[str] = "RutheniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RutheniumAtom


class RutherfordiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RutherfordiumAtom
    class_class_curie: ClassVar[str] = "sio:RutherfordiumAtom"
    class_name: ClassVar[str] = "RutherfordiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.RutherfordiumAtom


class Sadness(NegativeEmotion):
    """
    sadness is emotional pain associated with, or characterized by feelings of disadvantage, loss, despair,
    helplessness, sorrow, and rage.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sadness
    class_class_curie: ClassVar[str] = "sio:Sadness"
    class_name: ClassVar[str] = "Sadness"
    class_model_uri: ClassVar[URIRef] = SIO.Sadness


class Depression(Sadness):
    """
    depression is an unpleasant emotion linked to aversion to activity that can affect a person's thoughts, behavior,
    feelings and physical well-being. Depressed individuals may feel sad, anxious, empty, hopeless, worried, helpless,
    worthless, guilty, irritable, or restless.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Depression
    class_class_curie: ClassVar[str] = "sio:Depression"
    class_name: ClassVar[str] = "Depression"
    class_model_uri: ClassVar[URIRef] = SIO.Depression


class Despair(Sadness):
    """
    despair is depression, hopelessness or lack of hope.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Despair
    class_class_curie: ClassVar[str] = "sio:Despair"
    class_name: ClassVar[str] = "Despair"
    class_model_uri: ClassVar[URIRef] = SIO.Despair


class Grief(Sadness):
    """
    grief is an emotion in response to loss, whether physical or abstract including death, unemployment, ill health or
    the end of a relationship.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Grief
    class_class_curie: ClassVar[str] = "sio:Grief"
    class_name: ClassVar[str] = "Grief"
    class_model_uri: ClassVar[URIRef] = SIO.Grief


class Misery(Sadness):
    """
    misery is a feeling of great unhappiness, suffering and/or pain.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Misery
    class_class_curie: ClassVar[str] = "sio:Misery"
    class_name: ClassVar[str] = "Misery"
    class_model_uri: ClassVar[URIRef] = SIO.Misery


class SamariumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SamariumAtom
    class_class_curie: ClassVar[str] = "sio:SamariumAtom"
    class_name: ClassVar[str] = "SamariumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.SamariumAtom


class Sample(HeterogeneousSubstance):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sample
    class_class_curie: ClassVar[str] = "sio:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = SIO.Sample


class SampleQuality(ObjectRelationalQuality):
    """
    sample quality is the quality of an object that is drawn from a larger population.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SampleQuality
    class_class_curie: ClassVar[str] = "sio:SampleQuality"
    class_name: ClassVar[str] = "SampleQuality"
    class_model_uri: ClassVar[URIRef] = SIO.SampleQuality


class Sampling(Interacting):
    """
    sampling is the act of obtaining a sample, whether through selection, collection or preparation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sampling
    class_class_curie: ClassVar[str] = "sio:Sampling"
    class_name: ClassVar[str] = "Sampling"
    class_model_uri: ClassVar[URIRef] = SIO.Sampling


class Satisfaction(Contentment):
    """
    satisfaction is an emotion of fulfillment of one's wishes, expectations, or needs, or the pleasure derived from
    this.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Satisfaction
    class_class_curie: ClassVar[str] = "sio:Satisfaction"
    class_name: ClassVar[str] = "Satisfaction"
    class_model_uri: ClassVar[URIRef] = SIO.Satisfaction


class Pride(Satisfaction):
    """
    pride is an emotion of satisfaction of attachment toward one's own or another's choices and actions, or toward a
    whole group of people, and is a product of praise, independent self-reflection, or a fulfilled feeling of
    belonging.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pride
    class_class_curie: ClassVar[str] = "sio:Pride"
    class_name: ClassVar[str] = "Pride"
    class_model_uri: ClassVar[URIRef] = SIO.Pride


class SatisfactionQualifier(InformationalQuality):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SatisfactionQualifier
    class_class_curie: ClassVar[str] = "sio:SatisfactionQualifier"
    class_name: ClassVar[str] = "SatisfactionQualifier"
    class_model_uri: ClassVar[URIRef] = SIO.SatisfactionQualifier


class DissatisfiedQualifier(SatisfactionQualifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DissatisfiedQualifier
    class_class_curie: ClassVar[str] = "sio:DissatisfiedQualifier"
    class_name: ClassVar[str] = "DissatisfiedQualifier"
    class_model_uri: ClassVar[URIRef] = SIO.DissatisfiedQualifier


class NeitherSatisfiedOrDissatisfiedQualifier(SatisfactionQualifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NeitherSatisfiedOrDissatisfiedQualifier
    class_class_curie: ClassVar[str] = "sio:NeitherSatisfiedOrDissatisfiedQualifier"
    class_name: ClassVar[str] = "NeitherSatisfiedOrDissatisfiedQualifier"
    class_model_uri: ClassVar[URIRef] = SIO.NeitherSatisfiedOrDissatisfiedQualifier


class SatisfiedQualifier(SatisfactionQualifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SatisfiedQualifier
    class_class_curie: ClassVar[str] = "sio:SatisfiedQualifier"
    class_name: ClassVar[str] = "SatisfiedQualifier"
    class_model_uri: ClassVar[URIRef] = SIO.SatisfiedQualifier


class ScandiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ScandiumAtom
    class_class_curie: ClassVar[str] = "sio:ScandiumAtom"
    class_name: ClassVar[str] = "ScandiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ScandiumAtom


class ScientificData(DataItem):
    """
    scientific data is data obtained from some scientific procedure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ScientificData
    class_class_curie: ClassVar[str] = "sio:ScientificData"
    class_name: ClassVar[str] = "ScientificData"
    class_model_uri: ClassVar[URIRef] = SIO.ScientificData


class BiologicalData(ScientificData):
    """
    biological data is scientific data relevant to biology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiologicalData
    class_class_curie: ClassVar[str] = "sio:BiologicalData"
    class_name: ClassVar[str] = "BiologicalData"
    class_model_uri: ClassVar[URIRef] = SIO.BiologicalData


class BioinformaticData(BiologicalData):
    """
    bioinformatic data is data genereated or used for computer-based investigations of biological phenomena.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BioinformaticData
    class_class_curie: ClassVar[str] = "sio:BioinformaticData"
    class_name: ClassVar[str] = "BioinformaticData"
    class_model_uri: ClassVar[URIRef] = SIO.BioinformaticData


class ChemicalData(ScientificData):
    """
    A chemical datum is a scientific data item which conforms to some specification, either for how it is calculated
    or for how it is measured, and is commonly used in the domain of chemistry to name and differentiate different
    numeric properties (both calculated and measured) which are about chemical entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalData
    class_class_curie: ClassVar[str] = "sio:ChemicalData"
    class_name: ClassVar[str] = "ChemicalData"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalData


class GeneticData(BiologicalData):
    """
    genetic data is data pertaining to genetics.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeneticData
    class_class_curie: ClassVar[str] = "sio:GeneticData"
    class_name: ClassVar[str] = "GeneticData"
    class_model_uri: ClassVar[URIRef] = SIO.GeneticData


class MedicalData(BiologicalData):
    """
    medical data is data of interest to medicine.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalData
    class_class_curie: ClassVar[str] = "sio:MedicalData"
    class_name: ClassVar[str] = "MedicalData"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalData


class SeaborgiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SeaborgiumAtom
    class_class_curie: ClassVar[str] = "sio:SeaborgiumAtom"
    class_name: ClassVar[str] = "SeaborgiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.SeaborgiumAtom


class SecondaryCategoryAxis(CategoryAxis):
    """
    A secondary category axis is a category axis that defines a finer granular part (or subset) of the value range of
    the primary category axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SecondaryCategoryAxis
    class_class_curie: ClassVar[str] = "sio:SecondaryCategoryAxis"
    class_name: ClassVar[str] = "SecondaryCategoryAxis"
    class_model_uri: ClassVar[URIRef] = SIO.SecondaryCategoryAxis


class SecondaryStructureDescriptor(BiomolecularStructureDescriptor):
    """
    A secondary structure descriptor describes local topological patterns in  a biopolymer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SecondaryStructureDescriptor
    class_class_curie: ClassVar[str] = "sio:SecondaryStructureDescriptor"
    class_name: ClassVar[str] = "SecondaryStructureDescriptor"
    class_model_uri: ClassVar[URIRef] = SIO.SecondaryStructureDescriptor


class SeleniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SeleniumAtom
    class_class_curie: ClassVar[str] = "sio:SeleniumAtom"
    class_name: ClassVar[str] = "SeleniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.SeleniumAtom


class Sentence(Phrase):
    """
    A sentence is a grammatical unit consisting of one or more words that bear minimal syntactic relation to the words
    that precede or follow it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sentence
    class_class_curie: ClassVar[str] = "sio:Sentence"
    class_name: ClassVar[str] = "Sentence"
    class_model_uri: ClassVar[URIRef] = SIO.Sentence


class Clause(Sentence):
    """
    A clause consists of a subject and a predicate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Clause
    class_class_curie: ClassVar[str] = "sio:Clause"
    class_name: ClassVar[str] = "Clause"
    class_model_uri: ClassVar[URIRef] = SIO.Clause


class Question(Sentence):
    """
    A question is a linguistic expression used to make a request for information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Question
    class_class_curie: ClassVar[str] = "sio:Question"
    class_name: ClassVar[str] = "Question"
    class_model_uri: ClassVar[URIRef] = SIO.Question


class SequenceAssembly(BiopolymerSequence):
    """
    A sequence assembly is a sequence that is produced as by the alignment of two or more sequences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceAssembly
    class_class_curie: ClassVar[str] = "sio:SequenceAssembly"
    class_name: ClassVar[str] = "SequenceAssembly"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceAssembly


class SequenceMotif(Pattern):
    """
    A sequence motif is a pattern of nucleotides in a DNA sequence or amino acids in a protein.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceMotif
    class_class_curie: ClassVar[str] = "sio:SequenceMotif"
    class_name: ClassVar[str] = "SequenceMotif"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceMotif


class SequenceProfile(Pattern):
    """
    A sequence profile is provides the preference for a character at each position of an abstracted sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceProfile
    class_class_curie: ClassVar[str] = "sio:SequenceProfile"
    class_name: ClassVar[str] = "SequenceProfile"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceProfile


class Set(MathematicalEntity):
    """
    A set is a collection of entities, for which there may be zero members.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Set
    class_class_curie: ClassVar[str] = "sio:Set"
    class_name: ClassVar[str] = "Set"
    class_model_uri: ClassVar[URIRef] = SIO.Set


class Class(Set):
    """
    A class is a collection of sets which can be unambiguously defined by a property that all its members share.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Class
    class_class_curie: ClassVar[str] = "sio:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = SIO.Class


@dataclass
class Collection(Set):
    """
    A collection is a set for which there exists at least one member, although any member need not to exist at any
    point in the collection's existence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Collection
    class_class_curie: ClassVar[str] = "sio:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = SIO.Collection

    hasMember: Optional[Union[dict, "Entity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasMember is not None and not isinstance(self.hasMember, Entity):
            self.hasMember = Entity(**as_dict(self.hasMember))

        super().__post_init__(**kwargs)


class ACollectionOfDuplicates(Collection):
    """
    a collection of duplicates is a collection composed of items that are an exact copy of other items in the
    collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ACollectionOfDuplicates
    class_class_curie: ClassVar[str] = "sio:ACollectionOfDuplicates"
    class_name: ClassVar[str] = "ACollectionOfDuplicates"
    class_model_uri: ClassVar[URIRef] = SIO.ACollectionOfDuplicates


class ACollectionOfReplicates(Collection):
    """
    a collection of replicates is a collection composed of items that are a facsimile, reproduction, or copy of other
    items in the collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ACollectionOfReplicates
    class_class_curie: ClassVar[str] = "sio:ACollectionOfReplicates"
    class_name: ClassVar[str] = "ACollectionOfReplicates"
    class_model_uri: ClassVar[URIRef] = SIO.ACollectionOfReplicates


class Catalog(Collection):
    """
    A catalog is a systemic collection of items of the same type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Catalog
    class_class_curie: ClassVar[str] = "sio:Catalog"
    class_name: ClassVar[str] = "Catalog"
    class_model_uri: ClassVar[URIRef] = SIO.Catalog


class CollectionOf3dMolecularStructureModels(Collection):
    """
    A collection of 3D molecular structure models is just that.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CollectionOf3dMolecularStructureModels
    class_class_curie: ClassVar[str] = "sio:CollectionOf3dMolecularStructureModels"
    class_name: ClassVar[str] = "CollectionOf3dMolecularStructureModels"
    class_model_uri: ClassVar[URIRef] = SIO.CollectionOf3dMolecularStructureModels


class CollectionOfDocuments(Collection):
    """
    A collection of documents is a non-zero set of documents.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CollectionOfDocuments
    class_class_curie: ClassVar[str] = "sio:CollectionOfDocuments"
    class_name: ClassVar[str] = "CollectionOfDocuments"
    class_model_uri: ClassVar[URIRef] = SIO.CollectionOfDocuments


class BookSeries(CollectionOfDocuments):
    """
    A book series is a collection of books that have been sequentially published.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BookSeries
    class_class_curie: ClassVar[str] = "sio:BookSeries"
    class_name: ClassVar[str] = "BookSeries"
    class_model_uri: ClassVar[URIRef] = SIO.BookSeries


class CollectionOfPoints(Collection):
    """
    A collection of points is a geometric entity that contains a non-zero set of geometric points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CollectionOfPoints
    class_class_curie: ClassVar[str] = "sio:CollectionOfPoints"
    class_name: ClassVar[str] = "CollectionOfPoints"
    class_model_uri: ClassVar[URIRef] = SIO.CollectionOfPoints


class EmptySet(Set):
    """
    An empty set is a set for which there are exactly 0 members.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EmptySet
    class_class_curie: ClassVar[str] = "sio:EmptySet"
    class_name: ClassVar[str] = "EmptySet"
    class_model_uri: ClassVar[URIRef] = SIO.EmptySet


class List(Set):
    """
    A list is any enumeration of a set of items.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.List
    class_class_curie: ClassVar[str] = "sio:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = SIO.List


class DataSeries(List):
    """
    A data series is a data set composed of related values displayed in a statistical graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DataSeries
    class_class_curie: ClassVar[str] = "sio:DataSeries"
    class_name: ClassVar[str] = "DataSeries"
    class_model_uri: ClassVar[URIRef] = SIO.DataSeries


class Intersection(List):
    """
    An intersection is a list of only the values of an attribute for the entities in the defined set where all
    entities have that value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Intersection
    class_class_curie: ClassVar[str] = "sio:Intersection"
    class_name: ClassVar[str] = "Intersection"
    class_model_uri: ClassVar[URIRef] = SIO.Intersection


class OrderedList(List):
    """
    an ordered list is a list in which items are sequentially ordered.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrderedList
    class_class_curie: ClassVar[str] = "sio:OrderedList"
    class_name: ClassVar[str] = "OrderedList"
    class_model_uri: ClassVar[URIRef] = SIO.OrderedList


class AuthorList(OrderedList):
    """
    an ordered list of authors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AuthorList
    class_class_curie: ClassVar[str] = "sio:AuthorList"
    class_name: ClassVar[str] = "AuthorList"
    class_model_uri: ClassVar[URIRef] = SIO.AuthorList


class Periodical(CollectionOfDocuments):
    """
    A periodical is a publication that appears on a regular schedule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Periodical
    class_class_curie: ClassVar[str] = "sio:Periodical"
    class_name: ClassVar[str] = "Periodical"
    class_model_uri: ClassVar[URIRef] = SIO.Periodical


class Journal(Periodical):
    """
    A journal is a a peer-reviewed periodical in which scholarship relating to a particular academic discipline is
    published.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Journal
    class_class_curie: ClassVar[str] = "sio:Journal"
    class_name: ClassVar[str] = "Journal"
    class_model_uri: ClassVar[URIRef] = SIO.Journal


class Magazine(Periodical):
    """
    A magazine is a periodical that typically contains essays, stories, poems, etc., by many writers, and often
    photographs and drawings, frequently specializing in a particular subject or area, as hobbies, news, or sports.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Magazine
    class_class_curie: ClassVar[str] = "sio:Magazine"
    class_name: ClassVar[str] = "Magazine"
    class_model_uri: ClassVar[URIRef] = SIO.Magazine


class Newspaper(Periodical):
    """
    A newspaper is a periodical publication containing news regarding current events, informative articles, diverse
    features, editorials, and advertising.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Newspaper
    class_class_curie: ClassVar[str] = "sio:Newspaper"
    class_name: ClassVar[str] = "Newspaper"
    class_model_uri: ClassVar[URIRef] = SIO.Newspaper


class ProteinFamily(Collection):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinFamily
    class_class_curie: ClassVar[str] = "sio:ProteinFamily"
    class_name: ClassVar[str] = "ProteinFamily"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinFamily


class Sequence(List):
    """
    A sequence is an ordered list of entities. Like a set, it contains members (also called elements, or terms).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sequence
    class_class_curie: ClassVar[str] = "sio:Sequence"
    class_name: ClassVar[str] = "Sequence"
    class_model_uri: ClassVar[URIRef] = SIO.Sequence


class SequenceAlignment(Collection):
    """
    A sequence alignment is the character-based alignment of sequences using some method.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceAlignment
    class_class_curie: ClassVar[str] = "sio:SequenceAlignment"
    class_name: ClassVar[str] = "SequenceAlignment"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceAlignment


class MultipleSequenceAlignment(SequenceAlignment):
    """
    A multiple sequence alignment is a sequence alignment involving more than two sequences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MultipleSequenceAlignment
    class_class_curie: ClassVar[str] = "sio:MultipleSequenceAlignment"
    class_name: ClassVar[str] = "MultipleSequenceAlignment"
    class_model_uri: ClassVar[URIRef] = SIO.MultipleSequenceAlignment


class PairwiseSequenceAlignment(SequenceAlignment):
    """
    A pairwise sequence alignment is the alignment of exactly 2 sequences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PairwiseSequenceAlignment
    class_class_curie: ClassVar[str] = "sio:PairwiseSequenceAlignment"
    class_name: ClassVar[str] = "PairwiseSequenceAlignment"
    class_model_uri: ClassVar[URIRef] = SIO.PairwiseSequenceAlignment


class SetItem(MathematicalEntity):
    """
    set item is an item in a set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SetItem
    class_class_curie: ClassVar[str] = "sio:SetItem"
    class_name: ClassVar[str] = "SetItem"
    class_model_uri: ClassVar[URIRef] = SIO.SetItem


class CollectionItem(SetItem):
    """
    a collection item is an item in a collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CollectionItem
    class_class_curie: ClassVar[str] = "sio:CollectionItem"
    class_name: ClassVar[str] = "CollectionItem"
    class_model_uri: ClassVar[URIRef] = SIO.CollectionItem


class Duplicate(CollectionItem):
    """
    a duplicate is an object that is an exact copy of another item
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Duplicate
    class_class_curie: ClassVar[str] = "sio:Duplicate"
    class_name: ClassVar[str] = "Duplicate"
    class_model_uri: ClassVar[URIRef] = SIO.Duplicate


class ListItem(SetItem):
    """
    a list item is an item in a list.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ListItem
    class_class_curie: ClassVar[str] = "sio:ListItem"
    class_name: ClassVar[str] = "ListItem"
    class_model_uri: ClassVar[URIRef] = SIO.ListItem


class OrderedListItem(ListItem):
    """
    an ordered list item is an item in an ordered list.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrderedListItem
    class_class_curie: ClassVar[str] = "sio:OrderedListItem"
    class_name: ClassVar[str] = "OrderedListItem"
    class_model_uri: ClassVar[URIRef] = SIO.OrderedListItem


class Replicate(CollectionItem):
    """
    a replicate is an object that is a facsimile, reproduction, or copy of another item.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Replicate
    class_class_curie: ClassVar[str] = "sio:Replicate"
    class_name: ClassVar[str] = "Replicate"
    class_model_uri: ClassVar[URIRef] = SIO.Replicate


class Severe(Intensity):
    """
    severe is a qualitative intensity value that is more intense than strong, but less intense than fatal.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Severe
    class_class_curie: ClassVar[str] = "sio:Severe"
    class_name: ClassVar[str] = "Severe"
    class_model_uri: ClassVar[URIRef] = SIO.Severe


class Shame(NegativeEmotion):
    """
    shame is the emotion borne from feeling responsible for the commission of an offense.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Shame
    class_class_curie: ClassVar[str] = "sio:Shame"
    class_name: ClassVar[str] = "Shame"
    class_model_uri: ClassVar[URIRef] = SIO.Shame


class Shape(ObjectQuality):
    """
    shape is the quality of a bearer that relates to its spatial extent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Shape
    class_class_curie: ClassVar[str] = "sio:Shape"
    class_name: ClassVar[str] = "Shape"
    class_model_uri: ClassVar[URIRef] = SIO.Shape


class Curvature(Shape):
    """
    curvature is a quality of a bearer that relates to the presence of curves, bends, or angles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Curvature
    class_class_curie: ClassVar[str] = "sio:Curvature"
    class_name: ClassVar[str] = "Curvature"
    class_model_uri: ClassVar[URIRef] = SIO.Curvature


class Bent(Curvature):
    """
    bent is the quality of a line being sharply curved or having an angle.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Bent
    class_class_curie: ClassVar[str] = "sio:Bent"
    class_name: ClassVar[str] = "Bent"
    class_model_uri: ClassVar[URIRef] = SIO.Bent


class Curved(Curvature):
    """
    curved is the quality of a line that deviates from straightness in a smooth, continuous fashion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Curved
    class_class_curie: ClassVar[str] = "sio:Curved"
    class_name: ClassVar[str] = "Curved"
    class_model_uri: ClassVar[URIRef] = SIO.Curved


class Shock(NegativeEmotion):
    """
    shock is an emotion of sudden upset or surprise.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Shock
    class_class_curie: ClassVar[str] = "sio:Shock"
    class_name: ClassVar[str] = "Shock"
    class_model_uri: ClassVar[URIRef] = SIO.Shock


class Shyness(NegativeEmotion):
    """
    shyness is an emotion of apprehension, lack of comfort, or awkwardness experienced when in proximity to,
    approaching, or being approached by other individuals, especially in new situations or with unfamiliar
    individuals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Shyness
    class_class_curie: ClassVar[str] = "sio:Shyness"
    class_name: ClassVar[str] = "Shyness"
    class_model_uri: ClassVar[URIRef] = SIO.Shyness


class Sick(Alive):
    """
    sick is the status of a living organism that is behaving at a sub-optimal level.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sick
    class_class_curie: ClassVar[str] = "sio:Sick"
    class_name: ClassVar[str] = "Sick"
    class_model_uri: ClassVar[URIRef] = SIO.Sick


class SignLanguage(Language):
    """
    A sign language (also signed language) is a language that involves manual communication and body language to
    convey meaning. This can involve simultaneously combining hand shapes, orientation and movement of the hands, arms
    or body, and facial expressions to fluidly express a speaker's thoughts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SignLanguage
    class_class_curie: ClassVar[str] = "sio:SignLanguage"
    class_name: ClassVar[str] = "SignLanguage"
    class_model_uri: ClassVar[URIRef] = SIO.SignLanguage


class Signal(Molecule):
    """
    A signal is an object that initiates a sequence of events.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Signal
    class_class_curie: ClassVar[str] = "sio:Signal"
    class_name: ClassVar[str] = "Signal"
    class_model_uri: ClassVar[URIRef] = SIO.Signal


class SignalTransducer(Molecule):
    """
    A signal transducer is a molecule that responds to and amplifies a signal in a signalling system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SignalTransducer
    class_class_curie: ClassVar[str] = "sio:SignalTransducer"
    class_name: ClassVar[str] = "SignalTransducer"
    class_model_uri: ClassVar[URIRef] = SIO.SignalTransducer


class Messenger(SignalTransducer):
    """
    A mesenger is a molecule involved in either signal detection or signal propagation from receptors on the cell
    surface to target molecules inside the cell, in the cytoplasm or nucleus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Messenger
    class_class_curie: ClassVar[str] = "sio:Messenger"
    class_name: ClassVar[str] = "Messenger"
    class_model_uri: ClassVar[URIRef] = SIO.Messenger


class Receptor(SignalTransducer):
    """
    A receptor molecule is a molecule that has the capability to bind to a signal and propogate a response to that
    signal.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Receptor
    class_class_curie: ClassVar[str] = "sio:Receptor"
    class_name: ClassVar[str] = "Receptor"
    class_model_uri: ClassVar[URIRef] = SIO.Receptor


class SecondMessenger(Messenger):
    """
    A second messenger is a molecule that relay signals from receptors on the cell surface to target molecules inside
    the cell, in the cytoplasm or nucleus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SecondMessenger
    class_class_curie: ClassVar[str] = "sio:SecondMessenger"
    class_name: ClassVar[str] = "SecondMessenger"
    class_model_uri: ClassVar[URIRef] = SIO.SecondMessenger


class SiliconAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SiliconAtom
    class_class_curie: ClassVar[str] = "sio:SiliconAtom"
    class_name: ClassVar[str] = "SiliconAtom"
    class_model_uri: ClassVar[URIRef] = SIO.SiliconAtom


class SilverAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SilverAtom
    class_class_curie: ClassVar[str] = "sio:SilverAtom"
    class_name: ClassVar[str] = "SilverAtom"
    class_model_uri: ClassVar[URIRef] = SIO.SilverAtom


class SingleArrowedLineSegment(ArrowedLineSegment):
    """
    A single arrowed line is directed line in which the endpoint is tangentially part of a triangle that bisects the
    line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SingleArrowedLineSegment
    class_class_curie: ClassVar[str] = "sio:SingleArrowedLineSegment"
    class_name: ClassVar[str] = "SingleArrowedLineSegment"
    class_model_uri: ClassVar[URIRef] = SIO.SingleArrowedLineSegment


class SingleDisplacementReaction(DisplacementReaction):
    """
    A single displacement reaction where one atom is transferred out of one molecule and into another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SingleDisplacementReaction
    class_class_curie: ClassVar[str] = "sio:SingleDisplacementReaction"
    class_name: ClassVar[str] = "SingleDisplacementReaction"
    class_model_uri: ClassVar[URIRef] = SIO.SingleDisplacementReaction


class Slide(Media):
    """
    A slide is an visual representation meant to communicate some information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Slide
    class_class_curie: ClassVar[str] = "sio:Slide"
    class_name: ClassVar[str] = "Slide"
    class_model_uri: ClassVar[URIRef] = SIO.Slide


class Slideshow(Media):
    """
    A slideshow is a visual presentation of information contained within a collection of slides.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Slideshow
    class_class_curie: ClassVar[str] = "sio:Slideshow"
    class_name: ClassVar[str] = "Slideshow"
    class_model_uri: ClassVar[URIRef] = SIO.Slideshow


class SmallCytoplasmicRNAscRNA(Non-proteinCodingRNAncRNA):
    """
    A small cytoplasmic RNA (scRNA) molecule is a small (7S; 129 nucleotides) RNA molecule found in the cytosol and
    rough endoplasmic reticulum that are normally associated with proteins that are involved in specific selection and
    transport of other proteins.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SmallCytoplasmicRNAscRNA
    class_class_curie: ClassVar[str] = "sio:SmallCytoplasmicRNAscRNA"
    class_name: ClassVar[str] = "SmallCytoplasmicRNAscRNA"
    class_model_uri: ClassVar[URIRef] = SIO.SmallCytoplasmicRNAscRNA


class SmallNuclearRNAsnRNA(Non-proteinCodingRNAncRNA):
    """
    A small nuclear RNA (snRNA) is a small RNA molecule that is located in the nucleus of a cell.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SmallNuclearRNAsnRNA
    class_class_curie: ClassVar[str] = "sio:SmallNuclearRNAsnRNA"
    class_name: ClassVar[str] = "SmallNuclearRNAsnRNA"
    class_model_uri: ClassVar[URIRef] = SIO.SmallNuclearRNAsnRNA


class SmallNucleolarRNAsnoRNA(Non-proteinCodingRNAncRNA):
    """
    A small nucleolar RNA (snoRNA) is a small RNA that are associated with the eukaryotic nucleus as components of
    small nucleolar ribonucleoproteins.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SmallNucleolarRNAsnoRNA
    class_class_curie: ClassVar[str] = "sio:SmallNucleolarRNAsnoRNA"
    class_name: ClassVar[str] = "SmallNucleolarRNAsnoRNA"
    class_model_uri: ClassVar[URIRef] = SIO.SmallNucleolarRNAsnoRNA


class SocialEntity(InformationContentEntity):
    """
    A social entity pertains to the interaction among individuals and groups.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SocialEntity
    class_class_curie: ClassVar[str] = "sio:SocialEntity"
    class_name: ClassVar[str] = "SocialEntity"
    class_model_uri: ClassVar[URIRef] = SIO.SocialEntity


class SocialRelation(SocialEntity):
    """
    A social relation is a social entity that describes a relationship  between two or more individuals or groups.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SocialRelation
    class_class_curie: ClassVar[str] = "sio:SocialRelation"
    class_name: ClassVar[str] = "SocialRelation"
    class_model_uri: ClassVar[URIRef] = SIO.SocialRelation


class Affiliation(SocialRelation):
    """
    An affiliation is a social relation which indicates the partnership between two or more entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Affiliation
    class_class_curie: ClassVar[str] = "sio:Affiliation"
    class_name: ClassVar[str] = "Affiliation"
    class_model_uri: ClassVar[URIRef] = SIO.Affiliation


class SocialRole(Role):
    """
    A social role is a role that is ascribed to individuals in a community.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SocialRole
    class_class_curie: ClassVar[str] = "sio:SocialRole"
    class_name: ClassVar[str] = "SocialRole"
    class_model_uri: ClassVar[URIRef] = SIO.SocialRole


class OccupationalRole(SocialRole):
    """
    An occupational role is a social role that pertains to an organizational structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OccupationalRole
    class_class_curie: ClassVar[str] = "sio:OccupationalRole"
    class_name: ClassVar[str] = "OccupationalRole"
    class_model_uri: ClassVar[URIRef] = SIO.OccupationalRole


class AcademicRole(OccupationalRole):
    """
    An academic role is a social role that pertains to the academic institution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AcademicRole
    class_class_curie: ClassVar[str] = "sio:AcademicRole"
    class_name: ClassVar[str] = "AcademicRole"
    class_model_uri: ClassVar[URIRef] = SIO.AcademicRole


class AdministrativeRole(OccupationalRole):
    """
    An administrative role is the role of an individual that performs administrative tasks for some organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AdministrativeRole
    class_class_curie: ClassVar[str] = "sio:AdministrativeRole"
    class_name: ClassVar[str] = "AdministrativeRole"
    class_model_uri: ClassVar[URIRef] = SIO.AdministrativeRole


class DepartmentChairRole(AcademicRole):
    """
    A department chain role is the role of an individual that heads a department at a academic organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DepartmentChairRole
    class_class_curie: ClassVar[str] = "sio:DepartmentChairRole"
    class_name: ClassVar[str] = "DepartmentChairRole"
    class_model_uri: ClassVar[URIRef] = SIO.DepartmentChairRole


class MedicalRole(OccupationalRole):
    """
    A medical role is the role of an individual that is a participant in the delivery of medical care.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalRole
    class_class_curie: ClassVar[str] = "sio:MedicalRole"
    class_name: ClassVar[str] = "MedicalRole"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalRole


class DentistRole(MedicalRole):
    """
    A dentist role is the role of an individual that that specializes in the diagnosis, prevention, and treatment of
    diseases and conditions of the oral cavity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DentistRole
    class_class_curie: ClassVar[str] = "sio:DentistRole"
    class_name: ClassVar[str] = "DentistRole"
    class_model_uri: ClassVar[URIRef] = SIO.DentistRole


class DoctorRole(MedicalRole):
    """
    A doctor role is the role of an individual who practices medicine, which is concerned with promoting, maintaining
    or restoring human health through the study, diagnosis, and treatment of disease, injury, and other physical and
    mental impairments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DoctorRole
    class_class_curie: ClassVar[str] = "sio:DoctorRole"
    class_name: ClassVar[str] = "DoctorRole"
    class_model_uri: ClassVar[URIRef] = SIO.DoctorRole


class NurseRole(MedicalRole):
    """
    A nurse role is the role of an individual that is involved in the protection, promotion, and optimization of
    health and abilities, prevention of illness and injury, alleviation of suffering through the diagnosis and
    treatment of human response, and advocacy in the care of individuals, families, communities, and populations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NurseRole
    class_class_curie: ClassVar[str] = "sio:NurseRole"
    class_name: ClassVar[str] = "NurseRole"
    class_model_uri: ClassVar[URIRef] = SIO.NurseRole


class PatientRole(MedicalRole):
    """
    A patient role is the role of an individual that is the recepient of medical care.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PatientRole
    class_class_curie: ClassVar[str] = "sio:PatientRole"
    class_name: ClassVar[str] = "PatientRole"
    class_model_uri: ClassVar[URIRef] = SIO.PatientRole


class ProfessorRole(AcademicRole):
    """
    A professor role is the role of an individual that is involved in teaching of students (undergraduate and/or
    graduate) at a post-secondary academic institution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProfessorRole
    class_class_curie: ClassVar[str] = "sio:ProfessorRole"
    class_name: ClassVar[str] = "ProfessorRole"
    class_model_uri: ClassVar[URIRef] = SIO.ProfessorRole


class PublishingRole(OccupationalRole):
    """
    A publishing role is the role of an individual that is involved in the preparation and issue of creative works for
    consumption by a wider audience.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PublishingRole
    class_class_curie: ClassVar[str] = "sio:PublishingRole"
    class_name: ClassVar[str] = "PublishingRole"
    class_model_uri: ClassVar[URIRef] = SIO.PublishingRole


class AuthorRole(PublishingRole):
    """
    An author role is the role of an individual that creates a creative, written work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AuthorRole
    class_class_curie: ClassVar[str] = "sio:AuthorRole"
    class_name: ClassVar[str] = "AuthorRole"
    class_model_uri: ClassVar[URIRef] = SIO.AuthorRole


class PublisherRole(PublishingRole):
    """
    A publisher role is the role of an individual that prepares and issues creative works.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PublisherRole
    class_class_curie: ClassVar[str] = "sio:PublisherRole"
    class_name: ClassVar[str] = "PublisherRole"
    class_model_uri: ClassVar[URIRef] = SIO.PublisherRole


class SecretaryRole(AdministrativeRole):
    """
    A secretary role is the role of an individual that performs administrative tasks to support one or more
    individuals of the same organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SecretaryRole
    class_class_curie: ClassVar[str] = "sio:SecretaryRole"
    class_name: ClassVar[str] = "SecretaryRole"
    class_model_uri: ClassVar[URIRef] = SIO.SecretaryRole


class SocialStructure(SocialEntity):
    """
    A social structure is a social entity which consists of relationships between two or more entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SocialStructure
    class_class_curie: ClassVar[str] = "sio:SocialStructure"
    class_name: ClassVar[str] = "SocialStructure"
    class_model_uri: ClassVar[URIRef] = SIO.SocialStructure


class Collective(SocialStructure):
    """
    A collective is a group of entities that share or are motivated by at least one common issue or interest, or work
    together on a specific project(s) to achieve a common objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Collective
    class_class_curie: ClassVar[str] = "sio:Collective"
    class_name: ClassVar[str] = "Collective"
    class_model_uri: ClassVar[URIRef] = SIO.Collective


class Community(Collective):
    """
    A community is a sizeable social unit that shares common values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Community
    class_class_curie: ClassVar[str] = "sio:Community"
    class_name: ClassVar[str] = "Community"
    class_model_uri: ClassVar[URIRef] = SIO.Community


class Family(Collective):
    """
    A group of people affiliated by consanguinity, affinity, or co-residence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Family
    class_class_curie: ClassVar[str] = "sio:Family"
    class_name: ClassVar[str] = "Family"
    class_model_uri: ClassVar[URIRef] = SIO.Family


class Organization(Collective):
    """
    An organization is a collective with a complex articulation of tasks, roles and responsibilities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Organization
    class_class_curie: ClassVar[str] = "sio:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = SIO.Organization


class AcademicOrganization(Organization):
    """
    An academic organization is a lawfully recognized organization that confers diplomas, degrees and other forms of
    recognition of academic achievement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AcademicOrganization
    class_class_curie: ClassVar[str] = "sio:AcademicOrganization"
    class_name: ClassVar[str] = "AcademicOrganization"
    class_model_uri: ClassVar[URIRef] = SIO.AcademicOrganization


class AcademicDepartment(AcademicOrganization):
    """
    An academic department is a division of a university or school faculty devoted to a particular academic discipline.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AcademicDepartment
    class_class_curie: ClassVar[str] = "sio:AcademicDepartment"
    class_name: ClassVar[str] = "AcademicDepartment"
    class_model_uri: ClassVar[URIRef] = SIO.AcademicDepartment


class Corporation(Organization):
    """
    A corporation is an organization that is granted a charter recognizing it as a separate legal entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Corporation
    class_class_curie: ClassVar[str] = "sio:Corporation"
    class_name: ClassVar[str] = "Corporation"
    class_model_uri: ClassVar[URIRef] = SIO.Corporation


class Institute(Organization):
    """
    institute is a society or organization having a object or common factor, and is normally applied to those with a
    scientific, educational, or social objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Institute
    class_class_curie: ClassVar[str] = "sio:Institute"
    class_name: ClassVar[str] = "Institute"
    class_model_uri: ClassVar[URIRef] = SIO.Institute


class Population(Collective):
    """
    A population is all the organisms that both belong to the same group or species and live in the same geographical
    area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Population
    class_class_curie: ClassVar[str] = "sio:Population"
    class_name: ClassVar[str] = "Population"
    class_model_uri: ClassVar[URIRef] = SIO.Population


class HumanPopulation(Population):
    """
    A human population refers to a collection of human beings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HumanPopulation
    class_class_curie: ClassVar[str] = "sio:HumanPopulation"
    class_name: ClassVar[str] = "HumanPopulation"
    class_model_uri: ClassVar[URIRef] = SIO.HumanPopulation


class EthnicGroup(HumanPopulation):
    """
    An ethnic group is a group of people whose members identify with each other through a common heritage, consisting
    of a common culture, including a shared language or dialect.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EthnicGroup
    class_class_curie: ClassVar[str] = "sio:EthnicGroup"
    class_name: ClassVar[str] = "EthnicGroup"
    class_model_uri: ClassVar[URIRef] = SIO.EthnicGroup


class RegulatoryAuthority(Organization):
    """
    A regulatory authority is an organization responsible for exercising regulatory or supervisory capacity in some
    area of human activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulatoryAuthority
    class_class_curie: ClassVar[str] = "sio:RegulatoryAuthority"
    class_name: ClassVar[str] = "RegulatoryAuthority"
    class_model_uri: ClassVar[URIRef] = SIO.RegulatoryAuthority


class DrugRegulatoryAuthority(RegulatoryAuthority):
    """
    A drug regulatory authority is a regulatory authority which acts to control what substances may be used to treat
    individuals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DrugRegulatoryAuthority
    class_class_curie: ClassVar[str] = "sio:DrugRegulatoryAuthority"
    class_name: ClassVar[str] = "DrugRegulatoryAuthority"
    class_model_uri: ClassVar[URIRef] = SIO.DrugRegulatoryAuthority


class SodiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SodiumAtom
    class_class_curie: ClassVar[str] = "sio:SodiumAtom"
    class_name: ClassVar[str] = "SodiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.SodiumAtom


class SoftwareEntity(ComputationalEntity):
    """
    A software entity is a computational entity that can be interpreted by or directly executed by a processing unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareEntity
    class_class_curie: ClassVar[str] = "sio:SoftwareEntity"
    class_name: ClassVar[str] = "SoftwareEntity"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareEntity


class SoftwareApplication(SoftwareEntity):
    """
    A software application is software that can be directly executed by some processing unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareApplication
    class_class_curie: ClassVar[str] = "sio:SoftwareApplication"
    class_name: ClassVar[str] = "SoftwareApplication"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareApplication


class SoftwareInterpreter(SoftwareApplication):
    """
    A software interpreter is a software application that executes some specified input software.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareInterpreter
    class_class_curie: ClassVar[str] = "sio:SoftwareInterpreter"
    class_name: ClassVar[str] = "SoftwareInterpreter"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareInterpreter


class SoftwareLibrary(SoftwareEntity):
    """
    A software library is software composed of a collection of software modules and/or software methods in a form that
    can be statically or dynamically linked to some software application.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareLibrary
    class_class_curie: ClassVar[str] = "sio:SoftwareLibrary"
    class_name: ClassVar[str] = "SoftwareLibrary"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareLibrary


class SoftwareMethod(SoftwareEntity):
    """
    A software method (also called subroutine, subprogram, procedure, method, function, or routine) is software
    designed to execute a specific task.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareMethod
    class_class_curie: ClassVar[str] = "sio:SoftwareMethod"
    class_name: ClassVar[str] = "SoftwareMethod"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareMethod


class SoftwareModule(SoftwareEntity):
    """
    A software module is software composed of a collection of software methods.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareModule
    class_class_curie: ClassVar[str] = "sio:SoftwareModule"
    class_name: ClassVar[str] = "SoftwareModule"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareModule


class SoftwareScript(SoftwareEntity):
    """
    A software script is software whose instructions can be executed using a software interpreter.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareScript
    class_class_curie: ClassVar[str] = "sio:SoftwareScript"
    class_name: ClassVar[str] = "SoftwareScript"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareScript


class SofwareExecution(InformationProcessing):
    """
    software execution is the process of executing software on a computing device.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SofwareExecution
    class_class_curie: ClassVar[str] = "sio:SofwareExecution"
    class_name: ClassVar[str] = "SofwareExecution"
    class_model_uri: ClassVar[URIRef] = SIO.SofwareExecution


class SolidStateHardDrive(HardDiskDrive):
    """
    A solid-state drive (SSD) is a data storage device that uses solid-state memory to store persistent data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SolidStateHardDrive
    class_class_curie: ClassVar[str] = "sio:SolidStateHardDrive"
    class_name: ClassVar[str] = "SolidStateHardDrive"
    class_model_uri: ClassVar[URIRef] = SIO.SolidStateHardDrive


class Solute(LiquidSolutionComponent):
    """
    A solute is a substance that becomes dissolved in a solvent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Solute
    class_class_curie: ClassVar[str] = "sio:Solute"
    class_name: ClassVar[str] = "Solute"
    class_model_uri: ClassVar[URIRef] = SIO.Solute


class Solvent(LiquidSolutionComponent):
    """
    A solvent is a substance that can dissolve other substances (solutes).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Solvent
    class_class_curie: ClassVar[str] = "sio:Solvent"
    class_name: ClassVar[str] = "Solvent"
    class_model_uri: ClassVar[URIRef] = SIO.Solvent


class NonpolarSolvent(Solvent):
    """
    A non-polar solvent is a solvent that exhibits a non-polar quality.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NonpolarSolvent
    class_class_curie: ClassVar[str] = "sio:NonpolarSolvent"
    class_name: ClassVar[str] = "NonpolarSolvent"
    class_model_uri: ClassVar[URIRef] = SIO.NonpolarSolvent


class PolarSolvent(Solvent):
    """
    A polar solvent is a solvent that exhibits a polar quality.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolarSolvent
    class_class_curie: ClassVar[str] = "sio:PolarSolvent"
    class_name: ClassVar[str] = "PolarSolvent"
    class_model_uri: ClassVar[URIRef] = SIO.PolarSolvent


class Sorrow(Sadness):
    """
    sorrow is the emotion that is characterized by a long term state of intense sadness, distress and a degree of
    resignation (not accepting).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sorrow
    class_class_curie: ClassVar[str] = "sio:Sorrow"
    class_name: ClassVar[str] = "Sorrow"
    class_model_uri: ClassVar[URIRef] = SIO.Sorrow


class SpatialRegion(Object):
    """
    A spatial region is an object contained in some region of space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpatialRegion
    class_class_curie: ClassVar[str] = "sio:SpatialRegion"
    class_name: ClassVar[str] = "SpatialRegion"
    class_model_uri: ClassVar[URIRef] = SIO.SpatialRegion


class GeographicRegion(SpatialRegion):
    """
    A geographic region is a spatial region whose boundaries are typically defined against some material frame of
    reference (like the earth).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeographicRegion
    class_class_curie: ClassVar[str] = "sio:GeographicRegion"
    class_name: ClassVar[str] = "GeographicRegion"
    class_model_uri: ClassVar[URIRef] = SIO.GeographicRegion


class Environment(GeographicRegion):
    """
    An environment is a geographic region that hosts certain processes or objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Environment
    class_class_curie: ClassVar[str] = "sio:Environment"
    class_name: ClassVar[str] = "Environment"
    class_model_uri: ClassVar[URIRef] = SIO.Environment


class GeolegalRegion(GeographicRegion):
    """
    A geolegal region is a geographic region which has causal powers confered by a legal entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeolegalRegion
    class_class_curie: ClassVar[str] = "sio:GeolegalRegion"
    class_name: ClassVar[str] = "GeolegalRegion"
    class_model_uri: ClassVar[URIRef] = SIO.GeolegalRegion


class GeopoliticalRegion(GeolegalRegion):
    """
    a geopolitical region is a geographic region recognized by social or legal convention.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeopoliticalRegion
    class_class_curie: ClassVar[str] = "sio:GeopoliticalRegion"
    class_name: ClassVar[str] = "GeopoliticalRegion"
    class_model_uri: ClassVar[URIRef] = SIO.GeopoliticalRegion


class City(GeopoliticalRegion):
    """
    A city is a relatively large and permanent settlement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.City
    class_class_curie: ClassVar[str] = "sio:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = SIO.City


class Country(GeopoliticalRegion):
    """
    A country is a region legally identified as a distinct entity in political geography.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Country
    class_class_curie: ClassVar[str] = "sio:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = SIO.Country


class Province(GeopoliticalRegion):
    """
    A province is a territorial unit, almost always an administrative division, within a country or state.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Province
    class_class_curie: ClassVar[str] = "sio:Province"
    class_name: ClassVar[str] = "Province"
    class_model_uri: ClassVar[URIRef] = SIO.Province


class Site(SpatialRegion):
    """
    A site is a spatial region bounded (in part or in whole) by material entities and may be occupied by material
    entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Site
    class_class_curie: ClassVar[str] = "sio:Site"
    class_name: ClassVar[str] = "Site"
    class_model_uri: ClassVar[URIRef] = SIO.Site


class Hole(Site):
    """
    A hole is a site that is opening into or through something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hole
    class_class_curie: ClassVar[str] = "sio:Hole"
    class_name: ClassVar[str] = "Hole"
    class_model_uri: ClassVar[URIRef] = SIO.Hole


class MolecularSite(Site):
    """
    A moleclar site is a spatial region bounded (in part or in whole) by a molecule and may be occupied by other
    material entities (e.g. drugs).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularSite
    class_class_curie: ClassVar[str] = "sio:MolecularSite"
    class_name: ClassVar[str] = "MolecularSite"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularSite


class ActiveSite(MolecularSite):
    """
    An active site is a molecular site in which a chemical event occurs (structural transformation or conformational
    change).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ActiveSite
    class_class_curie: ClassVar[str] = "sio:ActiveSite"
    class_name: ClassVar[str] = "ActiveSite"
    class_model_uri: ClassVar[URIRef] = SIO.ActiveSite


class BindingSite(MolecularSite):
    """
    A binding site is a molecular site which when occupied with particular ligands leads to structural transformations
    that initiatiate new moelcular processes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BindingSite
    class_class_curie: ClassVar[str] = "sio:BindingSite"
    class_name: ClassVar[str] = "BindingSite"
    class_model_uri: ClassVar[URIRef] = SIO.BindingSite


class AllostericSite(BindingSite):
    """
    An allosteric site is a binding site that when bound to particular ligand changes the conformational state and
    affects its functionality.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AllostericSite
    class_class_curie: ClassVar[str] = "sio:AllostericSite"
    class_name: ClassVar[str] = "AllostericSite"
    class_model_uri: ClassVar[URIRef] = SIO.AllostericSite


class MolecularPocket(MolecularSite):
    """
    A molecular pocket is a site on a molecule that appears as a depression into the structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularPocket
    class_class_curie: ClassVar[str] = "sio:MolecularPocket"
    class_name: ClassVar[str] = "MolecularPocket"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularPocket


class SpatialBoundary(SpatialRegion):
    """
    A spatial boundary is the closure minus the interior of a subset of a topological space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpatialBoundary
    class_class_curie: ClassVar[str] = "sio:SpatialBoundary"
    class_name: ClassVar[str] = "SpatialBoundary"
    class_model_uri: ClassVar[URIRef] = SIO.SpatialBoundary


class MaterialBoundary(SpatialBoundary):
    """
    A material boundary is the boundary of a material entity which exists as a lower dimensional entity at exactly the
    location where its parts no longer extend into space. Every material entity has a boundary, and a boundary is the
    boundary of exactly 1 material entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaterialBoundary
    class_class_curie: ClassVar[str] = "sio:MaterialBoundary"
    class_name: ClassVar[str] = "MaterialBoundary"
    class_model_uri: ClassVar[URIRef] = SIO.MaterialBoundary


class SpecializedObject(Object):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpecializedObject
    class_class_curie: ClassVar[str] = "sio:SpecializedObject"
    class_name: ClassVar[str] = "SpecializedObject"
    class_model_uri: ClassVar[URIRef] = SIO.SpecializedObject


class AnatomicalEntity(SpecializedObject):
    """
    an anatomical entity is an object that is a structural part (material or immaterial) of a biological entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AnatomicalEntity
    class_class_curie: ClassVar[str] = "sio:AnatomicalEntity"
    class_name: ClassVar[str] = "AnatomicalEntity"
    class_model_uri: ClassVar[URIRef] = SIO.AnatomicalEntity


class Person(SpecializedObject):
    """
    A person is an object that has certain capacities or attributes constituting personhood.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Person
    class_class_curie: ClassVar[str] = "sio:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = SIO.Person


class Academic(Person):
    """
    An academic is an individual that participates in education and scholarship.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Academic
    class_class_curie: ClassVar[str] = "sio:Academic"
    class_name: ClassVar[str] = "Academic"
    class_model_uri: ClassVar[URIRef] = SIO.Academic


class MedicalPractitioner(Person):
    """
    A medical practioner is an individual that provides medical care.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalPractitioner
    class_class_curie: ClassVar[str] = "sio:MedicalPractitioner"
    class_name: ClassVar[str] = "MedicalPractitioner"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalPractitioner


class Doctor(MedicalPractitioner):
    """
    A doctor is an individual who practices medicine, which is concerned with promoting, maintaining or restoring
    human health through the study, diagnosis, and treatment of disease, injury, and other physical and mental
    impairments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Doctor
    class_class_curie: ClassVar[str] = "sio:Doctor"
    class_name: ClassVar[str] = "Doctor"
    class_model_uri: ClassVar[URIRef] = SIO.Doctor


class Nurse(MedicalPractitioner):
    """
    A nurse is an individual that is involved in the protection, promotion, and optimization of health and abilities,
    prevention of illness and injury, alleviation of suffering through the diagnosis and treatment of human response,
    and advocacy in the care of individuals, families, communities, and populations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Nurse
    class_class_curie: ClassVar[str] = "sio:Nurse"
    class_name: ClassVar[str] = "Nurse"
    class_model_uri: ClassVar[URIRef] = SIO.Nurse


class Patient(Person):
    """
    A patient is an individual that is the recepient of medical care.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Patient
    class_class_curie: ClassVar[str] = "sio:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = SIO.Patient


class Professor(Academic):
    """
    A professor is an individual that is a scholarly teacher.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Professor
    class_class_curie: ClassVar[str] = "sio:Professor"
    class_name: ClassVar[str] = "Professor"
    class_model_uri: ClassVar[URIRef] = SIO.Professor


class SpecializedMaterialEntity(SpecializedObject):
    """
    A specialized material entity is a material entity that is defined by having some quality, role or capability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpecializedMaterialEntity
    class_class_curie: ClassVar[str] = "sio:SpecializedMaterialEntity"
    class_name: ClassVar[str] = "SpecializedMaterialEntity"
    class_model_uri: ClassVar[URIRef] = SIO.SpecializedMaterialEntity


class Specification(Description):
    """
    A specification is a description of the essential technical attributes/requirements for an object or procedure,
    and may be used to determine that the object / procedure meets its requirements/attributes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Specification
    class_class_curie: ClassVar[str] = "sio:Specification"
    class_name: ClassVar[str] = "Specification"
    class_model_uri: ClassVar[URIRef] = SIO.Specification


class ActionSpecification(Specification):
    """
    An action specification is a specification composed of a sequence of instructions to achieve some objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ActionSpecification
    class_class_curie: ClassVar[str] = "sio:ActionSpecification"
    class_name: ClassVar[str] = "ActionSpecification"
    class_model_uri: ClassVar[URIRef] = SIO.ActionSpecification


class ExperimentalProtocol(ActionSpecification):
    """
    An experimental protocol is an action specification with respect to the design and implementation of experiments.
    In addition to providing a detailed set of procedures and lists of required equipment and instruments,
    experimental protocols often include information on safety precautions, the calculation of results and reporting
    standards, including statistical analysis and rules for predefining and documenting excluded data to avoid bias.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ExperimentalProtocol
    class_class_curie: ClassVar[str] = "sio:ExperimentalProtocol"
    class_name: ClassVar[str] = "ExperimentalProtocol"
    class_model_uri: ClassVar[URIRef] = SIO.ExperimentalProtocol


class FunctionalSpecification(Specification):
    """
    A functional specification is a specification that describes the characteristics of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FunctionalSpecification
    class_class_curie: ClassVar[str] = "sio:FunctionalSpecification"
    class_name: ClassVar[str] = "FunctionalSpecification"
    class_model_uri: ClassVar[URIRef] = SIO.FunctionalSpecification


class Design(FunctionalSpecification):
    """
    A specification of an object, manifested by an agent, intended to accomplish goals, in a particular environment,
    using a set of primitive components, satisfying a set of requirements, subject to constraints.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Design
    class_class_curie: ClassVar[str] = "sio:Design"
    class_name: ClassVar[str] = "Design"
    class_model_uri: ClassVar[URIRef] = SIO.Design


class DesignSpecification(FunctionalSpecification):
    """
    A design specification is a specification that provides precise and explicit information about the requirements
    for a product design.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DesignSpecification
    class_class_curie: ClassVar[str] = "sio:DesignSpecification"
    class_name: ClassVar[str] = "DesignSpecification"
    class_model_uri: ClassVar[URIRef] = SIO.DesignSpecification


class Criterion(DesignSpecification):
    """
    A criterion is a specification to describe properties used for evaluation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Criterion
    class_class_curie: ClassVar[str] = "sio:Criterion"
    class_name: ClassVar[str] = "Criterion"
    class_model_uri: ClassVar[URIRef] = SIO.Criterion


class ExclusionCriterion(Criterion):
    """
    An exclusion criterion is a criterion that must be absent to satistify the objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ExclusionCriterion
    class_class_curie: ClassVar[str] = "sio:ExclusionCriterion"
    class_name: ClassVar[str] = "ExclusionCriterion"
    class_model_uri: ClassVar[URIRef] = SIO.ExclusionCriterion


class FormalSpecification(FunctionalSpecification):
    """
    A formal specification is a mathematical description of software or hardware that may be used to develop an
    implementation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FormalSpecification
    class_class_curie: ClassVar[str] = "sio:FormalSpecification"
    class_name: ClassVar[str] = "FormalSpecification"
    class_model_uri: ClassVar[URIRef] = SIO.FormalSpecification


class Genotype(FunctionalSpecification):
    """
    A genotype is a functional specification of a biological entity in terms of its genetic composition (or lack
    thereof).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Genotype
    class_class_curie: ClassVar[str] = "sio:Genotype"
    class_name: ClassVar[str] = "Genotype"
    class_model_uri: ClassVar[URIRef] = SIO.Genotype


class InclusionCriterion(Criterion):
    """
    An inclusion criterion is a criterion that must be present to satisfy some objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InclusionCriterion
    class_class_curie: ClassVar[str] = "sio:InclusionCriterion"
    class_name: ClassVar[str] = "InclusionCriterion"
    class_model_uri: ClassVar[URIRef] = SIO.InclusionCriterion


class MeasurementScale(FunctionalSpecification):
    """
    A measurement scale is a functional specification that specifies an allowed range of categories or values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MeasurementScale
    class_class_curie: ClassVar[str] = "sio:MeasurementScale"
    class_name: ClassVar[str] = "MeasurementScale"
    class_model_uri: ClassVar[URIRef] = SIO.MeasurementScale


class BinaryScale(MeasurementScale):
    """
    A binary scale is a measurement scale that specifies a choice between two values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BinaryScale
    class_class_curie: ClassVar[str] = "sio:BinaryScale"
    class_name: ClassVar[str] = "BinaryScale"
    class_model_uri: ClassVar[URIRef] = SIO.BinaryScale


class NomimalScale(MeasurementScale):
    """
    A nominal scale of measurement only specifies a limited set of categories.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NomimalScale
    class_class_curie: ClassVar[str] = "sio:NomimalScale"
    class_name: ClassVar[str] = "NomimalScale"
    class_model_uri: ClassVar[URIRef] = SIO.NomimalScale


class Notation(Specification):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Notation
    class_class_curie: ClassVar[str] = "sio:Notation"
    class_name: ClassVar[str] = "Notation"
    class_model_uri: ClassVar[URIRef] = SIO.Notation


class ChemicalNotation(Notation):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalNotation
    class_class_curie: ClassVar[str] = "sio:ChemicalNotation"
    class_name: ClassVar[str] = "ChemicalNotation"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalNotation


class InCHINotation(ChemicalNotation):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InCHINotation
    class_class_curie: ClassVar[str] = "sio:InCHINotation"
    class_name: ClassVar[str] = "InCHINotation"
    class_model_uri: ClassVar[URIRef] = SIO.InCHINotation


class NumericScale(MeasurementScale):
    """
    A numeric scale of measurement is one that only specifies numeric values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NumericScale
    class_class_curie: ClassVar[str] = "sio:NumericScale"
    class_name: ClassVar[str] = "NumericScale"
    class_model_uri: ClassVar[URIRef] = SIO.NumericScale


class DecimalScale(NumericScale):
    """
    A decimal scale of measurement is one that only specifies decimal values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecimalScale
    class_class_curie: ClassVar[str] = "sio:DecimalScale"
    class_name: ClassVar[str] = "DecimalScale"
    class_model_uri: ClassVar[URIRef] = SIO.DecimalScale


class IntegerScale(NumericScale):
    """
    An integer scale of measurement is one that only specifies integer values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IntegerScale
    class_class_curie: ClassVar[str] = "sio:IntegerScale"
    class_name: ClassVar[str] = "IntegerScale"
    class_model_uri: ClassVar[URIRef] = SIO.IntegerScale


class Ontology(FormalSpecification):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ontology
    class_class_curie: ClassVar[str] = "sio:Ontology"
    class_name: ClassVar[str] = "Ontology"
    class_model_uri: ClassVar[URIRef] = SIO.Ontology


class Pathway(ActionSpecification):
    """
    A pathway is an effective specification that outlines a set of actions that forms a way to achieve an objective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pathway
    class_class_curie: ClassVar[str] = "sio:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = SIO.Pathway


class ChemicalReactionPathway(Pathway):
    """
    A chemical reaction pathway specifies a series of chemical reactions towards producing some chemical product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalReactionPathway
    class_class_curie: ClassVar[str] = "sio:ChemicalReactionPathway"
    class_name: ClassVar[str] = "ChemicalReactionPathway"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalReactionPathway


class BiochemicalPathway(ChemicalReactionPathway):
    """
    A biochemical pathway specifies a series of biochemical modifications and transformations towards achieving some
    biological outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BiochemicalPathway
    class_class_curie: ClassVar[str] = "sio:BiochemicalPathway"
    class_name: ClassVar[str] = "BiochemicalPathway"
    class_model_uri: ClassVar[URIRef] = SIO.BiochemicalPathway


class ChemicalDegradationPathway(ChemicalReactionPathway):
    """
    A chemical degradation pathway is a pathway involved in the disassembly of a chemical.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalDegradationPathway
    class_class_curie: ClassVar[str] = "sio:ChemicalDegradationPathway"
    class_name: ClassVar[str] = "ChemicalDegradationPathway"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalDegradationPathway


class ChemicalSynthesisPathway(ChemicalReactionPathway):
    """
    A chemical synthesis pathway is a pathway involved in the assembly of a chemical.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalSynthesisPathway
    class_class_curie: ClassVar[str] = "sio:ChemicalSynthesisPathway"
    class_name: ClassVar[str] = "ChemicalSynthesisPathway"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalSynthesisPathway


class MetabolicPathway(BiochemicalPathway):
    """
    A metabolic pathway is a series of biochemical reactions that begins with one or more substrates and ends with one
    or more products.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MetabolicPathway
    class_class_curie: ClassVar[str] = "sio:MetabolicPathway"
    class_name: ClassVar[str] = "MetabolicPathway"
    class_model_uri: ClassVar[URIRef] = SIO.MetabolicPathway


class PharmacokineticPathway(MetabolicPathway):
    """
    a pharmacokinetic pathway is a metabolic pathway which describes the metabolism of a drug molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PharmacokineticPathway
    class_class_curie: ClassVar[str] = "sio:PharmacokineticPathway"
    class_name: ClassVar[str] = "PharmacokineticPathway"
    class_model_uri: ClassVar[URIRef] = SIO.PharmacokineticPathway


class Plan(ActionSpecification):
    """
    A plan is a set of intended actions, through which one expects to achieve a goal.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Plan
    class_class_curie: ClassVar[str] = "sio:Plan"
    class_name: ClassVar[str] = "Plan"
    class_model_uri: ClassVar[URIRef] = SIO.Plan


class Recipe(ActionSpecification):
    """
    A recipe is a set of instructions that describe how to prepare or make something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Recipe
    class_class_curie: ClassVar[str] = "sio:Recipe"
    class_name: ClassVar[str] = "Recipe"
    class_model_uri: ClassVar[URIRef] = SIO.Recipe


class RegulatoryPathway(BiochemicalPathway):
    """
    A regulatory pathway is a series of biochemical reactions that lead to the increase or decrease of activity of
    participating molecular components.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RegulatoryPathway
    class_class_curie: ClassVar[str] = "sio:RegulatoryPathway"
    class_name: ClassVar[str] = "RegulatoryPathway"
    class_model_uri: ClassVar[URIRef] = SIO.RegulatoryPathway


class PharmacodynamicPathway(RegulatoryPathway):
    """
    a pharmacodynamic pathay is a regulatory pathway in which a drug molecule regulates the activity of one or more
    components organized in a pathway.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PharmacodynamicPathway
    class_class_curie: ClassVar[str] = "sio:PharmacodynamicPathway"
    class_name: ClassVar[str] = "PharmacodynamicPathway"
    class_model_uri: ClassVar[URIRef] = SIO.PharmacodynamicPathway


class SequenceVariationNotation(Notation):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceVariationNotation
    class_class_curie: ClassVar[str] = "sio:SequenceVariationNotation"
    class_name: ClassVar[str] = "SequenceVariationNotation"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceVariationNotation


class HgvsNotation(SequenceVariationNotation):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HgvsNotation
    class_class_curie: ClassVar[str] = "sio:HgvsNotation"
    class_name: ClassVar[str] = "HgvsNotation"
    class_model_uri: ClassVar[URIRef] = SIO.HgvsNotation


class SpatialSpecification(FunctionalSpecification):
    """
    A specification for spatial location is an effective specification towards representation spatial position or
    spatial data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpatialSpecification
    class_class_curie: ClassVar[str] = "sio:SpatialSpecification"
    class_name: ClassVar[str] = "SpatialSpecification"
    class_model_uri: ClassVar[URIRef] = SIO.SpatialSpecification


class CoordinateSystem(SpatialSpecification):
    """
    A coordinate system is a specification for spatial location that uses a set of numbers, or coordinates, to
    uniquely determine the position of a point or other geometric element.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CoordinateSystem
    class_class_curie: ClassVar[str] = "sio:CoordinateSystem"
    class_name: ClassVar[str] = "CoordinateSystem"
    class_model_uri: ClassVar[URIRef] = SIO.CoordinateSystem


class CartesianCoordinateSystem(CoordinateSystem):
    """
    A Cartesian coordinate system specifies each point uniquely in a plane by a pair of numerical coordinates, which
    are the signed distances from the point to two fixed perpendicular directed lines, measured in the same unit of
    length.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CartesianCoordinateSystem
    class_class_curie: ClassVar[str] = "sio:CartesianCoordinateSystem"
    class_name: ClassVar[str] = "CartesianCoordinateSystem"
    class_model_uri: ClassVar[URIRef] = SIO.CartesianCoordinateSystem


class CylindricalCoordinateSystem(CoordinateSystem):
    """
    A cylindrical coordinate system is a three-dimensional coordinate system that specifies point positions by the
    distance from a chosen reference axis, the direction from the axis relative to a chosen reference direction, and
    the distance from a chosen reference plane perpendicular to the axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CylindricalCoordinateSystem
    class_class_curie: ClassVar[str] = "sio:CylindricalCoordinateSystem"
    class_name: ClassVar[str] = "CylindricalCoordinateSystem"
    class_model_uri: ClassVar[URIRef] = SIO.CylindricalCoordinateSystem


class PolarCoordinateSystem(CoordinateSystem):
    """
    A polar coordinate system is a two-dimensional coordinate system in which each point on a plane is determined by a
    distance from a fixed point and an angle from a fixed direction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolarCoordinateSystem
    class_class_curie: ClassVar[str] = "sio:PolarCoordinateSystem"
    class_name: ClassVar[str] = "PolarCoordinateSystem"
    class_model_uri: ClassVar[URIRef] = SIO.PolarCoordinateSystem


class Specimen(Sample):
    """
    A specimen is a portion of material for use in testing, examination, or study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Specimen
    class_class_curie: ClassVar[str] = "sio:Specimen"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = SIO.Specimen


class Speculation(Opinion):
    """
    speculation is an opinion based on incomplete evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Speculation
    class_class_curie: ClassVar[str] = "sio:Speculation"
    class_name: ClassVar[str] = "Speculation"
    class_model_uri: ClassVar[URIRef] = SIO.Speculation


class Speech(Communicating):
    """
    speech is the expression of thoughts and feelings by sound.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Speech
    class_class_curie: ClassVar[str] = "sio:Speech"
    class_name: ClassVar[str] = "Speech"
    class_model_uri: ClassVar[URIRef] = SIO.Speech


class SphericalCoordinateSystem(CoordinateSystem):
    """
    A spherical coordinate system is a coordinate system for three-dimensional space where the position of a point is
    specified by three numbers: the radial distance of that point from a fixed origin, its polar angle measured from a
    fixed zenith direction, and the azimuth angle of its orthogonal projection on a reference plane that passes
    through the origin and is orthogonal to the zenith, measured from a fixed reference direction on that plane.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SphericalCoordinateSystem
    class_class_curie: ClassVar[str] = "sio:SphericalCoordinateSystem"
    class_name: ClassVar[str] = "SphericalCoordinateSystem"
    class_model_uri: ClassVar[URIRef] = SIO.SphericalCoordinateSystem


class Standard(Specification):
    """
    A standard is a socially-agreed upon specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Standard
    class_class_curie: ClassVar[str] = "sio:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = SIO.Standard


class StandardOperatingProcedure(ExperimentalProtocol):
    """
    A standard operating procedure is a specification approved for use in specific environments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StandardOperatingProcedure
    class_class_curie: ClassVar[str] = "sio:StandardOperatingProcedure"
    class_name: ClassVar[str] = "StandardOperatingProcedure"
    class_model_uri: ClassVar[URIRef] = SIO.StandardOperatingProcedure


class State(GeopoliticalRegion):
    """
    A state is a set of governing and supportive institutions that have sovereignty over a definite territory and
    population.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.State
    class_class_curie: ClassVar[str] = "sio:State"
    class_name: ClassVar[str] = "State"
    class_model_uri: ClassVar[URIRef] = SIO.State


class Statement(Proposition):
    """
    A statement is a proposition that is either (a) a meaningful declarative sentence that is either true or false, or
    (b) that which a true or false declarative sentence asserts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Statement
    class_class_curie: ClassVar[str] = "sio:Statement"
    class_name: ClassVar[str] = "Statement"
    class_model_uri: ClassVar[URIRef] = SIO.Statement


class StatementOfConsequence(Statement):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StatementOfConsequence
    class_class_curie: ClassVar[str] = "sio:StatementOfConsequence"
    class_name: ClassVar[str] = "StatementOfConsequence"
    class_model_uri: ClassVar[URIRef] = SIO.StatementOfConsequence


class StationaryPoint(DataPoint):
    """
    A stationary point is a point that is part of a curve in which the derivative at that point is zero, and hence its
    value is at least a local maximum or minimum.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StationaryPoint
    class_class_curie: ClassVar[str] = "sio:StationaryPoint"
    class_name: ClassVar[str] = "StationaryPoint"
    class_model_uri: ClassVar[URIRef] = SIO.StationaryPoint


class LocalMaximumStationaryPoint(StationaryPoint):
    """
    A local maximum stationary point is a point that has a higher value in  some axis than adjacent points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LocalMaximumStationaryPoint
    class_class_curie: ClassVar[str] = "sio:LocalMaximumStationaryPoint"
    class_name: ClassVar[str] = "LocalMaximumStationaryPoint"
    class_model_uri: ClassVar[URIRef] = SIO.LocalMaximumStationaryPoint


class GlobalMaximalStationaryPoint(LocalMaximumStationaryPoint):
    """
    A global maximum stationary point is a data point that corresponds to a measurement value is larger than that of
    all other plotted datapoints.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GlobalMaximalStationaryPoint
    class_class_curie: ClassVar[str] = "sio:GlobalMaximalStationaryPoint"
    class_name: ClassVar[str] = "GlobalMaximalStationaryPoint"
    class_model_uri: ClassVar[URIRef] = SIO.GlobalMaximalStationaryPoint


class LocalMinimumStationaryPoint(StationaryPoint):
    """
    A local minimum stationary point is a point that has a lower value in  some axis than adjacent points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LocalMinimumStationaryPoint
    class_class_curie: ClassVar[str] = "sio:LocalMinimumStationaryPoint"
    class_name: ClassVar[str] = "LocalMinimumStationaryPoint"
    class_model_uri: ClassVar[URIRef] = SIO.LocalMinimumStationaryPoint


class GlobalMinimalStationaryPoint(LocalMinimumStationaryPoint):
    """
    A global minimum data point is a data point that corresponds to a measurement value is smaller than that of all
    other plotted datapoints.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GlobalMinimalStationaryPoint
    class_class_curie: ClassVar[str] = "sio:GlobalMinimalStationaryPoint"
    class_name: ClassVar[str] = "GlobalMinimalStationaryPoint"
    class_model_uri: ClassVar[URIRef] = SIO.GlobalMinimalStationaryPoint


class StatisticalAssociation(Association):
    """
    A statistical association is any relationship between two measured quantities that renders them statistically
    dependent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StatisticalAssociation
    class_class_curie: ClassVar[str] = "sio:StatisticalAssociation"
    class_name: ClassVar[str] = "StatisticalAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.StatisticalAssociation


class Correlation(StatisticalAssociation):
    """
    A correlation is a statistical relationship involving dependence between two random variables or datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Correlation
    class_class_curie: ClassVar[str] = "sio:Correlation"
    class_name: ClassVar[str] = "Correlation"
    class_model_uri: ClassVar[URIRef] = SIO.Correlation


class StatisticalGraph(Chart):
    """
    A statistical graph is a figure that displays the relationship among numeric data and/or mathematical functions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StatisticalGraph
    class_class_curie: ClassVar[str] = "sio:StatisticalGraph"
    class_name: ClassVar[str] = "StatisticalGraph"
    class_model_uri: ClassVar[URIRef] = SIO.StatisticalGraph


class BarGraph(StatisticalGraph):
    """
    A bar graph is a statistical graph with rectangular bars of lengths proportional to that value that they represent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BarGraph
    class_class_curie: ClassVar[str] = "sio:BarGraph"
    class_name: ClassVar[str] = "BarGraph"
    class_model_uri: ClassVar[URIRef] = SIO.BarGraph


class HorizontalBarGraph(BarGraph):
    """
    A horizontal bar graph is a bar graph in which the rectangular bars are horizontally oriented in space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HorizontalBarGraph
    class_class_curie: ClassVar[str] = "sio:HorizontalBarGraph"
    class_name: ClassVar[str] = "HorizontalBarGraph"
    class_model_uri: ClassVar[URIRef] = SIO.HorizontalBarGraph


class Line-barGraph(StatisticalGraph):
    """
    A line-bar graph statistical graph that contains both lines and bars.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Line-barGraph"]
    class_class_curie: ClassVar[str] = "sio:Line-barGraph"
    class_name: ClassVar[str] = "Line-barGraph"
    class_model_uri: ClassVar[URIRef] = SIO.Line-barGraph


class Boxplot(Line-barGraph):
    """
    A boxplot (box-and-whisker diagram) is a convenient way of graphically depicting groups of numerical data through
    their five-number summaries: the smallest observation (sample minimum), lower quartile (Q1), median (Q2), upper
    quartile (Q3), and largest observation (sample maximum).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Boxplot
    class_class_curie: ClassVar[str] = "sio:Boxplot"
    class_name: ClassVar[str] = "Boxplot"
    class_model_uri: ClassVar[URIRef] = SIO.Boxplot


class LineGraph(StatisticalGraph):
    """
    A line graph is a statistical graph in which lines contains the evaluation of functions or individual points
    connected by line segments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LineGraph
    class_class_curie: ClassVar[str] = "sio:LineGraph"
    class_name: ClassVar[str] = "LineGraph"
    class_model_uri: ClassVar[URIRef] = SIO.LineGraph


class Scatterplot(StatisticalGraph):
    """
    A scatterplot is a statistical graph which uses Cartesian coordinates to display values for two variables for a
    set of data. The data is displayed as a collection of points, each having the value of one variable determining
    the position on the horizontal axis and the value of the other variable determining the position on the vertical
    axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Scatterplot
    class_class_curie: ClassVar[str] = "sio:Scatterplot"
    class_name: ClassVar[str] = "Scatterplot"
    class_model_uri: ClassVar[URIRef] = SIO.Scatterplot


class StackGraph(StatisticalGraph):
    """
    A stack graph is a statistical graph which presents multiple series in which the distance between one series and
    another indicates the relative contribution to the total for any x-value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StackGraph
    class_class_curie: ClassVar[str] = "sio:StackGraph"
    class_name: ClassVar[str] = "StackGraph"
    class_model_uri: ClassVar[URIRef] = SIO.StackGraph


class StackedBarGraph(BarGraph):
    """
    A stacked bar graph is a bar graph in which each rectangular bar is partioned by the categorical value of each
    series of data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StackedBarGraph
    class_class_curie: ClassVar[str] = "sio:StackedBarGraph"
    class_name: ClassVar[str] = "StackedBarGraph"
    class_model_uri: ClassVar[URIRef] = SIO.StackedBarGraph


class StatisticalGraphLine(Line):
    """
    A statistical graph line is a line used in a statistical graph to communicate some trend or feature of the
    embedded data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StatisticalGraphLine
    class_class_curie: ClassVar[str] = "sio:StatisticalGraphLine"
    class_name: ClassVar[str] = "StatisticalGraphLine"
    class_model_uri: ClassVar[URIRef] = SIO.StatisticalGraphLine


class DropLine(StatisticalGraphLine):
    """
    A drop line is a statistical graph line that vertically or horizontally connects a data series line with a value
    axis in a statistical graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DropLine
    class_class_curie: ClassVar[str] = "sio:DropLine"
    class_name: ClassVar[str] = "DropLine"
    class_model_uri: ClassVar[URIRef] = SIO.DropLine


class StatusDescriptor(InformationalQuality):
    """
    status descriptor is a descriptor for the state of a process or object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StatusDescriptor
    class_class_curie: ClassVar[str] = "sio:StatusDescriptor"
    class_name: ClassVar[str] = "StatusDescriptor"
    class_model_uri: ClassVar[URIRef] = SIO.StatusDescriptor


class Stereoisomer(Isomer):
    """
    A stereoisomer is an isomer in which the atomic connectivity is the same, but differs in its spatial arrangement
    of atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Stereoisomer
    class_class_curie: ClassVar[str] = "sio:Stereoisomer"
    class_name: ClassVar[str] = "Stereoisomer"
    class_model_uri: ClassVar[URIRef] = SIO.Stereoisomer


class Diastereomer(Stereoisomer):
    """
    A diastereomer is a stereoisomer that is not a mirror image of its isomer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Diastereomer
    class_class_curie: ClassVar[str] = "sio:Diastereomer"
    class_name: ClassVar[str] = "Diastereomer"
    class_model_uri: ClassVar[URIRef] = SIO.Diastereomer


class Enantiomer(Stereoisomer):
    """
    An enantiomer is a stereoisomer that is a mirror image of its isomer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Enantiomer
    class_class_curie: ClassVar[str] = "sio:Enantiomer"
    class_name: ClassVar[str] = "Enantiomer"
    class_model_uri: ClassVar[URIRef] = SIO.Enantiomer


class Epimer(Stereoisomer):
    """
    An epimer is a stereoisomer that differs in configuration at only one stereogenic center.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Epimer
    class_class_curie: ClassVar[str] = "sio:Epimer"
    class_name: ClassVar[str] = "Epimer"
    class_model_uri: ClassVar[URIRef] = SIO.Epimer


class OpticalIsomer(Stereoisomer):
    """
    An optical isomer is a stereoisomer that rotates the plane of polarization of a beam of plane polarized light.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OpticalIsomer
    class_class_curie: ClassVar[str] = "sio:OpticalIsomer"
    class_name: ClassVar[str] = "OpticalIsomer"
    class_model_uri: ClassVar[URIRef] = SIO.OpticalIsomer


class Straight(Curvature):
    """
    straight is a quality of a bearer that is free of curves, bends, or angles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Straight
    class_class_curie: ClassVar[str] = "sio:Straight"
    class_name: ClassVar[str] = "Straight"
    class_model_uri: ClassVar[URIRef] = SIO.Straight


class Strain(Organism):
    """
    A strain is a genetic variant or kind of microorganism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Strain
    class_class_curie: ClassVar[str] = "sio:Strain"
    class_name: ClassVar[str] = "Strain"
    class_model_uri: ClassVar[URIRef] = SIO.Strain


class Streamgraph(StackGraph):
    """
    A streamgraph is a multi-line stacked graph that yields the appearance of continuous y-values across the x-axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Streamgraph
    class_class_curie: ClassVar[str] = "sio:Streamgraph"
    class_name: ClassVar[str] = "Streamgraph"
    class_model_uri: ClassVar[URIRef] = SIO.Streamgraph


class Strong(Intensity):
    """
    strong is a qualitative intensity value that is more intense than moderate, but less intense than severe.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Strong
    class_class_curie: ClassVar[str] = "sio:Strong"
    class_name: ClassVar[str] = "Strong"
    class_model_uri: ClassVar[URIRef] = SIO.Strong


class StrongChemicalSalt(ChemicalSalt):
    """
    a strong chemical salt is a chemical salt that is composed of strong electrolytes. Strong chemical salts contain
    Na,K,NH4 or NO3, CIO4, CH3COO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StrongChemicalSalt
    class_class_curie: ClassVar[str] = "sio:StrongChemicalSalt"
    class_name: ClassVar[str] = "StrongChemicalSalt"
    class_model_uri: ClassVar[URIRef] = SIO.StrongChemicalSalt


class StrontiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StrontiumAtom
    class_class_curie: ClassVar[str] = "sio:StrontiumAtom"
    class_name: ClassVar[str] = "StrontiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.StrontiumAtom


class StructuralIsomer(Isomer):
    """
    A structural isomer is an isomer in which the atoms are joined together in different ways.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StructuralIsomer
    class_class_curie: ClassVar[str] = "sio:StructuralIsomer"
    class_name: ClassVar[str] = "StructuralIsomer"
    class_model_uri: ClassVar[URIRef] = SIO.StructuralIsomer


class StructuralMotif(Pattern):
    """
    A structural motif is a pattern in a structure formed by a spatial arrangement of objects (e.g. atoms).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StructuralMotif
    class_class_curie: ClassVar[str] = "sio:StructuralMotif"
    class_name: ClassVar[str] = "StructuralMotif"
    class_model_uri: ClassVar[URIRef] = SIO.StructuralMotif


class StructuralQuality(ObjectQuality):
    """
    A structural quality is a quality of an object that describes its structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StructuralQuality
    class_class_curie: ClassVar[str] = "sio:StructuralQuality"
    class_name: ClassVar[str] = "StructuralQuality"
    class_model_uri: ClassVar[URIRef] = SIO.StructuralQuality


class Disordered(StructuralQuality):
    """
    disordered is a structural quality in which the parts of an object are non-rigid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Disordered
    class_class_curie: ClassVar[str] = "sio:Disordered"
    class_name: ClassVar[str] = "Disordered"
    class_model_uri: ClassVar[URIRef] = SIO.Disordered


class Helicity(StructuralQuality):
    """
    helicity is the quality of being helical
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Helicity
    class_class_curie: ClassVar[str] = "sio:Helicity"
    class_name: ClassVar[str] = "Helicity"
    class_model_uri: ClassVar[URIRef] = SIO.Helicity


class CircularlyHelical(Helicity):
    """
    a circularly helical quality is the quality of a helix that is connected in a circle or loop.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CircularlyHelical
    class_class_curie: ClassVar[str] = "sio:CircularlyHelical"
    class_name: ClassVar[str] = "CircularlyHelical"
    class_model_uri: ClassVar[URIRef] = SIO.CircularlyHelical


class Left-handedHelical(Helicity):
    """
    left-handed helical quality is the quality in which a clockwise screwing motion moves the helix towards the
    observed along the line of sight along the helix's axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Left-handedHelical"]
    class_class_curie: ClassVar[str] = "sio:Left-handedHelical"
    class_name: ClassVar[str] = "Left-handedHelical"
    class_model_uri: ClassVar[URIRef] = SIO.Left-handedHelical


class Right-handedHelical(Helicity):
    """
    right-handed helical quality is the quality in which a clockwise screwing motion moves the helix away from the
    observed along the line of sight along the helix's axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Right-handedHelical"]
    class_class_curie: ClassVar[str] = "sio:Right-handedHelical"
    class_name: ClassVar[str] = "Right-handedHelical"
    class_model_uri: ClassVar[URIRef] = SIO.Right-handedHelical


class Rigid(StructuralQuality):
    """
    rigid is the quality of maintaining structural integrity (and not bending) under pressure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Rigid
    class_class_curie: ClassVar[str] = "sio:Rigid"
    class_name: ClassVar[str] = "Rigid"
    class_model_uri: ClassVar[URIRef] = SIO.Rigid


class Structure(FunctionalSpecification):
    """
    structure is the specification that refers to the composition and arrangement of parts of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Structure
    class_class_curie: ClassVar[str] = "sio:Structure"
    class_name: ClassVar[str] = "Structure"
    class_model_uri: ClassVar[URIRef] = SIO.Structure


class ChemicalStructure(Structure):
    """
    chemical structure is the structure of a chemical entity in terms of its molecular geometry and electronic
    structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalStructure
    class_class_curie: ClassVar[str] = "sio:ChemicalStructure"
    class_name: ClassVar[str] = "ChemicalStructure"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalStructure


class ElectronicStructure(ChemicalStructure):
    """
    electronic structure is the electron configuration is the distribution of electrons of an atom or molecule (or
    other physical structure) in atomic or molecular orbitals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ElectronicStructure
    class_class_curie: ClassVar[str] = "sio:ElectronicStructure"
    class_name: ClassVar[str] = "ElectronicStructure"
    class_model_uri: ClassVar[URIRef] = SIO.ElectronicStructure


class MolecularStructure(ChemicalStructure):
    """
    molecular structure is the spatial arrangement of atoms in a molecule and the chemical bonds that hold the atoms
    together.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularStructure
    class_class_curie: ClassVar[str] = "sio:MolecularStructure"
    class_name: ClassVar[str] = "MolecularStructure"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularStructure


class CrystalStructure(MolecularStructure):
    """
    A crystal structure is the arrangement of atoms or molecules in a crystalline liquid or solid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CrystalStructure
    class_class_curie: ClassVar[str] = "sio:CrystalStructure"
    class_name: ClassVar[str] = "CrystalStructure"
    class_model_uri: ClassVar[URIRef] = SIO.CrystalStructure


class Student(Academic):
    """
    A student is an individual who is attends an educational institution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Student
    class_class_curie: ClassVar[str] = "sio:Student"
    class_name: ClassVar[str] = "Student"
    class_model_uri: ClassVar[URIRef] = SIO.Student


class StudentAdvisorRole(AcademicRole):
    """
    A student advisor role is the role of an individual employed at an academic organization that is involved in
    advising students.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StudentAdvisorRole
    class_class_curie: ClassVar[str] = "sio:StudentAdvisorRole"
    class_name: ClassVar[str] = "StudentAdvisorRole"
    class_model_uri: ClassVar[URIRef] = SIO.StudentAdvisorRole


class GraduateStudentAdvisorRole(StudentAdvisorRole):
    """
    A graduate student advisor role is the role of an individual employed at an academic organization that is involved
    in advising graduate students.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GraduateStudentAdvisorRole
    class_class_curie: ClassVar[str] = "sio:GraduateStudentAdvisorRole"
    class_name: ClassVar[str] = "GraduateStudentAdvisorRole"
    class_model_uri: ClassVar[URIRef] = SIO.GraduateStudentAdvisorRole


class StudentRole(AcademicRole):
    """
    A student role is the role of an individual that is enrolled in courses at an academic institution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StudentRole
    class_class_curie: ClassVar[str] = "sio:StudentRole"
    class_name: ClassVar[str] = "StudentRole"
    class_model_uri: ClassVar[URIRef] = SIO.StudentRole


class Study(Investigation):
    """
    A study is a process that realizes the steps of a study design.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Study
    class_class_curie: ClassVar[str] = "sio:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = SIO.Study


class StudyDesign(ExperimentalProtocol):
    """
    A study design is a protocol for the proper execution of a study which normally requires a carefullly crafted
    research question or hypothesis and at least one variable under observation and observed values for that variable.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StudyDesign
    class_class_curie: ClassVar[str] = "sio:StudyDesign"
    class_name: ClassVar[str] = "StudyDesign"
    class_model_uri: ClassVar[URIRef] = SIO.StudyDesign


class StudyGroup(Collective):
    """
    A study group is a group of individuals that are subjects in an observational or intervention study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StudyGroup
    class_class_curie: ClassVar[str] = "sio:StudyGroup"
    class_name: ClassVar[str] = "StudyGroup"
    class_model_uri: ClassVar[URIRef] = SIO.StudyGroup


class ControlGroup(StudyGroup):
    """
    A control group is a group of individuals that are not subject to an intervention of interest, but rather serve as
    a baseline to compare the outcomes in the intervention group.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ControlGroup
    class_class_curie: ClassVar[str] = "sio:ControlGroup"
    class_name: ClassVar[str] = "ControlGroup"
    class_model_uri: ClassVar[URIRef] = SIO.ControlGroup


class InterventionGroup(StudyGroup):
    """
    An intervention group is a group of individuals that are subject to an intervention.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InterventionGroup
    class_class_curie: ClassVar[str] = "sio:InterventionGroup"
    class_name: ClassVar[str] = "InterventionGroup"
    class_model_uri: ClassVar[URIRef] = SIO.InterventionGroup


class StudySubject(Person):
    """
    A study subject is an individual that is the subject of the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StudySubject
    class_class_curie: ClassVar[str] = "sio:StudySubject"
    class_name: ClassVar[str] = "StudySubject"
    class_model_uri: ClassVar[URIRef] = SIO.StudySubject


class SubcellularEntity(BiologicalEntity):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SubcellularEntity
    class_class_curie: ClassVar[str] = "sio:SubcellularEntity"
    class_name: ClassVar[str] = "SubcellularEntity"
    class_model_uri: ClassVar[URIRef] = SIO.SubcellularEntity


class SubjectRole(InvestigationalRole):
    """
    A subject role is the role of an individual that is the target of the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SubjectRole
    class_class_curie: ClassVar[str] = "sio:SubjectRole"
    class_name: ClassVar[str] = "SubjectRole"
    class_model_uri: ClassVar[URIRef] = SIO.SubjectRole


class SubmolecularEntity(ChemicalEntity):
    """
    A submolecular entity is a chemical entity that is a part of a molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SubmolecularEntity
    class_class_curie: ClassVar[str] = "sio:SubmolecularEntity"
    class_name: ClassVar[str] = "SubmolecularEntity"
    class_model_uri: ClassVar[URIRef] = SIO.SubmolecularEntity


class StrongSubmolecularComponent(SubmolecularEntity):
    """
    A strong submolecular component is a submolecular component that strongly connects submolecular components.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StrongSubmolecularComponent
    class_class_curie: ClassVar[str] = "sio:StrongSubmolecularComponent"
    class_name: ClassVar[str] = "StrongSubmolecularComponent"
    class_model_uri: ClassVar[URIRef] = SIO.StrongSubmolecularComponent


class CovalentBond(StrongSubmolecularComponent):
    """
    A covalent bond is a strong submolecular interaction between atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CovalentBond
    class_class_curie: ClassVar[str] = "sio:CovalentBond"
    class_name: ClassVar[str] = "CovalentBond"
    class_model_uri: ClassVar[URIRef] = SIO.CovalentBond


class AromaticBond(CovalentBond):
    """
    An aromatic bond is an interaction between a set of atoms across which pairs of electrons are shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AromaticBond
    class_class_curie: ClassVar[str] = "sio:AromaticBond"
    class_name: ClassVar[str] = "AromaticBond"
    class_model_uri: ClassVar[URIRef] = SIO.AromaticBond


class DoubleBond(CovalentBond):
    """
    A double bond is a covalent bond between a pair of atoms in which two pairs of electrons are shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DoubleBond
    class_class_curie: ClassVar[str] = "sio:DoubleBond"
    class_name: ClassVar[str] = "DoubleBond"
    class_model_uri: ClassVar[URIRef] = SIO.DoubleBond


class SingleBond(CovalentBond):
    """
    A single bond is a covalent bond between a pair of atoms in which one pair of electrons are shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SingleBond
    class_class_curie: ClassVar[str] = "sio:SingleBond"
    class_name: ClassVar[str] = "SingleBond"
    class_model_uri: ClassVar[URIRef] = SIO.SingleBond


class DisulfideBond(SingleBond):
    """
    A disulfide bond is a bond between two sulfur atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DisulfideBond
    class_class_curie: ClassVar[str] = "sio:DisulfideBond"
    class_name: ClassVar[str] = "DisulfideBond"
    class_model_uri: ClassVar[URIRef] = SIO.DisulfideBond


class Submolecule(SubmolecularEntity):
    """
    A submolecule is any part of a molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Submolecule
    class_class_curie: ClassVar[str] = "sio:Submolecule"
    class_name: ClassVar[str] = "Submolecule"
    class_model_uri: ClassVar[URIRef] = SIO.Submolecule


class ChemicalFunctionalGroup(Submolecule):
    """
    A chemical functional group is a submolecule that confers specific chemical properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalFunctionalGroup
    class_class_curie: ClassVar[str] = "sio:ChemicalFunctionalGroup"
    class_name: ClassVar[str] = "ChemicalFunctionalGroup"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalFunctionalGroup


class Monomer(Submolecule):
    """
    A monomer is a submolecule that is proper part of some polymer, and is a building block for such polymer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Monomer
    class_class_curie: ClassVar[str] = "sio:Monomer"
    class_name: ClassVar[str] = "Monomer"
    class_model_uri: ClassVar[URIRef] = SIO.Monomer


class OrganicSubmolecule(Submolecule):
    """
    An organic submolecule is connected region of a molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrganicSubmolecule
    class_class_curie: ClassVar[str] = "sio:OrganicSubmolecule"
    class_name: ClassVar[str] = "OrganicSubmolecule"
    class_model_uri: ClassVar[URIRef] = SIO.OrganicSubmolecule


class AminoAcidPolymerSubmolecule(OrganicSubmolecule):
    """
    An amino acid polymer submolecule is a submolecule of an amino acid polymer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AminoAcidPolymerSubmolecule
    class_class_curie: ClassVar[str] = "sio:AminoAcidPolymerSubmolecule"
    class_name: ClassVar[str] = "AminoAcidPolymerSubmolecule"
    class_model_uri: ClassVar[URIRef] = SIO.AminoAcidPolymerSubmolecule


class AlphaHelix(AminoAcidPolymerSubmolecule):
    """
    An alpha helix is structural region of a protein that is characterized by 3.6 residues per turn, a translation of
    1.5 angstroms along the helical axis in which backbone N-H groups form a hydrogen bond to the backbone carboxyl
    group of the amino acid four residues prior.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AlphaHelix
    class_class_curie: ClassVar[str] = "sio:AlphaHelix"
    class_name: ClassVar[str] = "AlphaHelix"
    class_model_uri: ClassVar[URIRef] = SIO.AlphaHelix


class AminoAcidResidue(AminoAcidPolymerSubmolecule):
    """
    An amino acid residue is a submolecule of an amino acid that is part of a larger molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AminoAcidResidue
    class_class_curie: ClassVar[str] = "sio:AminoAcidResidue"
    class_name: ClassVar[str] = "AminoAcidResidue"
    class_model_uri: ClassVar[URIRef] = SIO.AminoAcidResidue


class BetaStrand(AminoAcidPolymerSubmolecule):
    """
    A beta strand is structural region of a protein that is characterized by a roughly planar sequence of amino acid
    residues forming hydrogen bonds between the N-O and the C=O of another part of the peptide
    and having their side chains perpendicular to the planar axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BetaStrand
    class_class_curie: ClassVar[str] = "sio:BetaStrand"
    class_name: ClassVar[str] = "BetaStrand"
    class_model_uri: ClassVar[URIRef] = SIO.BetaStrand


class CarbohydrateResidue(OrganicSubmolecule):
    """
    A carbohydrate residue is a part of a molecule that was derived from a monosaccharide molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CarbohydrateResidue
    class_class_curie: ClassVar[str] = "sio:CarbohydrateResidue"
    class_name: ClassVar[str] = "CarbohydrateResidue"
    class_model_uri: ClassVar[URIRef] = SIO.CarbohydrateResidue


class LipidResidue(OrganicSubmolecule):
    """
    A lipid residue is a part of an organic molecule that was derived from a lipid molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LipidResidue
    class_class_curie: ClassVar[str] = "sio:LipidResidue"
    class_name: ClassVar[str] = "LipidResidue"
    class_model_uri: ClassVar[URIRef] = SIO.LipidResidue


class NucleicAcidPart(OrganicSubmolecule):
    """
    A nucleic acid part is a component of a nucleic acid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NucleicAcidPart
    class_class_curie: ClassVar[str] = "sio:NucleicAcidPart"
    class_name: ClassVar[str] = "NucleicAcidPart"
    class_model_uri: ClassVar[URIRef] = SIO.NucleicAcidPart


class CisRegulatoryElement(NucleicAcidPart):
    """
    A cisregulatory element is a DNA sequence located on the same DNA strand or chromosome as the gene whose
    expression it affects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CisRegulatoryElement
    class_class_curie: ClassVar[str] = "sio:CisRegulatoryElement"
    class_name: ClassVar[str] = "CisRegulatoryElement"
    class_model_uri: ClassVar[URIRef] = SIO.CisRegulatoryElement


class Gene(NucleicAcidPart):
    """
    A gene is part of a nucleic acid that contains all the necessary elements to encode a functional transcript.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Gene
    class_class_curie: ClassVar[str] = "sio:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = SIO.Gene


class Allele(Gene):
    """
    An allele is one of a set of sequence variants of a gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Allele
    class_class_curie: ClassVar[str] = "sio:Allele"
    class_name: ClassVar[str] = "Allele"
    class_model_uri: ClassVar[URIRef] = SIO.Allele


class DnaGene(Gene):
    """
    A gene that is located on DNA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DnaGene
    class_class_curie: ClassVar[str] = "sio:DnaGene"
    class_name: ClassVar[str] = "DnaGene"
    class_model_uri: ClassVar[URIRef] = SIO.DnaGene


class GeneComponent(NucleicAcidPart):
    """
    A gene component is a component of a gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeneComponent
    class_class_curie: ClassVar[str] = "sio:GeneComponent"
    class_name: ClassVar[str] = "GeneComponent"
    class_model_uri: ClassVar[URIRef] = SIO.GeneComponent


class 3%27UntranslatedRegion(GeneComponent):
    """
    A three prime untranslated region (3'-UTR) is the section of messenger RNA (mRNA) that immediately follows the
    translation termination codon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["3%27UntranslatedRegion"]
    class_class_curie: ClassVar[str] = "sio:3%27UntranslatedRegion"
    class_name: ClassVar[str] = "3%27UntranslatedRegion"
    class_model_uri: ClassVar[URIRef] = SIO.3%27UntranslatedRegion


class 5%27UntranslatedRegion(GeneComponent):
    """
    The five prime untranslated region (5' UTR) is a section of messenger RNA (mRNA) and the DNA that codes for it
    that starts at the +1 position (where transcription begins) and ends one nucleotide before the start codon
    (usually AUG) of the coding region.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["5%27UntranslatedRegion"]
    class_class_curie: ClassVar[str] = "sio:5%27UntranslatedRegion"
    class_name: ClassVar[str] = "5%27UntranslatedRegion"
    class_model_uri: ClassVar[URIRef] = SIO.5%27UntranslatedRegion


class Exon(GeneComponent):
    """
    An exon is a nucleotide sequence encoded by a gene that remains present within the final mature RNA product of
    that gene after introns have been removed by RNA splicing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Exon
    class_class_curie: ClassVar[str] = "sio:Exon"
    class_name: ClassVar[str] = "Exon"
    class_model_uri: ClassVar[URIRef] = SIO.Exon


class GeneRegulatoryComponent(GeneComponent):
    """
    A gene regulatory component is a gene component that exerts a regulatory function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeneRegulatoryComponent
    class_class_curie: ClassVar[str] = "sio:GeneRegulatoryComponent"
    class_name: ClassVar[str] = "GeneRegulatoryComponent"
    class_model_uri: ClassVar[URIRef] = SIO.GeneRegulatoryComponent


class GeneEnhancer(GeneRegulatoryComponent):
    """
    A gene enhancer is a short region of DNA that can be bound with proteins to enhance transcription levels of genes
    in a gene cluster.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeneEnhancer
    class_class_curie: ClassVar[str] = "sio:GeneEnhancer"
    class_name: ClassVar[str] = "GeneEnhancer"
    class_model_uri: ClassVar[URIRef] = SIO.GeneEnhancer


class GenePromoter(GeneRegulatoryComponent):
    """
    A gene promoter is a region of DNA that initiates transcription of a particular gene.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GenePromoter
    class_class_curie: ClassVar[str] = "sio:GenePromoter"
    class_name: ClassVar[str] = "GenePromoter"
    class_model_uri: ClassVar[URIRef] = SIO.GenePromoter


class GeneticPolymorphism(NucleicAcidPart):
    """
    genetic polymorphism is the description of a difference in genetic composition at some location.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeneticPolymorphism
    class_class_curie: ClassVar[str] = "sio:GeneticPolymorphism"
    class_name: ClassVar[str] = "GeneticPolymorphism"
    class_model_uri: ClassVar[URIRef] = SIO.GeneticPolymorphism


class GenomicSequenceVariant(NucleicAcidPart):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GenomicSequenceVariant
    class_class_curie: ClassVar[str] = "sio:GenomicSequenceVariant"
    class_name: ClassVar[str] = "GenomicSequenceVariant"
    class_model_uri: ClassVar[URIRef] = SIO.GenomicSequenceVariant


class Haplotype(GenomicSequenceVariant):
    """
    A haplotype is one of a set of genomic sequence variants.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Haplotype
    class_class_curie: ClassVar[str] = "sio:Haplotype"
    class_name: ClassVar[str] = "Haplotype"
    class_model_uri: ClassVar[URIRef] = SIO.Haplotype


class Intron(GeneComponent):
    """
    An intron is a region of a gene that is removed from the final protein open reading frame.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Intron
    class_class_curie: ClassVar[str] = "sio:Intron"
    class_name: ClassVar[str] = "Intron"
    class_model_uri: ClassVar[URIRef] = SIO.Intron


class Non-proteinCodingRNAncRNAGene(Gene):
    """
    A non-protein coding RNA (ncRNA) gene is a gene that encodes for a RNA transcript that is not further translated
    into a protein product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Non-proteinCodingRNAncRNAGene"]
    class_class_curie: ClassVar[str] = "sio:Non-proteinCodingRNAncRNAGene"
    class_name: ClassVar[str] = "Non-proteinCodingRNAncRNAGene"
    class_model_uri: ClassVar[URIRef] = SIO.Non-proteinCodingRNAncRNAGene


class NucleotideResidue(NucleicAcidPart):
    """
    A nucleotide residue is a part of a molecule that derives from a nucleotide.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NucleotideResidue
    class_class_curie: ClassVar[str] = "sio:NucleotideResidue"
    class_name: ClassVar[str] = "NucleotideResidue"
    class_model_uri: ClassVar[URIRef] = SIO.NucleotideResidue


class DeoxyribonucleotideResidue(NucleotideResidue):
    """
    A deoxyribonucleotide residue is a part of a molecule that derives from a deoxyribonucleotide.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DeoxyribonucleotideResidue
    class_class_curie: ClassVar[str] = "sio:DeoxyribonucleotideResidue"
    class_name: ClassVar[str] = "DeoxyribonucleotideResidue"
    class_model_uri: ClassVar[URIRef] = SIO.DeoxyribonucleotideResidue


class OpenReadingFrame(GeneComponent):
    """
    An open reading frame (ORF) is a part of a gene that encodes a protein but does not contain a stop codon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OpenReadingFrame
    class_class_curie: ClassVar[str] = "sio:OpenReadingFrame"
    class_name: ClassVar[str] = "OpenReadingFrame"
    class_model_uri: ClassVar[URIRef] = SIO.OpenReadingFrame


class Operon(NucleicAcidPart):
    """
    An operon is a collection of contiguous genes transcribed as a single (polycistronic) mRNA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Operon
    class_class_curie: ClassVar[str] = "sio:Operon"
    class_name: ClassVar[str] = "Operon"
    class_model_uri: ClassVar[URIRef] = SIO.Operon


class Post-translationalModification(AminoAcidPolymerSubmolecule):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Post-translationalModification"]
    class_class_curie: ClassVar[str] = "sio:Post-translationalModification"
    class_name: ClassVar[str] = "Post-translationalModification"
    class_model_uri: ClassVar[URIRef] = SIO.Post-translationalModification


class PredictedGene(Gene):
    """
    A predicted gene is a gene that was identified through computational method but has not been experimentally
    validated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PredictedGene
    class_class_curie: ClassVar[str] = "sio:PredictedGene"
    class_name: ClassVar[str] = "PredictedGene"
    class_model_uri: ClassVar[URIRef] = SIO.PredictedGene


class ProteinCodingGene(Gene):
    """
    A gene that contains an open reading frame which codes for a protein.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinCodingGene
    class_class_curie: ClassVar[str] = "sio:ProteinCodingGene"
    class_name: ClassVar[str] = "ProteinCodingGene"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinCodingGene


class ProteinCodingSequence(GeneComponent):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinCodingSequence
    class_class_curie: ClassVar[str] = "sio:ProteinCodingSequence"
    class_name: ClassVar[str] = "ProteinCodingSequence"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinCodingSequence


class ProteinDomain(AminoAcidPolymerSubmolecule):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinDomain
    class_class_curie: ClassVar[str] = "sio:ProteinDomain"
    class_name: ClassVar[str] = "ProteinDomain"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinDomain


class Pseudogene(NucleicAcidPart):
    """
    A pseudo gene is a region of a nucleic acid that either cannot be transcribed, or its RNA transcript cannot be
    translated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Pseudogene
    class_class_curie: ClassVar[str] = "sio:Pseudogene"
    class_name: ClassVar[str] = "Pseudogene"
    class_model_uri: ClassVar[URIRef] = SIO.Pseudogene


class RNATranscriptComponent(NucleicAcidPart):
    """
    An RNA transcript component is a region of an RNA transcript.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RNATranscriptComponent
    class_class_curie: ClassVar[str] = "sio:RNATranscriptComponent"
    class_name: ClassVar[str] = "RNATranscriptComponent"
    class_model_uri: ClassVar[URIRef] = SIO.RNATranscriptComponent


class RibonucleotideResidue(NucleotideResidue):
    """
    A ribonucleotide residue is a part of a molecule that derives from a ribonucleotide.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RibonucleotideResidue
    class_class_curie: ClassVar[str] = "sio:RibonucleotideResidue"
    class_name: ClassVar[str] = "RibonucleotideResidue"
    class_model_uri: ClassVar[URIRef] = SIO.RibonucleotideResidue


class RibosomalRNAGene(Non-proteinCodingRNAncRNAGene):
    """
    A ribosomal RNA gene is a gene that codes for a ribosomal RNA molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RibosomalRNAGene
    class_class_curie: ClassVar[str] = "sio:RibosomalRNAGene"
    class_name: ClassVar[str] = "RibosomalRNAGene"
    class_model_uri: ClassVar[URIRef] = SIO.RibosomalRNAGene


class Ring(ChemicalFunctionalGroup):
    """
    A ring is a submolecule with a circular topology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ring
    class_class_curie: ClassVar[str] = "sio:Ring"
    class_name: ClassVar[str] = "Ring"
    class_model_uri: ClassVar[URIRef] = SIO.Ring


class AromaticRing(Ring):
    """
    An aromatic ring is a ring in which the electrons are delocalized across all atoms in the ring.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AromaticRing
    class_class_curie: ClassVar[str] = "sio:AromaticRing"
    class_name: ClassVar[str] = "AromaticRing"
    class_model_uri: ClassVar[URIRef] = SIO.AromaticRing


class HeterocyclicRing(Ring):
    """
    A heterocyclic ring is a ring containing a hetero atom.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HeterocyclicRing
    class_class_curie: ClassVar[str] = "sio:HeterocyclicRing"
    class_name: ClassVar[str] = "HeterocyclicRing"
    class_model_uri: ClassVar[URIRef] = SIO.HeterocyclicRing


class HomocyclicRing(Ring):
    """
    A homocyclic ring is a ring where the atoms are of a single type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HomocyclicRing
    class_class_curie: ClassVar[str] = "sio:HomocyclicRing"
    class_name: ClassVar[str] = "HomocyclicRing"
    class_model_uri: ClassVar[URIRef] = SIO.HomocyclicRing


class RnaGene(Gene):
    """
    A gene that is located on RNA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RnaGene
    class_class_curie: ClassVar[str] = "sio:RnaGene"
    class_name: ClassVar[str] = "RnaGene"
    class_model_uri: ClassVar[URIRef] = SIO.RnaGene


class FunctionalRnaCodingGene(RnaGene):
    """
    A gene that codes for a functional RNA molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FunctionalRnaCodingGene
    class_class_curie: ClassVar[str] = "sio:FunctionalRnaCodingGene"
    class_name: ClassVar[str] = "FunctionalRnaCodingGene"
    class_model_uri: ClassVar[URIRef] = SIO.FunctionalRnaCodingGene


class SingleNucleotidePolymorphism(NucleotideResidue):
    """
    a single nucleotide variation (SNV) is a nucleotide residue that is a variant compared to some reference nucleic
    acid sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SingleNucleotidePolymorphism
    class_class_curie: ClassVar[str] = "sio:SingleNucleotidePolymorphism"
    class_name: ClassVar[str] = "SingleNucleotidePolymorphism"
    class_model_uri: ClassVar[URIRef] = SIO.SingleNucleotidePolymorphism


class SmallCytoplasmicRNAscRNAGene(Non-proteinCodingRNAncRNAGene):
    """
    A small cytoplasmic RNA (scRNA) gene is a gene that encodes a small (7S; 129 nucleotides) RNA molecule found in
    the cytosol and rough endoplasmic reticulum that are normally associated with proteins that are involved in
    specific selection and transport of other proteins.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SmallCytoplasmicRNAscRNAGene
    class_class_curie: ClassVar[str] = "sio:SmallCytoplasmicRNAscRNAGene"
    class_name: ClassVar[str] = "SmallCytoplasmicRNAscRNAGene"
    class_model_uri: ClassVar[URIRef] = SIO.SmallCytoplasmicRNAscRNAGene


class SmallNuclearRNAsnRNAGene(Non-proteinCodingRNAncRNAGene):
    """
    A small nuclear RNA (snRNA) gene is a gene that encodes a small niuclear RNA molecule.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SmallNuclearRNAsnRNAGene
    class_class_curie: ClassVar[str] = "sio:SmallNuclearRNAsnRNAGene"
    class_name: ClassVar[str] = "SmallNuclearRNAsnRNAGene"
    class_model_uri: ClassVar[URIRef] = SIO.SmallNuclearRNAsnRNAGene


class SmallNucleolarRNAsnoRNAGene(Non-proteinCodingRNAncRNAGene):
    """
    A small nucleolar RNA (snoRNA) gene is a gene that encodes a small RNA that are associated with the eukaryotic
    nucleus as components of small nucleolar ribonucleoproteins.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SmallNucleolarRNAsnoRNAGene
    class_class_curie: ClassVar[str] = "sio:SmallNucleolarRNAsnoRNAGene"
    class_name: ClassVar[str] = "SmallNucleolarRNAsnoRNAGene"
    class_model_uri: ClassVar[URIRef] = SIO.SmallNucleolarRNAsnoRNAGene


class SpliceSite(RNATranscriptComponent):
    """
    A splice site is a region required for the excision of an intron and connection to another exon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpliceSite
    class_class_curie: ClassVar[str] = "sio:SpliceSite"
    class_name: ClassVar[str] = "SpliceSite"
    class_model_uri: ClassVar[URIRef] = SIO.SpliceSite


class 3%27SpliceSite(SpliceSite):
    """
    The 3' splice site is the terminal region of an exon that is 3' to the intron that is to be excised.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["3%27SpliceSite"]
    class_class_curie: ClassVar[str] = "sio:3%27SpliceSite"
    class_name: ClassVar[str] = "3%27SpliceSite"
    class_model_uri: ClassVar[URIRef] = SIO.3%27SpliceSite


class 5%27SpliceSite(SpliceSite):
    """
    The 5' splice site is the terminal region of an exon that is 5' to the intron that is to be excised.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["5%27SpliceSite"]
    class_class_curie: ClassVar[str] = "sio:5%27SpliceSite"
    class_name: ClassVar[str] = "5%27SpliceSite"
    class_model_uri: ClassVar[URIRef] = SIO.5%27SpliceSite


class StartCodon(RNATranscriptComponent):
    """
    A start codon is the first codon of a messenger RNA (mRNA) transcript translated by a ribosome. The start codon is
    almost always preceded by an untranslated region 5' UTR.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StartCodon
    class_class_curie: ClassVar[str] = "sio:StartCodon"
    class_name: ClassVar[str] = "StartCodon"
    class_model_uri: ClassVar[URIRef] = SIO.StartCodon


class StopCodon(RNATranscriptComponent):
    """
    A stop codon (or termination codon) is a nucleotide triplet within messenger RNA that signals a termination of
    translation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StopCodon
    class_class_curie: ClassVar[str] = "sio:StopCodon"
    class_name: ClassVar[str] = "StopCodon"
    class_model_uri: ClassVar[URIRef] = SIO.StopCodon


class SubstrateRole(ReactantRole):
    """
    The role of a chemical entity that is modified in a chemical reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SubstrateRole
    class_class_curie: ClassVar[str] = "sio:SubstrateRole"
    class_name: ClassVar[str] = "SubstrateRole"
    class_model_uri: ClassVar[URIRef] = SIO.SubstrateRole


class Co-enzymeRole(SubstrateRole):
    """
    A co-factor role in which the chemical entity is modified during catalysis and must be regenerated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Co-enzymeRole"]
    class_class_curie: ClassVar[str] = "sio:Co-enzymeRole"
    class_name: ClassVar[str] = "Co-enzymeRole"
    class_model_uri: ClassVar[URIRef] = SIO.Co-enzymeRole


class Co-substrateRole(Co-enzymeRole):
    """
    A co-enzyme role of a chemical entity that is transiently associated, and is regenerated in a separate reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Co-substrateRole"]
    class_class_curie: ClassVar[str] = "sio:Co-substrateRole"
    class_name: ClassVar[str] = "Co-substrateRole"
    class_model_uri: ClassVar[URIRef] = SIO.Co-substrateRole


class ProstheticGroupRole(Co-enzymeRole):
    """
    A coenzyme role of a chemical entity that is covalently bonded to the  enzyme.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProstheticGroupRole
    class_class_curie: ClassVar[str] = "sio:ProstheticGroupRole"
    class_name: ClassVar[str] = "ProstheticGroupRole"
    class_model_uri: ClassVar[URIRef] = SIO.ProstheticGroupRole


class Suffering(Hurt):
    """
    Suffering is the unpleasant emotion and aversion associated with the perception of harm or threat of harm in an
    individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Suffering
    class_class_curie: ClassVar[str] = "sio:Suffering"
    class_name: ClassVar[str] = "Suffering"
    class_model_uri: ClassVar[URIRef] = SIO.Suffering


class Suicidal(NegativeEmotion):
    """
    suicidal is the emotion of being deeply unhappy or depressed with thoughts of killing one's self.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Suicidal
    class_class_curie: ClassVar[str] = "sio:Suicidal"
    class_name: ClassVar[str] = "Suicidal"
    class_model_uri: ClassVar[URIRef] = SIO.Suicidal


class SulfurAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SulfurAtom
    class_class_curie: ClassVar[str] = "sio:SulfurAtom"
    class_name: ClassVar[str] = "SulfurAtom"
    class_model_uri: ClassVar[URIRef] = SIO.SulfurAtom


class Supernatant(CentrifugationSubstance):
    """
    A supernatent is a liquid substance that remains after centrifugation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Supernatant
    class_class_curie: ClassVar[str] = "sio:Supernatant"
    class_name: ClassVar[str] = "Supernatant"
    class_model_uri: ClassVar[URIRef] = SIO.Supernatant


class Surprise(PositiveEmotion):
    """
    surprise is a brief emotion experienced as the result of an unexpected event.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Surprise
    class_class_curie: ClassVar[str] = "sio:Surprise"
    class_name: ClassVar[str] = "Surprise"
    class_model_uri: ClassVar[URIRef] = SIO.Surprise


class Suspended(ProcessStatus):
    """
    suspended is the status of a process that is no longer progressing towards completion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Suspended
    class_class_curie: ClassVar[str] = "sio:Suspended"
    class_name: ClassVar[str] = "Suspended"
    class_model_uri: ClassVar[URIRef] = SIO.Suspended


class Symbol(Representation):
    """
    A symbol is a proposition about what an entity represents.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Symbol
    class_class_curie: ClassVar[str] = "sio:Symbol"
    class_name: ClassVar[str] = "Symbol"
    class_model_uri: ClassVar[URIRef] = SIO.Symbol


class Syndrome(Description):
    """
    A syndrome is composed of a set of several clinically recognizable features, signs (observed by someone other than
    the patient), symptoms (reported by the patient), phenomena or characteristics that often occur together.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Syndrome
    class_class_curie: ClassVar[str] = "sio:Syndrome"
    class_name: ClassVar[str] = "Syndrome"
    class_model_uri: ClassVar[URIRef] = SIO.Syndrome


class SynthesisReaction(InorganicReaction):
    """
    A synthesis reaction is an inorganic reaction in which two or more molecules are chemically bonded together to
    produce a single product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SynthesisReaction
    class_class_curie: ClassVar[str] = "sio:SynthesisReaction"
    class_name: ClassVar[str] = "SynthesisReaction"
    class_model_uri: ClassVar[URIRef] = SIO.SynthesisReaction


class SyntheticQuality(ObjectRelationalQuality):
    """
    synthetic quality is the quality of a manufactured object that has similar properties as naturally occuring
    objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SyntheticQuality
    class_class_curie: ClassVar[str] = "sio:SyntheticQuality"
    class_name: ClassVar[str] = "SyntheticQuality"
    class_model_uri: ClassVar[URIRef] = SIO.SyntheticQuality


class Table(Figure):
    """
    A table is a figure that consists of an ordered arrangement of columns and rows.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Table
    class_class_curie: ClassVar[str] = "sio:Table"
    class_name: ClassVar[str] = "Table"
    class_model_uri: ClassVar[URIRef] = SIO.Table


class TantalumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TantalumAtom
    class_class_curie: ClassVar[str] = "sio:TantalumAtom"
    class_name: ClassVar[str] = "TantalumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.TantalumAtom


class Target(YAMLRoot):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Target
    class_class_curie: ClassVar[str] = "sio:Target"
    class_name: ClassVar[str] = "Target"
    class_model_uri: ClassVar[URIRef] = SIO.Target


class Substrate(Target):
    """
    A substrate is a molecule that is consumed in the course of a biochemical reaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Substrate
    class_class_curie: ClassVar[str] = "sio:Substrate"
    class_name: ClassVar[str] = "Substrate"
    class_model_uri: ClassVar[URIRef] = SIO.Substrate


class TechnetiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TechnetiumAtom
    class_class_curie: ClassVar[str] = "sio:TechnetiumAtom"
    class_name: ClassVar[str] = "TechnetiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.TechnetiumAtom


class Telephone(CommunicationDevice):
    """
    The telephone is a communications device that transmits and receives sounds, and are minimally composed of a
    microphone to speak into, a speaker'which reproduces the voice of the other person and a ringer which makes a
    sound to alert the owner when a call is coming in.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Telephone
    class_class_curie: ClassVar[str] = "sio:Telephone"
    class_name: ClassVar[str] = "Telephone"
    class_model_uri: ClassVar[URIRef] = SIO.Telephone


class TelevisionProgram(Media):
    """
    A television program is a audiovisual media that is produced and broadcast using a television.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TelevisionProgram
    class_class_curie: ClassVar[str] = "sio:TelevisionProgram"
    class_name: ClassVar[str] = "TelevisionProgram"
    class_model_uri: ClassVar[URIRef] = SIO.TelevisionProgram


class TelluriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TelluriumAtom
    class_class_curie: ClassVar[str] = "sio:TelluriumAtom"
    class_name: ClassVar[str] = "TelluriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.TelluriumAtom


class TemporalQualifier(InformationalQuality):
    """
    a temporal qualifier is pertains to the frequency of the event of interest.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TemporalQualifier
    class_class_curie: ClassVar[str] = "sio:TemporalQualifier"
    class_name: ClassVar[str] = "TemporalQualifier"
    class_model_uri: ClassVar[URIRef] = SIO.TemporalQualifier


class Always(TemporalQualifier):
    """
    always indicates that the event occurs at all times.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Always
    class_class_curie: ClassVar[str] = "sio:Always"
    class_name: ClassVar[str] = "Always"
    class_model_uri: ClassVar[URIRef] = SIO.Always


class MostOfTheTime(TemporalQualifier):
    """
    most refers to in the majority of occasions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MostOfTheTime
    class_class_curie: ClassVar[str] = "sio:MostOfTheTime"
    class_name: ClassVar[str] = "MostOfTheTime"
    class_model_uri: ClassVar[URIRef] = SIO.MostOfTheTime


class Never(TemporalQualifier):
    """
    never refers to in none of the occasions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Never
    class_class_curie: ClassVar[str] = "sio:Never"
    class_name: ClassVar[str] = "Never"
    class_model_uri: ClassVar[URIRef] = SIO.Never


class SomeOfTheTime(TemporalQualifier):
    """
    some refers to in the minority of occasions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SomeOfTheTime
    class_class_curie: ClassVar[str] = "sio:SomeOfTheTime"
    class_name: ClassVar[str] = "SomeOfTheTime"
    class_model_uri: ClassVar[URIRef] = SIO.SomeOfTheTime


class Tensor(MathematicalEntity):
    """
    a tensor is a n-dimensional array.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Tensor
    class_class_curie: ClassVar[str] = "sio:Tensor"
    class_name: ClassVar[str] = "Tensor"
    class_model_uri: ClassVar[URIRef] = SIO.Tensor


class RankNonzeroTensor(Tensor):
    """
    a rank nonzero tensor is a tensor with a rank greater than zero.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RankNonzeroTensor
    class_class_curie: ClassVar[str] = "sio:RankNonzeroTensor"
    class_name: ClassVar[str] = "RankNonzeroTensor"
    class_model_uri: ClassVar[URIRef] = SIO.RankNonzeroTensor


class Matrix(RankNonzeroTensor):
    """
    a matrix is a rank 2 tensor. It is represented as a rectangular array or table of numbers, symbols, or expressions
    arranged in rows and columns.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Matrix
    class_class_curie: ClassVar[str] = "sio:Matrix"
    class_name: ClassVar[str] = "Matrix"
    class_model_uri: ClassVar[URIRef] = SIO.Matrix


class Scalar(Tensor):
    """
    a scalar is a rank 0 tensor and is an element of a field that is used to define a vector space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Scalar
    class_class_curie: ClassVar[str] = "sio:Scalar"
    class_name: ClassVar[str] = "Scalar"
    class_model_uri: ClassVar[URIRef] = SIO.Scalar


class Number(Scalar):
    """
    A number is a tensor of rank 0.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Number
    class_class_curie: ClassVar[str] = "sio:Number"
    class_name: ClassVar[str] = "Number"
    class_model_uri: ClassVar[URIRef] = SIO.Number


@dataclass
class MeasurementValue(Number):
    """
    A measurement value is a quantitative description that reflects the magnitude of some attribute.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MeasurementValue
    class_class_curie: ClassVar[str] = "sio:MeasurementValue"
    class_name: ClassVar[str] = "MeasurementValue"
    class_model_uri: ClassVar[URIRef] = SIO.MeasurementValue

    isMeasurementValueOf: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isMeasurementValueOf is not None and not isinstance(self.isMeasurementValueOf, Entity):
            self.isMeasurementValueOf = Entity(**as_dict(self.isMeasurementValueOf))

        super().__post_init__(**kwargs)


class Position(MeasurementValue):
    """
    A measurement of a spatial location relative to a frame of reference or other objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Position
    class_class_curie: ClassVar[str] = "sio:Position"
    class_name: ClassVar[str] = "Position"
    class_model_uri: ClassVar[URIRef] = SIO.Position


class Altitude(Position):
    """
    Altitude is a distance above sea level.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Altitude
    class_class_curie: ClassVar[str] = "sio:Altitude"
    class_name: ClassVar[str] = "Altitude"
    class_model_uri: ClassVar[URIRef] = SIO.Altitude


class CenterOfMass(Position):
    """
    The center of mass (aka barycenter) is the weighted average location of all the mass in a body or group of bodies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CenterOfMass
    class_class_curie: ClassVar[str] = "sio:CenterOfMass"
    class_name: ClassVar[str] = "CenterOfMass"
    class_model_uri: ClassVar[URIRef] = SIO.CenterOfMass


class Coordinate(Position):
    """
    A coordinate is a measurement of position in n-dimensional space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Coordinate
    class_class_curie: ClassVar[str] = "sio:Coordinate"
    class_name: ClassVar[str] = "Coordinate"
    class_model_uri: ClassVar[URIRef] = SIO.Coordinate


class CartesianCoordinate(Coordinate):
    """
    A Cartesian coordinate is the signed distance of a point to some referent line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CartesianCoordinate
    class_class_curie: ClassVar[str] = "sio:CartesianCoordinate"
    class_name: ClassVar[str] = "CartesianCoordinate"
    class_model_uri: ClassVar[URIRef] = SIO.CartesianCoordinate


class 3DCartesianCoordinate(CartesianCoordinate):
    """
    A 3D cartesian coordinate is a coordinate that is composed of an x, y and z coordinate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["3DCartesianCoordinate"]
    class_class_curie: ClassVar[str] = "sio:3DCartesianCoordinate"
    class_name: ClassVar[str] = "3DCartesianCoordinate"
    class_model_uri: ClassVar[URIRef] = SIO.3DCartesianCoordinate


class GeographicPosition(Position):
    """
    A geographic position is the coordinate of an entity against some geographic coordinate system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeographicPosition
    class_class_curie: ClassVar[str] = "sio:GeographicPosition"
    class_name: ClassVar[str] = "GeographicPosition"
    class_model_uri: ClassVar[URIRef] = SIO.GeographicPosition


class Latitude(GeographicPosition):
    """
    Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the
    equatorial plane
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Latitude
    class_class_curie: ClassVar[str] = "sio:Latitude"
    class_name: ClassVar[str] = "Latitude"
    class_model_uri: ClassVar[URIRef] = SIO.Latitude


class LinearPosition(Position):
    """
    A linear position is the position of some object against a linear positioning system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LinearPosition
    class_class_curie: ClassVar[str] = "sio:LinearPosition"
    class_name: ClassVar[str] = "LinearPosition"
    class_model_uri: ClassVar[URIRef] = SIO.LinearPosition


class EndPosition(LinearPosition):
    """
    An end position is the distal position of an object relative to an origin in a linear system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EndPosition
    class_class_curie: ClassVar[str] = "sio:EndPosition"
    class_name: ClassVar[str] = "EndPosition"
    class_model_uri: ClassVar[URIRef] = SIO.EndPosition


class Longitude(GeographicPosition):
    """
    Longitude is a geographic position that refers to the angle east or west of a reference meridian between the two
    geographical poles to another meridian that passes through an arbitrary point.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Longitude
    class_class_curie: ClassVar[str] = "sio:Longitude"
    class_name: ClassVar[str] = "Longitude"
    class_model_uri: ClassVar[URIRef] = SIO.Longitude


class OrdinalPosition(LinearPosition):
    """
    A ordinal position is a number that designates the position of an entity from the first entity in an ordered
    sequence of entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OrdinalPosition
    class_class_curie: ClassVar[str] = "sio:OrdinalPosition"
    class_name: ClassVar[str] = "OrdinalPosition"
    class_model_uri: ClassVar[URIRef] = SIO.OrdinalPosition


class CharacterPosition(OrdinalPosition):
    """
    The ordinal position of a character in a sequence of characters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CharacterPosition
    class_class_curie: ClassVar[str] = "sio:CharacterPosition"
    class_name: ClassVar[str] = "CharacterPosition"
    class_model_uri: ClassVar[URIRef] = SIO.CharacterPosition


class Orientation(Position):
    """
    orientation is an angle between the bearer and an axis, or the angle between the bearer and another object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Orientation
    class_class_curie: ClassVar[str] = "sio:Orientation"
    class_name: ClassVar[str] = "Orientation"
    class_model_uri: ClassVar[URIRef] = SIO.Orientation


class PolarCoordinate(Coordinate):
    """
    A polar coordinate is a position characterized by a distance from a fixed point and an angle from a fixed
    direction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PolarCoordinate
    class_class_curie: ClassVar[str] = "sio:PolarCoordinate"
    class_name: ClassVar[str] = "PolarCoordinate"
    class_model_uri: ClassVar[URIRef] = SIO.PolarCoordinate


class PostalCode(GeographicPosition):
    """
    A postal code is a geographic coordinate composed of a series of letters and/or digits appended to a postal
    address for the purpose of sorting mail.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PostalCode
    class_class_curie: ClassVar[str] = "sio:PostalCode"
    class_name: ClassVar[str] = "PostalCode"
    class_model_uri: ClassVar[URIRef] = SIO.PostalCode


class ProcessNumber(OrdinalPosition):
    """
    process number is a number associated with a process that denotes its ordinal position in a set of processes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProcessNumber
    class_class_curie: ClassVar[str] = "sio:ProcessNumber"
    class_name: ClassVar[str] = "ProcessNumber"
    class_model_uri: ClassVar[URIRef] = SIO.ProcessNumber


@dataclass
class Quantity(MeasurementValue):
    """
    A quantity is an informational entity that gives the magnitude of a property.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Quantity
    class_class_curie: ClassVar[str] = "sio:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = SIO.Quantity

    isNumericallyComparableTo: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isNumericallyComparableTo is not None and not isinstance(self.isNumericallyComparableTo, Quantity):
            self.isNumericallyComparableTo = Quantity(**as_dict(self.isNumericallyComparableTo))

        super().__post_init__(**kwargs)


class CentralityMeasure(Quantity):
    """
    A central tendency measure is a central value or a typical value for a probability distribution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CentralityMeasure
    class_class_curie: ClassVar[str] = "sio:CentralityMeasure"
    class_name: ClassVar[str] = "CentralityMeasure"
    class_model_uri: ClassVar[URIRef] = SIO.CentralityMeasure


class DimensionalQuantity(Quantity):
    """
    A dimensional quantity is a quantity that has an associated unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DimensionalQuantity
    class_class_curie: ClassVar[str] = "sio:DimensionalQuantity"
    class_name: ClassVar[str] = "DimensionalQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.DimensionalQuantity


class Age(DimensionalQuantity):
    """
    age is the length of time that a person has lived or a thing has existed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Age
    class_class_curie: ClassVar[str] = "sio:Age"
    class_name: ClassVar[str] = "Age"
    class_model_uri: ClassVar[URIRef] = SIO.Age


class DimensionlessQuantity(Quantity):
    """
    A dimensionless quantity is a quantity that has no associated unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DimensionlessQuantity
    class_class_curie: ClassVar[str] = "sio:DimensionlessQuantity"
    class_name: ClassVar[str] = "DimensionlessQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.DimensionlessQuantity


class Count(DimensionlessQuantity):
    """
    The number of elements of a finite set of objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Count
    class_class_curie: ClassVar[str] = "sio:Count"
    class_name: ClassVar[str] = "Count"
    class_model_uri: ClassVar[URIRef] = SIO.Count


class CopyNumberVariation(Count):
    """
    copy number variation refers to the number of deletions/duplications of a DNA region as compared to some reference
    state.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CopyNumberVariation
    class_class_curie: ClassVar[str] = "sio:CopyNumberVariation"
    class_name: ClassVar[str] = "CopyNumberVariation"
    class_model_uri: ClassVar[URIRef] = SIO.CopyNumberVariation


class DifferenceInNumberOfObjectsProduced(Count):
    """
    A difference in number of objects produced is a count of the number of objects produced with respect to a second
    variable (space, time, etc)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DifferenceInNumberOfObjectsProduced
    class_class_curie: ClassVar[str] = "sio:DifferenceInNumberOfObjectsProduced"
    class_name: ClassVar[str] = "DifferenceInNumberOfObjectsProduced"
    class_model_uri: ClassVar[URIRef] = SIO.DifferenceInNumberOfObjectsProduced


class DecreaseInNumberOfObjectsProduced(DifferenceInNumberOfObjectsProduced):
    """
    An decrease in the number of objects produced is the negative value of a difference in number of objects produced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreaseInNumberOfObjectsProduced
    class_class_curie: ClassVar[str] = "sio:DecreaseInNumberOfObjectsProduced"
    class_name: ClassVar[str] = "DecreaseInNumberOfObjectsProduced"
    class_model_uri: ClassVar[URIRef] = SIO.DecreaseInNumberOfObjectsProduced


class Dose(DimensionalQuantity):
    """
    A dose is the quantity of a chemical substance administered to a biological system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Dose
    class_class_curie: ClassVar[str] = "sio:Dose"
    class_name: ClassVar[str] = "Dose"
    class_model_uri: ClassVar[URIRef] = SIO.Dose


class EditionNumber(Count):
    """
    An edition number is count of a literary work edited and published, as by a certain editor or in a certain manner
    including being printed during some interval of time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EditionNumber
    class_class_curie: ClassVar[str] = "sio:EditionNumber"
    class_name: ClassVar[str] = "EditionNumber"
    class_model_uri: ClassVar[URIRef] = SIO.EditionNumber


class EffectiveDose(Dose):
    """
    effective dose is the amount of a substance required to produce an effect on a predefined percentage of a
    population.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EffectiveDose
    class_class_curie: ClassVar[str] = "sio:EffectiveDose"
    class_name: ClassVar[str] = "EffectiveDose"
    class_model_uri: ClassVar[URIRef] = SIO.EffectiveDose


class GeneExpressionValue(DimensionalQuantity):
    """
    A gene expression value is a measured value obtained from a gene expression experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeneExpressionValue
    class_class_curie: ClassVar[str] = "sio:GeneExpressionValue"
    class_name: ClassVar[str] = "GeneExpressionValue"
    class_model_uri: ClassVar[URIRef] = SIO.GeneExpressionValue


class GenerationNumber(Count):
    """
    generation number is a count of the number of biological reproduction events elapsed from some starting reference
    point.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GenerationNumber
    class_class_curie: ClassVar[str] = "sio:GenerationNumber"
    class_name: ClassVar[str] = "GenerationNumber"
    class_model_uri: ClassVar[URIRef] = SIO.GenerationNumber


class IncreaseInNumberOfObjectsProduced(DifferenceInNumberOfObjectsProduced):
    """
    An increase in the number of objects produced is the positive value of a difference in number of objects produced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreaseInNumberOfObjectsProduced
    class_class_curie: ClassVar[str] = "sio:IncreaseInNumberOfObjectsProduced"
    class_name: ClassVar[str] = "IncreaseInNumberOfObjectsProduced"
    class_model_uri: ClassVar[URIRef] = SIO.IncreaseInNumberOfObjectsProduced


class Likelihood(Quantity):
    """
    Likelihood is the hypothetical probability that an event that has already occurred would yield a specific outcome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Likelihood
    class_class_curie: ClassVar[str] = "sio:Likelihood"
    class_name: ClassVar[str] = "Likelihood"
    class_model_uri: ClassVar[URIRef] = SIO.Likelihood


class LogLikelihood(Likelihood):
    """
    Log likelihood is the natural logarithm of the likelihood function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LogLikelihood
    class_class_curie: ClassVar[str] = "sio:LogLikelihood"
    class_name: ClassVar[str] = "LogLikelihood"
    class_model_uri: ClassVar[URIRef] = SIO.LogLikelihood


class MaximalValue(Quantity):
    """
    A maximal value is largest value of an attribute for the entities in the defined set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaximalValue
    class_class_curie: ClassVar[str] = "sio:MaximalValue"
    class_name: ClassVar[str] = "MaximalValue"
    class_model_uri: ClassVar[URIRef] = SIO.MaximalValue


class Mean(CentralityMeasure):
    """
    A mean is the central tendency of a collection of numbers taken as the sum of the numbers divided by the size of
    the collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Mean
    class_class_curie: ClassVar[str] = "sio:Mean"
    class_name: ClassVar[str] = "Mean"
    class_model_uri: ClassVar[URIRef] = SIO.Mean


class Median(CentralityMeasure):
    """
    A median is the numerical value separating the higher half of a sample, a population, or a probability
    distribution, from the lower half.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Median
    class_class_curie: ClassVar[str] = "sio:Median"
    class_name: ClassVar[str] = "Median"
    class_model_uri: ClassVar[URIRef] = SIO.Median


class MemberCount(Count):
    """
    A count of the instances of a class or members in a collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MemberCount
    class_class_curie: ClassVar[str] = "sio:MemberCount"
    class_name: ClassVar[str] = "MemberCount"
    class_model_uri: ClassVar[URIRef] = SIO.MemberCount


class MinimalValue(Quantity):
    """
    A minimal value is smallest value of an attribute for the entities in the defined set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MinimalValue
    class_class_curie: ClassVar[str] = "sio:MinimalValue"
    class_name: ClassVar[str] = "MinimalValue"
    class_model_uri: ClassVar[URIRef] = SIO.MinimalValue


class Mode(CentralityMeasure):
    """
    A mode is the value that appears most often in a set of data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Mode
    class_class_curie: ClassVar[str] = "sio:Mode"
    class_name: ClassVar[str] = "Mode"
    class_model_uri: ClassVar[URIRef] = SIO.Mode


class NumberOfObjectsConsumed(Count):
    """
    number of objects consumed is a count of objects that were consumed in some process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NumberOfObjectsConsumed
    class_class_curie: ClassVar[str] = "sio:NumberOfObjectsConsumed"
    class_name: ClassVar[str] = "NumberOfObjectsConsumed"
    class_model_uri: ClassVar[URIRef] = SIO.NumberOfObjectsConsumed


class NumberOfObjectsProduced(Count):
    """
    number of objects produced is a count of objects that were produced in some process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NumberOfObjectsProduced
    class_class_curie: ClassVar[str] = "sio:NumberOfObjectsProduced"
    class_name: ClassVar[str] = "NumberOfObjectsProduced"
    class_model_uri: ClassVar[URIRef] = SIO.NumberOfObjectsProduced


class PH(DimensionlessQuantity):
    """
    pH is a measure of the activity of the (solvated) hydrogen ion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PH
    class_class_curie: ClassVar[str] = "sio:PH"
    class_name: ClassVar[str] = "PH"
    class_model_uri: ClassVar[URIRef] = SIO.PH


class PageNumber(Count):
    """
    A page number is the count of a page in a sequence of pages.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PageNumber
    class_class_curie: ClassVar[str] = "sio:PageNumber"
    class_name: ClassVar[str] = "PageNumber"
    class_model_uri: ClassVar[URIRef] = SIO.PageNumber


class PageTotal(Count):
    """
    A page total is a textual entity that is about the number of pages in some informational entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PageTotal
    class_class_curie: ClassVar[str] = "sio:PageTotal"
    class_name: ClassVar[str] = "PageTotal"
    class_model_uri: ClassVar[URIRef] = SIO.PageTotal


class ProbabilityMeasure(DimensionlessQuantity):
    """
    A probability measure is quantity of how likely it is that some event will occur.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProbabilityMeasure
    class_class_curie: ClassVar[str] = "sio:ProbabilityMeasure"
    class_name: ClassVar[str] = "ProbabilityMeasure"
    class_model_uri: ClassVar[URIRef] = SIO.ProbabilityMeasure


class ExpectedValue(ProbabilityMeasure):
    """
    An expected value (or e-value) is the weighted average of all possible values that a random variable can take on.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ExpectedValue
    class_class_curie: ClassVar[str] = "sio:ExpectedValue"
    class_name: ClassVar[str] = "ExpectedValue"
    class_model_uri: ClassVar[URIRef] = SIO.ExpectedValue


class ProbabilityValue(ProbabilityMeasure):
    """
    A p-value or probability value is the probability of obtaining a test statistic at least as extreme as the one
    that was actually observed, assuming that the null hypothesis is true
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProbabilityValue
    class_class_curie: ClassVar[str] = "sio:ProbabilityValue"
    class_name: ClassVar[str] = "ProbabilityValue"
    class_model_uri: ClassVar[URIRef] = SIO.ProbabilityValue


class ProteinExpressionValue(DimensionalQuantity):
    """
    A protein expression value is a quantity obtained from a protein expression experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ProteinExpressionValue
    class_class_curie: ClassVar[str] = "sio:ProteinExpressionValue"
    class_name: ClassVar[str] = "ProteinExpressionValue"
    class_model_uri: ClassVar[URIRef] = SIO.ProteinExpressionValue


class Quantile(DimensionlessQuantity):
    """
    A quantile is a quantity that divides the range of a probability distribution into continuous intervals with equal
    probabilities, or dividing the observations in a sample in the same way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Quantile
    class_class_curie: ClassVar[str] = "sio:Quantile"
    class_name: ClassVar[str] = "Quantile"
    class_model_uri: ClassVar[URIRef] = SIO.Quantile


class Percentile(Quantile):
    """
    A percentile (or a centile) is a quantile that divides the given probability distribution, or sample, into 100
    equal-sized intervals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Percentile
    class_class_curie: ClassVar[str] = "sio:Percentile"
    class_name: ClassVar[str] = "Percentile"
    class_model_uri: ClassVar[URIRef] = SIO.Percentile


class RateOfChange(DimensionalQuantity):
    """
    The amount of change accumulated per unit time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RateOfChange
    class_class_curie: ClassVar[str] = "sio:RateOfChange"
    class_name: ClassVar[str] = "RateOfChange"
    class_model_uri: ClassVar[URIRef] = SIO.RateOfChange


class Frequency(RateOfChange):
    """
    Frequency is the number of occurrences of a repeating event per unit time
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Frequency
    class_class_curie: ClassVar[str] = "sio:Frequency"
    class_name: ClassVar[str] = "Frequency"
    class_model_uri: ClassVar[URIRef] = SIO.Frequency


class Ratio(DimensionlessQuantity):
    """
    A ratio is a relationship between two numbers of the same kind expressed arithmetically as a dimensionless
    quotient of the two which explicitly indicates how many times the first number contains the second.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Ratio
    class_class_curie: ClassVar[str] = "sio:Ratio"
    class_name: ClassVar[str] = "Ratio"
    class_model_uri: ClassVar[URIRef] = SIO.Ratio


class AspectRatio(Ratio):
    """
    The aspect ratio of a geometric shape is the ratio of its sizes in different dimensions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AspectRatio
    class_class_curie: ClassVar[str] = "sio:AspectRatio"
    class_name: ClassVar[str] = "AspectRatio"
    class_model_uri: ClassVar[URIRef] = SIO.AspectRatio


class DifferentialGeneExpressionRatio(Ratio):
    """
    A differential gene expression ratio is the ratio of gene expression values from a test sample compared to a
    control sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DifferentialGeneExpressionRatio
    class_class_curie: ClassVar[str] = "sio:DifferentialGeneExpressionRatio"
    class_name: ClassVar[str] = "DifferentialGeneExpressionRatio"
    class_model_uri: ClassVar[URIRef] = SIO.DifferentialGeneExpressionRatio


class DisGeNETDiseaseSpecificity(Ratio):
    """
    DisGeNET Disease specificity is a measure of disease coverage. It is calculated from the negative base 2 log of
    the ratio of number of diseases associated to the total number of diseases.

    The measure is described here: http://www.disgenet.org/web/DisGeNET/menu/dbinfo#specificity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DisGeNETDiseaseSpecificity
    class_class_curie: ClassVar[str] = "sio:DisGeNETDiseaseSpecificity"
    class_name: ClassVar[str] = "DisGeNETDiseaseSpecificity"
    class_model_uri: ClassVar[URIRef] = SIO.DisGeNETDiseaseSpecificity


class DisGeNETPleiotropyIndex(Ratio):
    """
    The DisGeNET pleiotropy index is a measure of specificity as it pertains to classes of disease. The disease
    pleotropy index is computed from the ratio of the number of disease classes associated with an entity over the
    total number of disease classes multplied by 100.

    The measure is defined here: http://www.disgenet.org/web/DisGeNET/menu/dbinfo#pleiotropy
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DisGeNETPleiotropyIndex
    class_class_curie: ClassVar[str] = "sio:DisGeNETPleiotropyIndex"
    class_name: ClassVar[str] = "DisGeNETPleiotropyIndex"
    class_model_uri: ClassVar[URIRef] = SIO.DisGeNETPleiotropyIndex


class Percentage(Ratio):
    """
    A percentage is a number that is a ratio expressed as a fraction of 100. It is denoted using the percent sign "%".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Percentage
    class_class_curie: ClassVar[str] = "sio:Percentage"
    class_name: ClassVar[str] = "Percentage"
    class_model_uri: ClassVar[URIRef] = SIO.Percentage


class SequenceElementPosition(LinearPosition):
    """
    A sequence element position is the position of an element of a linear sequence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceElementPosition
    class_class_curie: ClassVar[str] = "sio:SequenceElementPosition"
    class_name: ClassVar[str] = "SequenceElementPosition"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceElementPosition


class SequenceEndPosition(EndPosition):
    """
    A sequence end position is the position of the last character in a sequence of characters relative to some linear
    frame of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceEndPosition
    class_class_curie: ClassVar[str] = "sio:SequenceEndPosition"
    class_name: ClassVar[str] = "SequenceEndPosition"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceEndPosition


class SequenceStartPosition(SequenceElementPosition):
    """
    A sequence start position is the start position for a sequence of characters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceStartPosition
    class_class_curie: ClassVar[str] = "sio:SequenceStartPosition"
    class_name: ClassVar[str] = "SequenceStartPosition"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceStartPosition


class Slope(Ratio):
    """
    A slope or gradient of a line describes its steepness, incline, or grade. A higher slope value indicates a steeper
    incline. Slope is normally described by the ratio of the "rise" divided by the "run" between two points on a line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Slope
    class_class_curie: ClassVar[str] = "sio:Slope"
    class_name: ClassVar[str] = "Slope"
    class_model_uri: ClassVar[URIRef] = SIO.Slope


class SpatialQuantity(DimensionalQuantity):
    """
    A spatial quantity is a quantity obtained from measuring the spatial extent of an entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpatialQuantity
    class_class_curie: ClassVar[str] = "sio:SpatialQuantity"
    class_name: ClassVar[str] = "SpatialQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.SpatialQuantity


class 1DExtentQuantity(SpatialQuantity):
    """
    A quantity that extends in single dimension.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["1DExtentQuantity"]
    class_class_curie: ClassVar[str] = "sio:1DExtentQuantity"
    class_name: ClassVar[str] = "1DExtentQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.1DExtentQuantity


class 2DExtentQuantity(SpatialQuantity):
    """
    A quantity that extends in two dimensions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["2DExtentQuantity"]
    class_class_curie: ClassVar[str] = "sio:2DExtentQuantity"
    class_name: ClassVar[str] = "2DExtentQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.2DExtentQuantity


class 3DExtentQuantity(SpatialQuantity):
    """
    A quantity that extends in three dimensions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["3DExtentQuantity"]
    class_class_curie: ClassVar[str] = "sio:3DExtentQuantity"
    class_name: ClassVar[str] = "3DExtentQuantity"
    class_model_uri: ClassVar[URIRef] = SIO.3DExtentQuantity


class Area(2DExtentQuantity):
    """
    area is a quantity that pertains to the extent of a two-dimensional surface or shape, or planar lamina, in the
    plane.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Area
    class_class_curie: ClassVar[str] = "sio:Area"
    class_name: ClassVar[str] = "Area"
    class_model_uri: ClassVar[URIRef] = SIO.Area


class Concentration(3DExtentQuantity):
    """
    concentration is the amount of substance per unit volume of a solution
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Concentration
    class_class_curie: ClassVar[str] = "sio:Concentration"
    class_name: ClassVar[str] = "Concentration"
    class_model_uri: ClassVar[URIRef] = SIO.Concentration


class Density(3DExtentQuantity):
    """
    Density (volumetric mass density) is the quantity of mass per unit volume of a substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Density
    class_class_curie: ClassVar[str] = "sio:Density"
    class_name: ClassVar[str] = "Density"
    class_model_uri: ClassVar[URIRef] = SIO.Density


class Depth(1DExtentQuantity):
    """
    depth is the dimensional extent into a plane of a 3D projection of the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Depth
    class_class_curie: ClassVar[str] = "sio:Depth"
    class_name: ClassVar[str] = "Depth"
    class_model_uri: ClassVar[URIRef] = SIO.Depth


class Height(1DExtentQuantity):
    """
    height is the one dimensional extent along the vertical projection of a 3D object from a base plane of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Height
    class_class_curie: ClassVar[str] = "sio:Height"
    class_name: ClassVar[str] = "Height"
    class_model_uri: ClassVar[URIRef] = SIO.Height


class Length(1DExtentQuantity):
    """
    length is the longer dimensional extent along a 2D projection of the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Length
    class_class_curie: ClassVar[str] = "sio:Length"
    class_name: ClassVar[str] = "Length"
    class_model_uri: ClassVar[URIRef] = SIO.Length


class LengthOfPerimeter(2DExtentQuantity):
    """
    A perimeter is a length of the outline that surrounds a two-dimensional shape.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LengthOfPerimeter
    class_class_curie: ClassVar[str] = "sio:LengthOfPerimeter"
    class_name: ClassVar[str] = "LengthOfPerimeter"
    class_model_uri: ClassVar[URIRef] = SIO.LengthOfPerimeter


class Circumference(LengthOfPerimeter):
    """
    circumference is the length of the outline of a circle or ellipse. it is defined as c = 2*pi*r, where r is the
    radius.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Circumference
    class_class_curie: ClassVar[str] = "sio:Circumference"
    class_name: ClassVar[str] = "Circumference"
    class_model_uri: ClassVar[URIRef] = SIO.Circumference


class Mass(SpatialQuantity):
    """
    mass is the quality of the amount of substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Mass
    class_class_curie: ClassVar[str] = "sio:Mass"
    class_name: ClassVar[str] = "Mass"
    class_model_uri: ClassVar[URIRef] = SIO.Mass


class SpecificGravity(Ratio):
    """
    Specific gravity is the ratio of the density of a substance to the density of a reference substance; equivalently,
    it is the ratio of the mass of a substance to the mass of a reference substance for the same given volume.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SpecificGravity
    class_class_curie: ClassVar[str] = "sio:SpecificGravity"
    class_name: ClassVar[str] = "SpecificGravity"
    class_model_uri: ClassVar[URIRef] = SIO.SpecificGravity


class Speed(RateOfChange):
    """
    Speed is the rate of change of an object's position.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Speed
    class_class_curie: ClassVar[str] = "sio:Speed"
    class_name: ClassVar[str] = "Speed"
    class_model_uri: ClassVar[URIRef] = SIO.Speed


class StandardDeviation(Quantity):
    """
    A standard deviation (represented by the symbol σ) is the quantity of variation from the average (mean, or
    expected value).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StandardDeviation
    class_class_curie: ClassVar[str] = "sio:StandardDeviation"
    class_name: ClassVar[str] = "StandardDeviation"
    class_model_uri: ClassVar[URIRef] = SIO.StandardDeviation


class StandardScore(ProbabilityMeasure):
    """
    A standard score is the (signed) number of standard deviations an observation or datum is above the mean.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StandardScore
    class_class_curie: ClassVar[str] = "sio:StandardScore"
    class_name: ClassVar[str] = "StandardScore"
    class_model_uri: ClassVar[URIRef] = SIO.StandardScore


class StartPosition(LinearPosition):
    """
    A start position is the proximal position of an object relative to an origin in a linear system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StartPosition
    class_class_curie: ClassVar[str] = "sio:StartPosition"
    class_name: ClassVar[str] = "StartPosition"
    class_model_uri: ClassVar[URIRef] = SIO.StartPosition


class Sum(Quantity):
    """
    A sum is the result of adding a set of values together.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Sum
    class_class_curie: ClassVar[str] = "sio:Sum"
    class_name: ClassVar[str] = "Sum"
    class_model_uri: ClassVar[URIRef] = SIO.Sum


class SurfaceArea(Area):
    """
    The surface area of a is a measure of the total area that the surface of the object occupies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SurfaceArea
    class_class_curie: ClassVar[str] = "sio:SurfaceArea"
    class_name: ClassVar[str] = "SurfaceArea"
    class_model_uri: ClassVar[URIRef] = SIO.SurfaceArea


class T-statistic(Ratio):
    """
    A t-statistic is a ratio of the departure of an estimated parameter from its notional value and its standard error.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["T-statistic"]
    class_class_curie: ClassVar[str] = "sio:T-statistic"
    class_name: ClassVar[str] = "T-statistic"
    class_model_uri: ClassVar[URIRef] = SIO.T-statistic


class T-statisticBasedDecreasedDifferentialGeneExpression(DifferentialGeneExpressionRatio):
    """
    A t-statistic based decreased differential gene expression is a differential gene expression ratio in which the
    t-statistic is less than zero.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["T-statisticBasedDecreasedDifferentialGeneExpression"]
    class_class_curie: ClassVar[str] = "sio:T-statisticBasedDecreasedDifferentialGeneExpression"
    class_name: ClassVar[str] = "T-statisticBasedDecreasedDifferentialGeneExpression"
    class_model_uri: ClassVar[URIRef] = SIO.T-statisticBasedDecreasedDifferentialGeneExpression


class T-statisticBasedIncreasedDifferentialGeneExpression(DifferentialGeneExpressionRatio):
    """
    A t-statistic based increased differential gene expression is a differential gene expression ratio in which the
    t-statistic is greater than zero.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["T-statisticBasedIncreasedDifferentialGeneExpression"]
    class_class_curie: ClassVar[str] = "sio:T-statisticBasedIncreasedDifferentialGeneExpression"
    class_name: ClassVar[str] = "T-statisticBasedIncreasedDifferentialGeneExpression"
    class_model_uri: ClassVar[URIRef] = SIO.T-statisticBasedIncreasedDifferentialGeneExpression


class TerbiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TerbiumAtom
    class_class_curie: ClassVar[str] = "sio:TerbiumAtom"
    class_name: ClassVar[str] = "TerbiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.TerbiumAtom


@dataclass
class Term(LanguageEntity):
    """
    A term is a word or phrase used to denote one or more entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Term
    class_class_curie: ClassVar[str] = "sio:Term"
    class_name: ClassVar[str] = "Term"
    class_model_uri: ClassVar[URIRef] = SIO.Term

    isNarrowerThant: Optional[Union[dict, "Term"]] = None
    isMatchTo: Optional[Union[dict, "Term"]] = None
    isBroaderThant: Optional[Union[dict, "Term"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isNarrowerThant is not None and not isinstance(self.isNarrowerThant, Term):
            self.isNarrowerThant = Term(**as_dict(self.isNarrowerThant))

        if self.isMatchTo is not None and not isinstance(self.isMatchTo, Term):
            self.isMatchTo = Term(**as_dict(self.isMatchTo))

        if self.isBroaderThant is not None and not isinstance(self.isBroaderThant, Term):
            self.isBroaderThant = Term(**as_dict(self.isBroaderThant))

        super().__post_init__(**kwargs)


class Concept(Term):
    """
    A concept is term that refers to a generalization of a set of attributes or entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Concept
    class_class_curie: ClassVar[str] = "sio:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = SIO.Concept


class Category(Concept):
    """
    A category is a class of entities having particular shared characteristics.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Category
    class_class_curie: ClassVar[str] = "sio:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = SIO.Category


class Descriptor(Term):
    """
    A descriptor (index term, subject term, subject heading) is a term that captures the essence of the topic of a
    document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Descriptor
    class_class_curie: ClassVar[str] = "sio:Descriptor"
    class_name: ClassVar[str] = "Descriptor"
    class_model_uri: ClassVar[URIRef] = SIO.Descriptor


class Keyword(Descriptor):
    """
    A keyword is a descriptor in which the association of the word with the entity facilitates information retrieval.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Keyword
    class_class_curie: ClassVar[str] = "sio:Keyword"
    class_name: ClassVar[str] = "Keyword"
    class_model_uri: ClassVar[URIRef] = SIO.Keyword


class Label(Term):
    """
    a label is a term that is associated with some entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Label
    class_class_curie: ClassVar[str] = "sio:Label"
    class_name: ClassVar[str] = "Label"
    class_model_uri: ClassVar[URIRef] = SIO.Label


@dataclass
class Identifier(Label):
    """
    An identifier is a label that specifically refers to (identifies) an entity (instance/type).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Identifier
    class_class_curie: ClassVar[str] = "sio:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = SIO.Identifier

    isIdentifierFor: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isIdentifierFor is not None and not isinstance(self.isIdentifierFor, Entity):
            self.isIdentifierFor = Entity(**as_dict(self.isIdentifierFor))

        super().__post_init__(**kwargs)


class InformationalEntityIdentifier(Identifier):
    """
    An informational entity identifier is an identifier for an informational entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InformationalEntityIdentifier
    class_class_curie: ClassVar[str] = "sio:InformationalEntityIdentifier"
    class_name: ClassVar[str] = "InformationalEntityIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.InformationalEntityIdentifier


class EmailAddress(InformationalEntityIdentifier):
    """
    an email address is an identifier to send mail to particular electronic mailbox.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EmailAddress
    class_class_curie: ClassVar[str] = "sio:EmailAddress"
    class_name: ClassVar[str] = "EmailAddress"
    class_model_uri: ClassVar[URIRef] = SIO.EmailAddress


class IPNumber(InformationalEntityIdentifier):
    """
    an IP number is an number to connect to a device on the internet.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IPNumber
    class_class_curie: ClassVar[str] = "sio:IPNumber"
    class_name: ClassVar[str] = "IPNumber"
    class_model_uri: ClassVar[URIRef] = SIO.IPNumber


class LanguageLabel(Label):
    """
    A language label is a label that denotes the language of a textual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LanguageLabel
    class_class_curie: ClassVar[str] = "sio:LanguageLabel"
    class_name: ClassVar[str] = "LanguageLabel"
    class_model_uri: ClassVar[URIRef] = SIO.LanguageLabel


class Name(Label):
    """
    A name is a label used to identify an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Name
    class_class_curie: ClassVar[str] = "sio:Name"
    class_name: ClassVar[str] = "Name"
    class_model_uri: ClassVar[URIRef] = SIO.Name


class BrandName(Name):
    """
    A brand name is a trademarked and marketed name of a product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BrandName
    class_class_curie: ClassVar[str] = "sio:BrandName"
    class_name: ClassVar[str] = "BrandName"
    class_model_uri: ClassVar[URIRef] = SIO.BrandName


class CommonName(Name):
    """
    A common name is a name that is commonly used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CommonName
    class_class_curie: ClassVar[str] = "sio:CommonName"
    class_name: ClassVar[str] = "CommonName"
    class_model_uri: ClassVar[URIRef] = SIO.CommonName


class FirstName(Name):
    """
    A first name is a name that denotes a specific individual between members of a group of individuals, whose members
    usually share the same surname.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FirstName
    class_class_curie: ClassVar[str] = "sio:FirstName"
    class_name: ClassVar[str] = "FirstName"
    class_model_uri: ClassVar[URIRef] = SIO.FirstName


class GenericName(Name):
    """
    A generic name is the preferred name provided by manufacturer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GenericName
    class_class_curie: ClassVar[str] = "sio:GenericName"
    class_name: ClassVar[str] = "GenericName"
    class_model_uri: ClassVar[URIRef] = SIO.GenericName


class LastName(Name):
    """
    A last name (surname) is a name added to a given name and is part of a personal name and is often the family name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LastName
    class_class_curie: ClassVar[str] = "sio:LastName"
    class_name: ClassVar[str] = "LastName"
    class_model_uri: ClassVar[URIRef] = SIO.LastName


class MiddleName(Name):
    """
    a middle name is a name assigned to an individual that is not the first or last name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MiddleName
    class_class_curie: ClassVar[str] = "sio:MiddleName"
    class_name: ClassVar[str] = "MiddleName"
    class_model_uri: ClassVar[URIRef] = SIO.MiddleName


class MiddleInitial(MiddleName):
    """
    a middle initial is an abbreviated middle name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MiddleInitial
    class_class_curie: ClassVar[str] = "sio:MiddleInitial"
    class_name: ClassVar[str] = "MiddleInitial"
    class_model_uri: ClassVar[URIRef] = SIO.MiddleInitial


class NamespaceLabel(Label):
    """
    A namespace label is a short name for a namespace.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NamespaceLabel
    class_class_curie: ClassVar[str] = "sio:NamespaceLabel"
    class_name: ClassVar[str] = "NamespaceLabel"
    class_model_uri: ClassVar[URIRef] = SIO.NamespaceLabel


class NumericLabel(Label):
    """
    A numeric label is a number used as a label.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NumericLabel
    class_class_curie: ClassVar[str] = "sio:NumericLabel"
    class_name: ClassVar[str] = "NumericLabel"
    class_model_uri: ClassVar[URIRef] = SIO.NumericLabel


class PersonalName(Name):
    """
    A personal name is a name to identify an individual person and usually comprises of a first name and a last name.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PersonalName
    class_class_curie: ClassVar[str] = "sio:PersonalName"
    class_name: ClassVar[str] = "PersonalName"
    class_model_uri: ClassVar[URIRef] = SIO.PersonalName


class LegalName(PersonalName):
    """
    A legal name is a name given at birth, or which appears on their birth certificate, marriage certificate, or
    change of name certificate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LegalName
    class_class_curie: ClassVar[str] = "sio:LegalName"
    class_name: ClassVar[str] = "LegalName"
    class_model_uri: ClassVar[URIRef] = SIO.LegalName


class PhysicalEntityIdentifier(Identifier):
    """
    A physical entity identifier is an identifier for a physical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PhysicalEntityIdentifier
    class_class_curie: ClassVar[str] = "sio:PhysicalEntityIdentifier"
    class_name: ClassVar[str] = "PhysicalEntityIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.PhysicalEntityIdentifier


class ChemicalIdentifier(PhysicalEntityIdentifier):
    """
    A chemical identifier is an identifier for a chemical entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalIdentifier
    class_class_curie: ClassVar[str] = "sio:ChemicalIdentifier"
    class_name: ClassVar[str] = "ChemicalIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalIdentifier


class MolecularIdentifier(ChemicalIdentifier):
    """
    A molecular identifier is an identifier for a molecular entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MolecularIdentifier
    class_class_curie: ClassVar[str] = "sio:MolecularIdentifier"
    class_name: ClassVar[str] = "MolecularIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.MolecularIdentifier


class MicroarrayProbeSetIdentifier(MolecularIdentifier):
    """
    A microarray probe set identifier is an identifier for a set of probe pairs selected to represent expressed
    sequences on an array.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MicroarrayProbeSetIdentifier
    class_class_curie: ClassVar[str] = "sio:MicroarrayProbeSetIdentifier"
    class_name: ClassVar[str] = "MicroarrayProbeSetIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.MicroarrayProbeSetIdentifier


class PDBChainIdentifier(MolecularIdentifier):
    """
    A PDB chain identifier is a alphabetical label to identify a molecule in a structure provided by the Protein
    DataBank .
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PDBChainIdentifier
    class_class_curie: ClassVar[str] = "sio:PDBChainIdentifier"
    class_name: ClassVar[str] = "PDBChainIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.PDBChainIdentifier


class PositionalIdentifier(Identifier):
    """
    A positional description is a description of location using some system or frame of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PositionalIdentifier
    class_class_curie: ClassVar[str] = "sio:PositionalIdentifier"
    class_name: ClassVar[str] = "PositionalIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.PositionalIdentifier


class Address(PositionalIdentifier):
    """
    An address is a position that indicates the physical location of some entity using a social convention.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Address
    class_class_curie: ClassVar[str] = "sio:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = SIO.Address


class ApartmentNumber(PositionalIdentifier):
    """
    An apartment number is the number assigned to identify an apartment in a building of apartments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ApartmentNumber
    class_class_curie: ClassVar[str] = "sio:ApartmentNumber"
    class_name: ClassVar[str] = "ApartmentNumber"
    class_model_uri: ClassVar[URIRef] = SIO.ApartmentNumber


class PreferredName(Name):
    """
    A preferred name is the name that is generally used by some organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PreferredName
    class_class_curie: ClassVar[str] = "sio:PreferredName"
    class_name: ClassVar[str] = "PreferredName"
    class_model_uri: ClassVar[URIRef] = SIO.PreferredName


class RecordIdentifier(InformationalEntityIdentifier):
    """
    A record identifier is an identifier for a database entry.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RecordIdentifier
    class_class_curie: ClassVar[str] = "sio:RecordIdentifier"
    class_name: ClassVar[str] = "RecordIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.RecordIdentifier


class PDBRecordIdentifier(RecordIdentifier):
    """
    A PDB record identifier is an identifier for a PDB generated record.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PDBRecordIdentifier
    class_class_curie: ClassVar[str] = "sio:PDBRecordIdentifier"
    class_name: ClassVar[str] = "PDBRecordIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.PDBRecordIdentifier


class ScientificName(Name):
    """
    A scientific name is a name given through scientific nomenclature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ScientificName
    class_class_curie: ClassVar[str] = "sio:ScientificName"
    class_name: ClassVar[str] = "ScientificName"
    class_model_uri: ClassVar[URIRef] = SIO.ScientificName


class GeneSymbol(ScientificName):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GeneSymbol
    class_class_curie: ClassVar[str] = "sio:GeneSymbol"
    class_name: ClassVar[str] = "GeneSymbol"
    class_model_uri: ClassVar[URIRef] = SIO.GeneSymbol


class SoftwareProcessIdentifier(InformationalEntityIdentifier):
    """
    A software process identifier is an identifier for a software process in some operating system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareProcessIdentifier
    class_class_curie: ClassVar[str] = "sio:SoftwareProcessIdentifier"
    class_name: ClassVar[str] = "SoftwareProcessIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareProcessIdentifier


class StreetName(PositionalIdentifier):
    """
    A street name is the token given to identify a particular street.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StreetName
    class_class_curie: ClassVar[str] = "sio:StreetName"
    class_name: ClassVar[str] = "StreetName"
    class_model_uri: ClassVar[URIRef] = SIO.StreetName


class TelephoneNumber(InformationalEntityIdentifier):
    """
    a telephone number is an identifier used to connect to a physical device capable of transfering voice or data over
    a network.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TelephoneNumber
    class_class_curie: ClassVar[str] = "sio:TelephoneNumber"
    class_name: ClassVar[str] = "TelephoneNumber"
    class_model_uri: ClassVar[URIRef] = SIO.TelephoneNumber


class CellularPhoneNumber(TelephoneNumber):
    """
    a cellular phone number is a number to connect to a mobile device
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CellularPhoneNumber
    class_class_curie: ClassVar[str] = "sio:CellularPhoneNumber"
    class_name: ClassVar[str] = "CellularPhoneNumber"
    class_model_uri: ClassVar[URIRef] = SIO.CellularPhoneNumber


class FaxNumber(TelephoneNumber):
    """
    a fax number is a number to connect to fax device
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.FaxNumber
    class_class_curie: ClassVar[str] = "sio:FaxNumber"
    class_name: ClassVar[str] = "FaxNumber"
    class_model_uri: ClassVar[URIRef] = SIO.FaxNumber


class HomePhoneNumber(TelephoneNumber):
    """
    a home phone number is the number to connect to an phone at a place of residence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HomePhoneNumber
    class_class_curie: ClassVar[str] = "sio:HomePhoneNumber"
    class_name: ClassVar[str] = "HomePhoneNumber"
    class_model_uri: ClassVar[URIRef] = SIO.HomePhoneNumber


class TermVariant(Term):
    """
    A term variant is a term that is a variant of another term.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TermVariant
    class_class_curie: ClassVar[str] = "sio:TermVariant"
    class_name: ClassVar[str] = "TermVariant"
    class_model_uri: ClassVar[URIRef] = SIO.TermVariant


class Antonym(TermVariant):
    """
    An antonym is a word with opposite or nearly opposite meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Antonym
    class_class_curie: ClassVar[str] = "sio:Antonym"
    class_name: ClassVar[str] = "Antonym"
    class_model_uri: ClassVar[URIRef] = SIO.Antonym


class Homonym(TermVariant):
    """
    A homonym is a word that sounds the same but has different meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Homonym
    class_class_curie: ClassVar[str] = "sio:Homonym"
    class_name: ClassVar[str] = "Homonym"
    class_model_uri: ClassVar[URIRef] = SIO.Homonym


class Hypernym(TermVariant):
    """
    A hypernym is a term with a broader meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hypernym
    class_class_curie: ClassVar[str] = "sio:Hypernym"
    class_name: ClassVar[str] = "Hypernym"
    class_model_uri: ClassVar[URIRef] = SIO.Hypernym


class Hyponym(TermVariant):
    """
    A hyponym is a term with a narrower meaning.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hyponym
    class_class_curie: ClassVar[str] = "sio:Hyponym"
    class_name: ClassVar[str] = "Hyponym"
    class_model_uri: ClassVar[URIRef] = SIO.Hyponym


class Synonym(TermVariant):
    """
    A synonym is a word with the same or very similar meanings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Synonym
    class_class_curie: ClassVar[str] = "sio:Synonym"
    class_name: ClassVar[str] = "Synonym"
    class_model_uri: ClassVar[URIRef] = SIO.Synonym


class TerminalPoint(Point):
    """
    A terminal point is a point that defines the finite extension of a line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TerminalPoint
    class_class_curie: ClassVar[str] = "sio:TerminalPoint"
    class_name: ClassVar[str] = "TerminalPoint"
    class_model_uri: ClassVar[URIRef] = SIO.TerminalPoint


class Endpoint(TerminalPoint):
    """
    An endpoint is a terminal point that is the last of an ordered
    pair of points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Endpoint
    class_class_curie: ClassVar[str] = "sio:Endpoint"
    class_name: ClassVar[str] = "Endpoint"
    class_model_uri: ClassVar[URIRef] = SIO.Endpoint


class StartPoint(TerminalPoint):
    """
    A start point is a terminal point which is the first of an ordered
    pair of points.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StartPoint
    class_class_curie: ClassVar[str] = "sio:StartPoint"
    class_name: ClassVar[str] = "StartPoint"
    class_model_uri: ClassVar[URIRef] = SIO.StartPoint


class Territory(GeopoliticalRegion):
    """
    A territory is a non-sovereign geographic region.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Territory
    class_class_curie: ClassVar[str] = "sio:Territory"
    class_name: ClassVar[str] = "Territory"
    class_model_uri: ClassVar[URIRef] = SIO.Territory


class Terror(Dread):
    """
    terror is the extreme feeling of fear.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Terror
    class_class_curie: ClassVar[str] = "sio:Terror"
    class_name: ClassVar[str] = "Terror"
    class_model_uri: ClassVar[URIRef] = SIO.Terror


class TertiaryStructureDescriptor(BiomolecularStructureDescriptor):
    """
    A tertiary structure descriptor describes 3D topological patterns in a biopolymer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TertiaryStructureDescriptor
    class_class_curie: ClassVar[str] = "sio:TertiaryStructureDescriptor"
    class_name: ClassVar[str] = "TertiaryStructureDescriptor"
    class_model_uri: ClassVar[URIRef] = SIO.TertiaryStructureDescriptor


class 3dStructureModel(TertiaryStructureDescriptor):
    """
    A 3D structure model is a representation of the spatial arrangement of one or more chemical entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["3dStructureModel"]
    class_class_curie: ClassVar[str] = "sio:3dStructureModel"
    class_name: ClassVar[str] = "3dStructureModel"
    class_model_uri: ClassVar[URIRef] = SIO.3dStructureModel


class TestRole(EvaluationRole):
    """
    A test role is the role of an individual that is a participant in the study and is the target of the intervention.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TestRole
    class_class_curie: ClassVar[str] = "sio:TestRole"
    class_name: ClassVar[str] = "TestRole"
    class_model_uri: ClassVar[URIRef] = SIO.TestRole


class TextQuality(ObjectQuality):
    """
    text quality is the quality of a textual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TextQuality
    class_class_curie: ClassVar[str] = "sio:TextQuality"
    class_name: ClassVar[str] = "TextQuality"
    class_model_uri: ClassVar[URIRef] = SIO.TextQuality


class TextSpanEndPosition(EndPosition):
    """
    text span end position is the position (offset) of the last character of a text span in relation the text it is
    from.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TextSpanEndPosition
    class_class_curie: ClassVar[str] = "sio:TextSpanEndPosition"
    class_name: ClassVar[str] = "TextSpanEndPosition"
    class_model_uri: ClassVar[URIRef] = SIO.TextSpanEndPosition


class TextSpanStartPosition(StartPosition):
    """
    text span start position is the position (offset) of the first character of a text span in relation the text it is
    from.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TextSpanStartPosition
    class_class_curie: ClassVar[str] = "sio:TextSpanStartPosition"
    class_name: ClassVar[str] = "TextSpanStartPosition"
    class_model_uri: ClassVar[URIRef] = SIO.TextSpanStartPosition


class TextualChart(Chart):
    """
    A textual chart is a chart containing text.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TextualChart
    class_class_curie: ClassVar[str] = "sio:TextualChart"
    class_name: ClassVar[str] = "TextualChart"
    class_model_uri: ClassVar[URIRef] = SIO.TextualChart


class PhraseNetDiagram(TextualChart):
    """
    A phrase net diagram illustrates the relationship between different words used in a text.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PhraseNetDiagram
    class_class_curie: ClassVar[str] = "sio:PhraseNetDiagram"
    class_name: ClassVar[str] = "PhraseNetDiagram"
    class_model_uri: ClassVar[URIRef] = SIO.PhraseNetDiagram


class TagCloud(TextualChart):
    """
    A tag cloud is a visualization of word frequencies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TagCloud
    class_class_curie: ClassVar[str] = "sio:TagCloud"
    class_name: ClassVar[str] = "TagCloud"
    class_model_uri: ClassVar[URIRef] = SIO.TagCloud


class TextualEntity(LanguageEntity):
    """
    A textual entity is language entity that is manifested as a sequence of one or more distinct characters.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TextualEntity
    class_class_curie: ClassVar[str] = "sio:TextualEntity"
    class_name: ClassVar[str] = "TextualEntity"
    class_model_uri: ClassVar[URIRef] = SIO.TextualEntity


class Document(TextualEntity):
    """
    A document is a bounded physical or digital representation of a body of information designed with the capacity
    (and usually intent) to communicate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Document
    class_class_curie: ClassVar[str] = "sio:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = SIO.Document


class Booklet(Document):
    """
    A booklet is a document that lacks a named publisher or sponsoring institution.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Booklet
    class_class_curie: ClassVar[str] = "sio:Booklet"
    class_name: ClassVar[str] = "Booklet"
    class_model_uri: ClassVar[URIRef] = SIO.Booklet


class Diary(Document):
    """
    A diary is a document which describes day-to-day experiences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Diary
    class_class_curie: ClassVar[str] = "sio:Diary"
    class_name: ClassVar[str] = "Diary"
    class_model_uri: ClassVar[URIRef] = SIO.Diary


class DocumentComponent(TextualEntity):
    """
    A bibliographic attribute is an attribute related to publications.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DocumentComponent
    class_class_curie: ClassVar[str] = "sio:DocumentComponent"
    class_name: ClassVar[str] = "DocumentComponent"
    class_model_uri: ClassVar[URIRef] = SIO.DocumentComponent


class Citation(DocumentComponent):
    """
    A citation is a textual entity which denotes a source described in the bibliography or reference section of a
    document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Citation
    class_class_curie: ClassVar[str] = "sio:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = SIO.Citation


class DocumentSection(DocumentComponent):
    """
    A document section is a component of a document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DocumentSection
    class_class_curie: ClassVar[str] = "sio:DocumentSection"
    class_name: ClassVar[str] = "DocumentSection"
    class_model_uri: ClassVar[URIRef] = SIO.DocumentSection


class AbstractSection(DocumentSection):
    """
    An abstract section is a document section that provides brief summary of a document that explains the main
    argument(s), topic(s) or findings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AbstractSection
    class_class_curie: ClassVar[str] = "sio:AbstractSection"
    class_name: ClassVar[str] = "AbstractSection"
    class_model_uri: ClassVar[URIRef] = SIO.AbstractSection


class AcknowledgementsSection(DocumentSection):
    """
    An acknowledgements section is a document section that identifies individuals, groups or organizations for their
    support in the development of the work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AcknowledgementsSection
    class_class_curie: ClassVar[str] = "sio:AcknowledgementsSection"
    class_name: ClassVar[str] = "AcknowledgementsSection"
    class_model_uri: ClassVar[URIRef] = SIO.AcknowledgementsSection


class AuthorContributionSection(DocumentSection):
    """
    An author contribution section is a document section that describes the contribution of the authors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AuthorContributionSection
    class_class_curie: ClassVar[str] = "sio:AuthorContributionSection"
    class_name: ClassVar[str] = "AuthorContributionSection"
    class_model_uri: ClassVar[URIRef] = SIO.AuthorContributionSection


class AuthorSection(DocumentSection):
    """
    An author section is a document section that lists the contributing authors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AuthorSection
    class_class_curie: ClassVar[str] = "sio:AuthorSection"
    class_name: ClassVar[str] = "AuthorSection"
    class_model_uri: ClassVar[URIRef] = SIO.AuthorSection


class BibliographySection(DocumentSection):
    """
    A bibliography section is a document section that is composed of a list of references used in the development of
    the work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BibliographySection
    class_class_curie: ClassVar[str] = "sio:BibliographySection"
    class_name: ClassVar[str] = "BibliographySection"
    class_model_uri: ClassVar[URIRef] = SIO.BibliographySection


class BookSection(DocumentSection):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BookSection
    class_class_curie: ClassVar[str] = "sio:BookSection"
    class_name: ClassVar[str] = "BookSection"
    class_model_uri: ClassVar[URIRef] = SIO.BookSection


class Chapter(DocumentSection):
    """
    A chapter is a document section of a book or thesis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Chapter
    class_class_curie: ClassVar[str] = "sio:Chapter"
    class_name: ClassVar[str] = "Chapter"
    class_model_uri: ClassVar[URIRef] = SIO.Chapter


class CopyrightSection(DocumentSection):
    """
    A copyright section is a document section that contains a notice of copyright.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CopyrightSection
    class_class_curie: ClassVar[str] = "sio:CopyrightSection"
    class_name: ClassVar[str] = "CopyrightSection"
    class_model_uri: ClassVar[URIRef] = SIO.CopyrightSection


class CorrespondenceSection(DocumentSection):
    """
    A correspondence section is a document section that contains the details for contacting the corresponding author.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CorrespondenceSection
    class_class_curie: ClassVar[str] = "sio:CorrespondenceSection"
    class_name: ClassVar[str] = "CorrespondenceSection"
    class_model_uri: ClassVar[URIRef] = SIO.CorrespondenceSection


class DiscussionSection(DocumentSection):
    """
    The discussion section is a document section containing a summary of the findings, a reflection on the
    significance of findings, comparison with related work, among others.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DiscussionSection
    class_class_curie: ClassVar[str] = "sio:DiscussionSection"
    class_name: ClassVar[str] = "DiscussionSection"
    class_model_uri: ClassVar[URIRef] = SIO.DiscussionSection


class Email(Document):
    """
    Email message is a digital document that is composed of a header and a body and is transmitted using the SMTP
    protocol.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Email
    class_class_curie: ClassVar[str] = "sio:Email"
    class_name: ClassVar[str] = "Email"
    class_model_uri: ClassVar[URIRef] = SIO.Email


class Excerpt(TextualEntity):
    """
    An excerpt is a contiguous or discontiguous portion of a document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Excerpt
    class_class_curie: ClassVar[str] = "sio:Excerpt"
    class_name: ClassVar[str] = "Excerpt"
    class_model_uri: ClassVar[URIRef] = SIO.Excerpt


class IntroductionSection(DocumentSection):
    """
    An introduction section is a document section that generally provides background, motivation and goals of the work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IntroductionSection
    class_class_curie: ClassVar[str] = "sio:IntroductionSection"
    class_name: ClassVar[str] = "IntroductionSection"
    class_model_uri: ClassVar[URIRef] = SIO.IntroductionSection


class LegalDocument(Document):
    """
    A legal document is a formally executed written document that can be formally attributed to its author, records
    and formally expresses a legally enforceable act, process, or contractual duty, obligation, or right, and
    therefore evidences that act, process, or agreement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LegalDocument
    class_class_curie: ClassVar[str] = "sio:LegalDocument"
    class_name: ClassVar[str] = "LegalDocument"
    class_model_uri: ClassVar[URIRef] = SIO.LegalDocument


class Bill(LegalDocument):
    """
    A bill is proposed legislation under consideration by a legislature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Bill
    class_class_curie: ClassVar[str] = "sio:Bill"
    class_name: ClassVar[str] = "Bill"
    class_model_uri: ClassVar[URIRef] = SIO.Bill


class Brief(LegalDocument):
    """
    A brief is a written legal document used in various legal adversarial systems that is presented to a court arguing
    why one party to a particular case should prevail.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Brief
    class_class_curie: ClassVar[str] = "sio:Brief"
    class_name: ClassVar[str] = "Brief"
    class_model_uri: ClassVar[URIRef] = SIO.Brief


class Legislation(LegalDocument):
    """
    A legal document proposing or enacting a law or a group of laws.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Legislation
    class_class_curie: ClassVar[str] = "sio:Legislation"
    class_name: ClassVar[str] = "Legislation"
    class_model_uri: ClassVar[URIRef] = SIO.Legislation


class Letter(Document):
    """
    A letter is a document that contains a personal communication from one part to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Letter
    class_class_curie: ClassVar[str] = "sio:Letter"
    class_name: ClassVar[str] = "Letter"
    class_model_uri: ClassVar[URIRef] = SIO.Letter


class Manuscript(Document):
    """
    A manuscript is a document prior to publication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Manuscript
    class_class_curie: ClassVar[str] = "sio:Manuscript"
    class_name: ClassVar[str] = "Manuscript"
    class_model_uri: ClassVar[URIRef] = SIO.Manuscript


class MaterialsAndMethodsSection(DocumentSection):
    """
    The materials and methods section is a document section containing a description of the materials and methods used
    in the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaterialsAndMethodsSection
    class_class_curie: ClassVar[str] = "sio:MaterialsAndMethodsSection"
    class_name: ClassVar[str] = "MaterialsAndMethodsSection"
    class_model_uri: ClassVar[URIRef] = SIO.MaterialsAndMethodsSection


class MaterialsSection(DocumentSection):
    """
    The materials section is a document section containing a description of the materials used in the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MaterialsSection
    class_class_curie: ClassVar[str] = "sio:MaterialsSection"
    class_name: ClassVar[str] = "MaterialsSection"
    class_model_uri: ClassVar[URIRef] = SIO.MaterialsSection


class MethodsSection(DocumentSection):
    """
    The methods section is a document section containing a description of the methods used in the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MethodsSection
    class_class_curie: ClassVar[str] = "sio:MethodsSection"
    class_name: ClassVar[str] = "MethodsSection"
    class_model_uri: ClassVar[URIRef] = SIO.MethodsSection


class Note(Document):
    """
    A note is a brief document.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Note
    class_class_curie: ClassVar[str] = "sio:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = SIO.Note


class OntologyDocument(Document):
    """
    An ontology document is a document that contains an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OntologyDocument
    class_class_curie: ClassVar[str] = "sio:OntologyDocument"
    class_name: ClassVar[str] = "OntologyDocument"
    class_model_uri: ClassVar[URIRef] = SIO.OntologyDocument


class OBOOntology(OntologyDocument):
    """
    An OBO ontology is an ontology document as specified by the Open Biological Ontology community.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OBOOntology
    class_class_curie: ClassVar[str] = "sio:OBOOntology"
    class_name: ClassVar[str] = "OBOOntology"
    class_model_uri: ClassVar[URIRef] = SIO.OBOOntology


class OWLOntology(OntologyDocument):
    """
    An OWL ontology is an ontology as specified by the W3C OWL specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.OWLOntology
    class_class_curie: ClassVar[str] = "sio:OWLOntology"
    class_name: ClassVar[str] = "OWLOntology"
    class_model_uri: ClassVar[URIRef] = SIO.OWLOntology


class Paragraph(TextualEntity):
    """
    A paragraph is a self-contained unit of written discourse consisting of one or more sentences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Paragraph
    class_class_curie: ClassVar[str] = "sio:Paragraph"
    class_name: ClassVar[str] = "Paragraph"
    class_model_uri: ClassVar[URIRef] = SIO.Paragraph


class Patent(LegalDocument):
    """
    A patent is an information entity granted by a patent issuing authority which confers upon the patenter the sole
    right to make, use and sell an invention for a set period of time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Patent
    class_class_curie: ClassVar[str] = "sio:Patent"
    class_name: ClassVar[str] = "Patent"
    class_model_uri: ClassVar[URIRef] = SIO.Patent


class Publication(Document):
    """
    A publication is a document that has been made available by a publisher.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Publication
    class_class_curie: ClassVar[str] = "sio:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = SIO.Publication


class Article(Publication):
    """
    An article is a publication that is stand-alone section of a larger work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Article
    class_class_curie: ClassVar[str] = "sio:Article"
    class_name: ClassVar[str] = "Article"
    class_model_uri: ClassVar[URIRef] = SIO.Article


class Blog(Publication):
    """
    A blog is a publication accessible at some website and is typically about various experiences.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Blog
    class_class_curie: ClassVar[str] = "sio:Blog"
    class_name: ClassVar[str] = "Blog"
    class_model_uri: ClassVar[URIRef] = SIO.Blog


class Book(Publication):
    """
    A book is a publication composed of a large number of entries.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Book
    class_class_curie: ClassVar[str] = "sio:Book"
    class_name: ClassVar[str] = "Book"
    class_model_uri: ClassVar[URIRef] = SIO.Book


class BookVolume(Book):
    """
    A book volume is a book that is part of a collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BookVolume
    class_class_curie: ClassVar[str] = "sio:BookVolume"
    class_name: ClassVar[str] = "BookVolume"
    class_model_uri: ClassVar[URIRef] = SIO.BookVolume


class ConferenceProceedings(Book):
    """
    A conference proceedings is a book composed of papers presented at a conference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ConferenceProceedings
    class_class_curie: ClassVar[str] = "sio:ConferenceProceedings"
    class_name: ClassVar[str] = "ConferenceProceedings"
    class_model_uri: ClassVar[URIRef] = SIO.ConferenceProceedings


class EditedPublication(Publication):
    """
    An edited publication is a publication that has been examined and potentially changed by an editor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EditedPublication
    class_class_curie: ClassVar[str] = "sio:EditedPublication"
    class_name: ClassVar[str] = "EditedPublication"
    class_model_uri: ClassVar[URIRef] = SIO.EditedPublication


class Issue(EditedPublication):
    """
    An issue is a single instance of a periodically published journal, magazine, or newspaper.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Issue
    class_class_curie: ClassVar[str] = "sio:Issue"
    class_name: ClassVar[str] = "Issue"
    class_model_uri: ClassVar[URIRef] = SIO.Issue


class Manual(Publication):
    """
    A manual is a document that instructs on the usage of a device.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Manual
    class_class_curie: ClassVar[str] = "sio:Manual"
    class_name: ClassVar[str] = "Manual"
    class_model_uri: ClassVar[URIRef] = SIO.Manual


class Novel(Publication):
    """
    A novel is a fictitious prose narrative of book length, typically representing character and action with some
    degree of realism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Novel
    class_class_curie: ClassVar[str] = "sio:Novel"
    class_name: ClassVar[str] = "Novel"
    class_model_uri: ClassVar[URIRef] = SIO.Novel


class PeerReviewedArticle(Article):
    """
    A peer reviewed article is an article that has undergone peer-review and deemed acceptable for publication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PeerReviewedArticle
    class_class_curie: ClassVar[str] = "sio:PeerReviewedArticle"
    class_name: ClassVar[str] = "PeerReviewedArticle"
    class_model_uri: ClassVar[URIRef] = SIO.PeerReviewedArticle


class Quote(Excerpt):
    """
    A quote is a excerpt that is attributed to a particular source.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Quote
    class_class_curie: ClassVar[str] = "sio:Quote"
    class_name: ClassVar[str] = "Quote"
    class_model_uri: ClassVar[URIRef] = SIO.Quote


class RDFSOntology(OntologyDocument):
    """
    An RDFS ontology is an ontology that conforms to the syntax and semantics of the Resource Description Framework
    Schema (RDFS).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RDFSOntology
    class_class_curie: ClassVar[str] = "sio:RDFSOntology"
    class_name: ClassVar[str] = "RDFSOntology"
    class_model_uri: ClassVar[URIRef] = SIO.RDFSOntology


class Record(Document):
    """
    A record is a document containing a collection of statements about some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Record
    class_class_curie: ClassVar[str] = "sio:Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = SIO.Record


class MedicalHealthRecord(Record):
    """
    A medical health record is a record of a single patient's medical history.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalHealthRecord
    class_class_curie: ClassVar[str] = "sio:MedicalHealthRecord"
    class_name: ClassVar[str] = "MedicalHealthRecord"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalHealthRecord


class Reference(DocumentComponent):
    """
    A reference is a textual entity that describes a single source used in the preparation or development of the work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Reference
    class_class_curie: ClassVar[str] = "sio:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = SIO.Reference


class Report(Document):
    """
    A report is a textual document made that present focused, salient content to a specific audience.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Report
    class_class_curie: ClassVar[str] = "sio:Report"
    class_name: ClassVar[str] = "Report"
    class_model_uri: ClassVar[URIRef] = SIO.Report


class MedicalReport(Report):
    """
    A medical report is a report prepared by a health care practioner about test outcomes or health status of an
    individual.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MedicalReport
    class_class_curie: ClassVar[str] = "sio:MedicalReport"
    class_name: ClassVar[str] = "MedicalReport"
    class_model_uri: ClassVar[URIRef] = SIO.MedicalReport


class ResultsSection(DocumentSection):
    """
    The results section is a document section describing the main findings of the study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ResultsSection
    class_class_curie: ClassVar[str] = "sio:ResultsSection"
    class_name: ClassVar[str] = "ResultsSection"
    class_model_uri: ClassVar[URIRef] = SIO.ResultsSection


class Statute(LegalDocument):
    """
    A statute is a formal written enactment of a legislative authority that governs a state, city or country.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Statute
    class_class_curie: ClassVar[str] = "sio:Statute"
    class_name: ClassVar[str] = "Statute"
    class_model_uri: ClassVar[URIRef] = SIO.Statute


class TableOfContents(DocumentSection):
    """
    The table of contents is a document section that lists all sections (and optionally subsections) in a sequential
    order along with their page number.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TableOfContents
    class_class_curie: ClassVar[str] = "sio:TableOfContents"
    class_name: ClassVar[str] = "TableOfContents"
    class_model_uri: ClassVar[URIRef] = SIO.TableOfContents


class TechnicalReport(Publication):
    """
    A technical report is a publication published by a school or other institution, usually numbered within a series.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TechnicalReport
    class_class_curie: ClassVar[str] = "sio:TechnicalReport"
    class_name: ClassVar[str] = "TechnicalReport"
    class_model_uri: ClassVar[URIRef] = SIO.TechnicalReport


class TextSpan(TextualEntity):
    """
    A text span is a subset of contiguous sequence of characters of a textual entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TextSpan
    class_class_curie: ClassVar[str] = "sio:TextSpan"
    class_name: ClassVar[str] = "TextSpan"
    class_model_uri: ClassVar[URIRef] = SIO.TextSpan


class ThalliumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ThalliumAtom
    class_class_curie: ClassVar[str] = "sio:ThalliumAtom"
    class_name: ClassVar[str] = "ThalliumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ThalliumAtom


class TherapeuticGene-diseaseAssociation(Gene-diseaseAssociation):
    """
    A gene disease association in which the gene is a therapeutic marker for the disease.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["TherapeuticGene-diseaseAssociation"]
    class_class_curie: ClassVar[str] = "sio:TherapeuticGene-diseaseAssociation"
    class_name: ClassVar[str] = "TherapeuticGene-diseaseAssociation"
    class_model_uri: ClassVar[URIRef] = SIO.TherapeuticGene-diseaseAssociation


class ThesisDocument(Publication):
    """
    A thesis document is the written research component of a post-secondary institution that contains a statement
    supported by arguments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ThesisDocument
    class_class_curie: ClassVar[str] = "sio:ThesisDocument"
    class_name: ClassVar[str] = "ThesisDocument"
    class_model_uri: ClassVar[URIRef] = SIO.ThesisDocument


class Honor%27sThesis(ThesisDocument):
    """
    An honor's thesis is a thesis prepared as a requirement for an honor's undergraduate degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Honor%27sThesis"]
    class_class_curie: ClassVar[str] = "sio:Honor%27sThesis"
    class_name: ClassVar[str] = "Honor%27sThesis"
    class_model_uri: ClassVar[URIRef] = SIO.Honor%27sThesis


class Master%27sThesis(ThesisDocument):
    """
    A Master's thesis is a thesis prepared as a requirement for a Master's degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Master%27sThesis"]
    class_class_curie: ClassVar[str] = "sio:Master%27sThesis"
    class_name: ClassVar[str] = "Master%27sThesis"
    class_model_uri: ClassVar[URIRef] = SIO.Master%27sThesis


class PhdThesis(ThesisDocument):
    """
    A PhD thesis is a thesis prepared as a requirement for a doctoral degree.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PhdThesis
    class_class_curie: ClassVar[str] = "sio:PhdThesis"
    class_name: ClassVar[str] = "PhdThesis"
    class_model_uri: ClassVar[URIRef] = SIO.PhdThesis


class Thickness(Depth):
    """
    thickness is the shortest dimensional extent of a 3D projection of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Thickness
    class_class_curie: ClassVar[str] = "sio:Thickness"
    class_name: ClassVar[str] = "Thickness"
    class_model_uri: ClassVar[URIRef] = SIO.Thickness


class ThoriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ThoriumAtom
    class_class_curie: ClassVar[str] = "sio:ThoriumAtom"
    class_name: ClassVar[str] = "ThoriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ThoriumAtom


class ThuliumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ThuliumAtom
    class_class_curie: ClassVar[str] = "sio:ThuliumAtom"
    class_name: ClassVar[str] = "ThuliumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ThuliumAtom


class TickMark(LineSegment):
    """
    A tick mark is a line segment that is spatially positioned perpendicular to the axis of a statistical graph and
    indicates the position of a specific numeric value (which may be indicated by an adjacent value label) on a value
    axis, or is one of a pair of tick marks that delineates the boundary of a categorical value (which may be
    indicated by an adjacent category label) on the categorical axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TickMark
    class_class_curie: ClassVar[str] = "sio:TickMark"
    class_name: ClassVar[str] = "TickMark"
    class_model_uri: ClassVar[URIRef] = SIO.TickMark


class MajorTickMark(TickMark):
    """
    A major tick mark is a tick mark that indicates the position of a specific numeric value and is adjacent to its
    value label on the value axis, or is one of a pair of tick marks that delineates the boundary of a categorical
    value indicated by an adjacent category label on the categorical axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MajorTickMark
    class_class_curie: ClassVar[str] = "sio:MajorTickMark"
    class_name: ClassVar[str] = "MajorTickMark"
    class_model_uri: ClassVar[URIRef] = SIO.MajorTickMark


class MinorTickMark(TickMark):
    """
    A minor tick mark is a tick mark that indicates the position of a specific numeric value but has no adjacent value
    label, or is one of a pair of tick marks that delineates the boundary of a categorical value but has no adjacent
    category label on the categorical axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MinorTickMark
    class_class_curie: ClassVar[str] = "sio:MinorTickMark"
    class_name: ClassVar[str] = "MinorTickMark"
    class_model_uri: ClassVar[URIRef] = SIO.MinorTickMark


class TimeMeasurement(DimensionalQuantity):
    """
    time measurement is a measurement value of the duration of some interval of time or a particular instant of time
    (against some frame of reference).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TimeMeasurement
    class_class_curie: ClassVar[str] = "sio:TimeMeasurement"
    class_name: ClassVar[str] = "TimeMeasurement"
    class_model_uri: ClassVar[URIRef] = SIO.TimeMeasurement


@dataclass
class TimeInstant(TimeMeasurement):
    """
    A time instant is a temporal region which occurs instantaneously, e.g. having no duration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TimeInstant
    class_class_curie: ClassVar[str] = "sio:TimeInstant"
    class_name: ClassVar[str] = "TimeInstant"
    class_model_uri: ClassVar[URIRef] = SIO.TimeInstant

    isStartTimeOf: Optional[Union[dict, Entity]] = None
    isTimeBoundaryOf: Optional[Union[dict, Entity]] = None
    isEndTimeOf: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isStartTimeOf is not None and not isinstance(self.isStartTimeOf, Entity):
            self.isStartTimeOf = Entity(**as_dict(self.isStartTimeOf))

        if self.isTimeBoundaryOf is not None and not isinstance(self.isTimeBoundaryOf, Entity):
            self.isTimeBoundaryOf = Entity(**as_dict(self.isTimeBoundaryOf))

        if self.isEndTimeOf is not None and not isinstance(self.isEndTimeOf, Entity):
            self.isEndTimeOf = Entity(**as_dict(self.isEndTimeOf))

        super().__post_init__(**kwargs)


class DateOfDatabaseSubmission(TimeInstant):
    """
    A date of database submission refers to the moment in time in which some information was submitted/received to a
    database system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DateOfDatabaseSubmission
    class_class_curie: ClassVar[str] = "sio:DateOfDatabaseSubmission"
    class_name: ClassVar[str] = "DateOfDatabaseSubmission"
    class_model_uri: ClassVar[URIRef] = SIO.DateOfDatabaseSubmission


class DateOfIssue(TimeInstant):
    """
    the date at which an information content entity was made public.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DateOfIssue
    class_class_curie: ClassVar[str] = "sio:DateOfIssue"
    class_name: ClassVar[str] = "DateOfIssue"
    class_model_uri: ClassVar[URIRef] = SIO.DateOfIssue


class EndDate(TimeInstant):
    """
    An end date is a time instant pertaining to date of the end of a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EndDate
    class_class_curie: ClassVar[str] = "sio:EndDate"
    class_name: ClassVar[str] = "EndDate"
    class_model_uri: ClassVar[URIRef] = SIO.EndDate


class EndTime(TimeInstant):
    """
    An end time is a time instant pertaining to the time at which a process ends.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EndTime
    class_class_curie: ClassVar[str] = "sio:EndTime"
    class_name: ClassVar[str] = "EndTime"
    class_model_uri: ClassVar[URIRef] = SIO.EndTime


class StartDate(TimeInstant):
    """
    A start date is a time instant pertaining to the date of the beginning of a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StartDate
    class_class_curie: ClassVar[str] = "sio:StartDate"
    class_name: ClassVar[str] = "StartDate"
    class_model_uri: ClassVar[URIRef] = SIO.StartDate


class StartTime(TimeInstant):
    """
    A start time is a time instant pertaining to the time at which a process begins.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.StartTime
    class_class_curie: ClassVar[str] = "sio:StartTime"
    class_name: ClassVar[str] = "StartTime"
    class_model_uri: ClassVar[URIRef] = SIO.StartTime


class TimeInterval(TimeMeasurement):
    """
    A time internval is a contiguous temporal region having some duration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TimeInterval
    class_class_curie: ClassVar[str] = "sio:TimeInterval"
    class_name: ClassVar[str] = "TimeInterval"
    class_model_uri: ClassVar[URIRef] = SIO.TimeInterval


class Century(TimeInterval):
    """
    A century is a period of one hundred years.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Century
    class_class_curie: ClassVar[str] = "sio:Century"
    class_name: ClassVar[str] = "Century"
    class_model_uri: ClassVar[URIRef] = SIO.Century


class Day(TimeInterval):
    """
    A day is a period of 24 hours.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Day
    class_class_curie: ClassVar[str] = "sio:Day"
    class_name: ClassVar[str] = "Day"
    class_model_uri: ClassVar[URIRef] = SIO.Day


class Hour(TimeInterval):
    """
    An hour is a period of 60 minutes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hour
    class_class_curie: ClassVar[str] = "sio:Hour"
    class_name: ClassVar[str] = "Hour"
    class_model_uri: ClassVar[URIRef] = SIO.Hour


class Millennium(TimeInterval):
    """
    A millenium is a period of 1000 years
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Millennium
    class_class_curie: ClassVar[str] = "sio:Millennium"
    class_name: ClassVar[str] = "Millennium"
    class_model_uri: ClassVar[URIRef] = SIO.Millennium


class Minute(TimeInterval):
    """
    A minute is a period of 60 seconds.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Minute
    class_class_curie: ClassVar[str] = "sio:Minute"
    class_name: ClassVar[str] = "Minute"
    class_model_uri: ClassVar[URIRef] = SIO.Minute


class Month(TimeInterval):
    """
    A month is a period of time that divides the year.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Month
    class_class_curie: ClassVar[str] = "sio:Month"
    class_name: ClassVar[str] = "Month"
    class_model_uri: ClassVar[URIRef] = SIO.Month


class Second(TimeInterval):
    """
    A second (symbol: s) is the base unit of time in the International System of Units (SI) and is the second division
    of the hour by sixty, the first division by 60 being the minute.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Second
    class_class_curie: ClassVar[str] = "sio:Second"
    class_name: ClassVar[str] = "Second"
    class_model_uri: ClassVar[URIRef] = SIO.Second


class TinAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TinAtom
    class_class_curie: ClassVar[str] = "sio:TinAtom"
    class_name: ClassVar[str] = "TinAtom"
    class_model_uri: ClassVar[URIRef] = SIO.TinAtom


class Tissue(BiologicalEntity):
    """
    A tissue is a mereologically maximal collection of cells that together perform some function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Tissue
    class_class_curie: ClassVar[str] = "sio:Tissue"
    class_name: ClassVar[str] = "Tissue"
    class_model_uri: ClassVar[URIRef] = SIO.Tissue


class TitaniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TitaniumAtom
    class_class_curie: ClassVar[str] = "sio:TitaniumAtom"
    class_name: ClassVar[str] = "TitaniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.TitaniumAtom


class Title(Label):
    """
    A title is a textual entity that summarily describes some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Title
    class_class_curie: ClassVar[str] = "sio:Title"
    class_name: ClassVar[str] = "Title"
    class_model_uri: ClassVar[URIRef] = SIO.Title


class DocumentTitle(Title):
    """
    A document title is a textual entity that summarizes the topic of the document in one sentence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DocumentTitle
    class_class_curie: ClassVar[str] = "sio:DocumentTitle"
    class_name: ClassVar[str] = "DocumentTitle"
    class_model_uri: ClassVar[URIRef] = SIO.DocumentTitle


class GraphTitle(Title):
    """
    A graph title is a title that describes a graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.GraphTitle
    class_class_curie: ClassVar[str] = "sio:GraphTitle"
    class_name: ClassVar[str] = "GraphTitle"
    class_model_uri: ClassVar[URIRef] = SIO.GraphTitle


class PrimaryTitle(Title):
    """
    A primary title is a title that should be first used in describing some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PrimaryTitle
    class_class_curie: ClassVar[str] = "sio:PrimaryTitle"
    class_name: ClassVar[str] = "PrimaryTitle"
    class_model_uri: ClassVar[URIRef] = SIO.PrimaryTitle


class PrimaryGraphTitle(PrimaryTitle):
    """
    A primary graph title is a primary title that describes a statistical graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PrimaryGraphTitle
    class_class_curie: ClassVar[str] = "sio:PrimaryGraphTitle"
    class_name: ClassVar[str] = "PrimaryGraphTitle"
    class_model_uri: ClassVar[URIRef] = SIO.PrimaryGraphTitle


class SecondaryGraphTitle(PrimaryTitle):
    """
    A secondary graph title is a secondary title that describes a statistical graph.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SecondaryGraphTitle
    class_class_curie: ClassVar[str] = "sio:SecondaryGraphTitle"
    class_name: ClassVar[str] = "SecondaryGraphTitle"
    class_model_uri: ClassVar[URIRef] = SIO.SecondaryGraphTitle


class SecondaryTitle(Title):
    """
    A secondary title is a title of lesser importance that should be used after the first title in describing some
    entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SecondaryTitle
    class_class_curie: ClassVar[str] = "sio:SecondaryTitle"
    class_name: ClassVar[str] = "SecondaryTitle"
    class_model_uri: ClassVar[URIRef] = SIO.SecondaryTitle


class ToBeInteractedWith(Capability):
    """
    to be interacted with is the capability of an object to be target of a physical interaction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeInteractedWith
    class_class_curie: ClassVar[str] = "sio:ToBeInteractedWith"
    class_name: ClassVar[str] = "ToBeInteractedWith"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeInteractedWith


class ToBeActivelyInteractedWith(ToBeInteractedWith):
    """
    to be actively interacted with is the capability to be manipulated by some device or agent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeActivelyInteractedWith
    class_class_curie: ClassVar[str] = "sio:ToBeActivelyInteractedWith"
    class_name: ClassVar[str] = "ToBeActivelyInteractedWith"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeActivelyInteractedWith


class ToBeModified(ToBeActivelyInteractedWith):
    """
    to be modified is the capability to be actively interacted with in such a way that it leads to a physical
    reconfiguration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeModified
    class_class_curie: ClassVar[str] = "sio:ToBeModified"
    class_name: ClassVar[str] = "ToBeModified"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeModified


class ToBeCleaved(ToBeModified):
    """
    to be cleaved is the capability to be modified in a way that splits one part of the object from the other.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeCleaved
    class_class_curie: ClassVar[str] = "sio:ToBeCleaved"
    class_name: ClassVar[str] = "ToBeCleaved"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeCleaved


class ToBeCombined(ToBeModified):
    """
    to be combined is the capability to be modified in a way that the object is merged with another object to form a
    new object or substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeCombined
    class_class_curie: ClassVar[str] = "sio:ToBeCombined"
    class_name: ClassVar[str] = "ToBeCombined"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeCombined


class ToBeAPartOf(ToBeCombined):
    """
    to be a part of is the capability to be assembled into a larger structure that persists in time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeAPartOf
    class_class_curie: ClassVar[str] = "sio:ToBeAPartOf"
    class_name: ClassVar[str] = "ToBeAPartOf"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeAPartOf


class ToBeConformationallyChanged(ToBeModified):
    """
    to be conformationally changed is the capability to be modified in such a way that the object's conformation is
    changed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeConformationallyChanged
    class_class_curie: ClassVar[str] = "sio:ToBeConformationallyChanged"
    class_name: ClassVar[str] = "ToBeConformationallyChanged"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeConformationallyChanged


class ToBeActivated(ToBeConformationallyChanged):
    """
    to be activated is the capability to be modified in such a way that the conformational change leads to an increase
    in another capability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeActivated
    class_class_curie: ClassVar[str] = "sio:ToBeActivated"
    class_name: ClassVar[str] = "ToBeActivated"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeActivated


class ToBeCovalentlyModified(ToBeModified):
    """
    to be covalently modified is the capability of a chemical entity to have bonds added or removed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeCovalentlyModified
    class_class_curie: ClassVar[str] = "sio:ToBeCovalentlyModified"
    class_name: ClassVar[str] = "ToBeCovalentlyModified"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeCovalentlyModified


class ToBeElectronicallyModified(ToBeModified):
    """
    to be electronically modified is the capability of a chemical entity to have electrons added or removed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeElectronicallyModified
    class_class_curie: ClassVar[str] = "sio:ToBeElectronicallyModified"
    class_name: ClassVar[str] = "ToBeElectronicallyModified"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeElectronicallyModified


class ToBeInhibited(ToBeConformationallyChanged):
    """
    to be inhibited is the capability to be modified in such a way that the conformational change leads to an decrease
    in another capability.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeInhibited
    class_class_curie: ClassVar[str] = "sio:ToBeInhibited"
    class_name: ClassVar[str] = "ToBeInhibited"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeInhibited


class ToBePassivelyInteractedWith(ToBeInteractedWith):
    """
    to be passively interacted with is the capability of an object to be observed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBePassivelyInteractedWith
    class_class_curie: ClassVar[str] = "sio:ToBePassivelyInteractedWith"
    class_name: ClassVar[str] = "ToBePassivelyInteractedWith"
    class_model_uri: ClassVar[URIRef] = SIO.ToBePassivelyInteractedWith


class ToBeObserved(ToBePassivelyInteractedWith):
    """
    to be observed is the capability of an object to be perceived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeObserved
    class_class_curie: ClassVar[str] = "sio:ToBeObserved"
    class_name: ClassVar[str] = "ToBeObserved"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeObserved


class ToBeExamined(ToBeObserved):
    """
    to be examined is the capability of an object to be observed in a detailed manner.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeExamined
    class_class_curie: ClassVar[str] = "sio:ToBeExamined"
    class_name: ClassVar[str] = "ToBeExamined"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeExamined


class ToBeCompared(ToBeExamined):
    """
    to be compared is the capability of an object to be examined in order to note the similarities or differences
    among a set of objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeCompared
    class_class_curie: ClassVar[str] = "sio:ToBeCompared"
    class_name: ClassVar[str] = "ToBeCompared"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeCompared


class ToBeRecorded(ToBeObserved):
    """
    to be recorded is the capability of an object to be observed in such a way that information about it can be
    transcribed in a specified format on some physical medium.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeRecorded
    class_class_curie: ClassVar[str] = "sio:ToBeRecorded"
    class_name: ClassVar[str] = "ToBeRecorded"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeRecorded


class ToBeTranslocated(ToBeInteractedWith):
    """
    to be translocated is the capability to be physically displaced from one location to another
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeTranslocated
    class_class_curie: ClassVar[str] = "sio:ToBeTranslocated"
    class_name: ClassVar[str] = "ToBeTranslocated"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeTranslocated


class ToBeTransported(ToBeActivelyInteractedWith):
    """
    to be transported is the disposition to undergo motion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeTransported
    class_class_curie: ClassVar[str] = "sio:ToBeTransported"
    class_name: ClassVar[str] = "ToBeTransported"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeTransported


class ToBreathe(Capability):
    """
    to breathe is the capability to inhale and exhale air into the body during respiration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBreathe
    class_class_curie: ClassVar[str] = "sio:ToBreathe"
    class_name: ClassVar[str] = "ToBreathe"
    class_model_uri: ClassVar[URIRef] = SIO.ToBreathe


class ToGainACovalentBond(ToBeCovalentlyModified):
    """
    to gain a covalent bond is the capability of a chemical entity to have bonds added.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToGainACovalentBond
    class_class_curie: ClassVar[str] = "sio:ToGainACovalentBond"
    class_name: ClassVar[str] = "ToGainACovalentBond"
    class_model_uri: ClassVar[URIRef] = SIO.ToGainACovalentBond


class ToGainAnElectron(ToBeElectronicallyModified):
    """
    to gain an electron is the capability of a chemical entity to receive an electron.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToGainAnElectron
    class_class_curie: ClassVar[str] = "sio:ToGainAnElectron"
    class_name: ClassVar[str] = "ToGainAnElectron"
    class_model_uri: ClassVar[URIRef] = SIO.ToGainAnElectron


class ToInteractAndToBeInteractedWith(MutualDisposition):
    """
    to interact and to be interacted with is a mutual disposition of interacting objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToInteractAndToBeInteractedWith
    class_class_curie: ClassVar[str] = "sio:ToInteractAndToBeInteractedWith"
    class_name: ClassVar[str] = "ToInteractAndToBeInteractedWith"
    class_model_uri: ClassVar[URIRef] = SIO.ToInteractAndToBeInteractedWith


class ToInteractWith(Capability):
    """
    to interact with is a capabililty that involves another object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToInteractWith
    class_class_curie: ClassVar[str] = "sio:ToInteractWith"
    class_name: ClassVar[str] = "ToInteractWith"
    class_model_uri: ClassVar[URIRef] = SIO.ToInteractWith


class ToActivelyInteractWith(ToInteractWith):
    """
    to actively interact with is the capability to interact with another entity in a way that requires physical
    contact.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToActivelyInteractWith
    class_class_curie: ClassVar[str] = "sio:ToActivelyInteractWith"
    class_name: ClassVar[str] = "ToActivelyInteractWith"
    class_model_uri: ClassVar[URIRef] = SIO.ToActivelyInteractWith


class ToAssemble(ToActivelyInteractWith):
    """
    to assemble is the capability to combine entities together into a larger object that persists in time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToAssemble
    class_class_curie: ClassVar[str] = "sio:ToAssemble"
    class_name: ClassVar[str] = "ToAssemble"
    class_model_uri: ClassVar[URIRef] = SIO.ToAssemble


class ToAssociate(ToActivelyInteractWith):
    """
    to associate is the capability to physically interact with another object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToAssociate
    class_class_curie: ClassVar[str] = "sio:ToAssociate"
    class_name: ClassVar[str] = "ToAssociate"
    class_model_uri: ClassVar[URIRef] = SIO.ToAssociate


class ToBindTo(ToAssociate):
    """
    to bind to is the capability to physically interact with another object through a set of non-covalent interactions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBindTo
    class_class_curie: ClassVar[str] = "sio:ToBindTo"
    class_name: ClassVar[str] = "ToBindTo"
    class_model_uri: ClassVar[URIRef] = SIO.ToBindTo


class ToConsume(ToActivelyInteractWith):
    """
    to consume is the capability to internalize a material entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToConsume
    class_class_curie: ClassVar[str] = "sio:ToConsume"
    class_name: ClassVar[str] = "ToConsume"
    class_model_uri: ClassVar[URIRef] = SIO.ToConsume


class ToDecodeInformation(ToActivelyInteractWith):
    """
    the ability to reverse an encoding operation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToDecodeInformation
    class_class_curie: ClassVar[str] = "sio:ToDecodeInformation"
    class_name: ClassVar[str] = "ToDecodeInformation"
    class_model_uri: ClassVar[URIRef] = SIO.ToDecodeInformation


class ToEncodeInformation(ToActivelyInteractWith):
    """
    the capability to encode information in a different representation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToEncodeInformation
    class_class_curie: ClassVar[str] = "sio:ToEncodeInformation"
    class_name: ClassVar[str] = "ToEncodeInformation"
    class_model_uri: ClassVar[URIRef] = SIO.ToEncodeInformation


class ToIngest(ToConsume):
    """
    to ingest is the capability to take into the body by the mouth for digestion or absorption.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToIngest
    class_class_curie: ClassVar[str] = "sio:ToIngest"
    class_name: ClassVar[str] = "ToIngest"
    class_model_uri: ClassVar[URIRef] = SIO.ToIngest


class ToInvestigate(ToActivelyInteractWith):
    """
    to investigate is the capability to uncover facts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToInvestigate
    class_class_curie: ClassVar[str] = "sio:ToInvestigate"
    class_name: ClassVar[str] = "ToInvestigate"
    class_model_uri: ClassVar[URIRef] = SIO.ToInvestigate


class ToIdentify(ToInvestigate):
    """
    to identify is the capability to determine the identity of something.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToIdentify
    class_class_curie: ClassVar[str] = "sio:ToIdentify"
    class_name: ClassVar[str] = "ToIdentify"
    class_model_uri: ClassVar[URIRef] = SIO.ToIdentify


class ToLoseACovalentBond(ToBeCovalentlyModified):
    """
    to lose a covalent bond is the capability of a chemical entity to have bonds removed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToLoseACovalentBond
    class_class_curie: ClassVar[str] = "sio:ToLoseACovalentBond"
    class_name: ClassVar[str] = "ToLoseACovalentBond"
    class_model_uri: ClassVar[URIRef] = SIO.ToLoseACovalentBond


class ToLoseAnElectron(ToBeElectronicallyModified):
    """
    to lose an electron is the capability of a chemical entity to lose an electron.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToLoseAnElectron
    class_class_curie: ClassVar[str] = "sio:ToLoseAnElectron"
    class_name: ClassVar[str] = "ToLoseAnElectron"
    class_model_uri: ClassVar[URIRef] = SIO.ToLoseAnElectron


class ToLuminesce(ToBeActivelyInteractedWith):
    """
    to luminesce is to emit light through cold body radiation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToLuminesce
    class_class_curie: ClassVar[str] = "sio:ToLuminesce"
    class_name: ClassVar[str] = "ToLuminesce"
    class_model_uri: ClassVar[URIRef] = SIO.ToLuminesce


class ToFluoresce(ToLuminesce):
    """
    to fluoresce is to emit light as a result of absorbing light or other electromagnetic radiation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToFluoresce
    class_class_curie: ClassVar[str] = "sio:ToFluoresce"
    class_name: ClassVar[str] = "ToFluoresce"
    class_model_uri: ClassVar[URIRef] = SIO.ToFluoresce


class ToMaintainInformation(ToActivelyInteractWith):
    """
    the capability to maintain information such that it can be retrieved in the future.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToMaintainInformation
    class_class_curie: ClassVar[str] = "sio:ToMaintainInformation"
    class_name: ClassVar[str] = "ToMaintainInformation"
    class_model_uri: ClassVar[URIRef] = SIO.ToMaintainInformation


class ToMeasure(ToInvestigate):
    """
    to measure is the capability to obtain information about some entity by examining its attributes in relation to
    some reference metric.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToMeasure
    class_class_curie: ClassVar[str] = "sio:ToMeasure"
    class_name: ClassVar[str] = "ToMeasure"
    class_model_uri: ClassVar[URIRef] = SIO.ToMeasure


class ToModify(ToActivelyInteractWith):
    """
    to modify is the capability to change some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToModify
    class_class_curie: ClassVar[str] = "sio:ToModify"
    class_name: ClassVar[str] = "ToModify"
    class_model_uri: ClassVar[URIRef] = SIO.ToModify


class ToChangeAppearance(ToModify):
    """
    to change appearance is the capability to change the visual attributes of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToChangeAppearance
    class_class_curie: ClassVar[str] = "sio:ToChangeAppearance"
    class_name: ClassVar[str] = "ToChangeAppearance"
    class_model_uri: ClassVar[URIRef] = SIO.ToChangeAppearance


class ToChangeEnergetically(ToModify):
    """
    to change energetically is the capability to change the energetic aspects of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToChangeEnergetically
    class_class_curie: ClassVar[str] = "sio:ToChangeEnergetically"
    class_name: ClassVar[str] = "ToChangeEnergetically"
    class_model_uri: ClassVar[URIRef] = SIO.ToChangeEnergetically


class ToChangeMaterially(ToModify):
    """
    to change appearance is the capability to change the material composition of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToChangeMaterially
    class_class_curie: ClassVar[str] = "sio:ToChangeMaterially"
    class_name: ClassVar[str] = "ToChangeMaterially"
    class_model_uri: ClassVar[URIRef] = SIO.ToChangeMaterially


class ToCauseDisease(ToChangeMaterially):
    """
    to cause disease is the capability to materially change a biological object in that it functions abnormally.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToCauseDisease
    class_class_curie: ClassVar[str] = "sio:ToCauseDisease"
    class_name: ClassVar[str] = "ToCauseDisease"
    class_model_uri: ClassVar[URIRef] = SIO.ToCauseDisease


class ToChangeSpatially(ToModify):
    """
    to change spatially is the capability to affect the physical movement of some entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToChangeSpatially
    class_class_curie: ClassVar[str] = "sio:ToChangeSpatially"
    class_name: ClassVar[str] = "ToChangeSpatially"
    class_model_uri: ClassVar[URIRef] = SIO.ToChangeSpatially


class ToChangeTheActivationEnergy(ToChangeEnergetically):
    """
    to change the activation energy is to change the amount of energy required to form or break a chemical bond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToChangeTheActivationEnergy
    class_class_curie: ClassVar[str] = "sio:ToChangeTheActivationEnergy"
    class_name: ClassVar[str] = "ToChangeTheActivationEnergy"
    class_model_uri: ClassVar[URIRef] = SIO.ToChangeTheActivationEnergy


class ToCombine(ToChangeMaterially):
    """
    to combine is the capability to modify a set of objects in a way that the object is merged with another object to
    form a new object or substance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToCombine
    class_class_curie: ClassVar[str] = "sio:ToCombine"
    class_name: ClassVar[str] = "ToCombine"
    class_model_uri: ClassVar[URIRef] = SIO.ToCombine


class ToContain(ToChangeSpatially):
    """
    to contain is the capability to bound or constrain a physical entity in some site.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToContain
    class_class_curie: ClassVar[str] = "sio:ToContain"
    class_name: ClassVar[str] = "ToContain"
    class_model_uri: ClassVar[URIRef] = SIO.ToContain


class ToCovalentlyModify(ToChangeMaterially):
    """
    to covalently modify is to materially change a molecule by adding or removing covalent bonds between atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToCovalentlyModify
    class_class_curie: ClassVar[str] = "sio:ToCovalentlyModify"
    class_name: ClassVar[str] = "ToCovalentlyModify"
    class_model_uri: ClassVar[URIRef] = SIO.ToCovalentlyModify


class ToAddACovalentBond(ToCovalentlyModify):
    """
    to add a covalent bond is the capability to covalently modify a chemical entity by adding a covalent bond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToAddACovalentBond
    class_class_curie: ClassVar[str] = "sio:ToAddACovalentBond"
    class_name: ClassVar[str] = "ToAddACovalentBond"
    class_model_uri: ClassVar[URIRef] = SIO.ToAddACovalentBond


class ToDemagnify(ToChangeAppearance):
    """
    to demagnify is the capability to decrease the appearance of the size of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToDemagnify
    class_class_curie: ClassVar[str] = "sio:ToDemagnify"
    class_name: ClassVar[str] = "ToDemagnify"
    class_model_uri: ClassVar[URIRef] = SIO.ToDemagnify


class ToDisassemble(ToChangeMaterially):
    """
    to disassemble is to physically separate the parts of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToDisassemble
    class_class_curie: ClassVar[str] = "sio:ToDisassemble"
    class_name: ClassVar[str] = "ToDisassemble"
    class_model_uri: ClassVar[URIRef] = SIO.ToDisassemble


class ToCleave(ToDisassemble):
    """
    to cleave is to split or sever an object along a natural line or grain.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToCleave
    class_class_curie: ClassVar[str] = "sio:ToCleave"
    class_name: ClassVar[str] = "ToCleave"
    class_model_uri: ClassVar[URIRef] = SIO.ToCleave


class ToDisassociate(ToModify):
    """
    to disassociate is to cease or break association with some thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToDisassociate
    class_class_curie: ClassVar[str] = "sio:ToDisassociate"
    class_name: ClassVar[str] = "ToDisassociate"
    class_model_uri: ClassVar[URIRef] = SIO.ToDisassociate


class ToDistort(ToChangeAppearance):
    """
    to distort is the capability to change the appearance of an entity by some transformation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToDistort
    class_class_curie: ClassVar[str] = "sio:ToDistort"
    class_name: ClassVar[str] = "ToDistort"
    class_model_uri: ClassVar[URIRef] = SIO.ToDistort


class ToImmobilize(ToContain):
    """
    to immobilize is the capability to contain an entity in such a way that it may not move in space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToImmobilize
    class_class_curie: ClassVar[str] = "sio:ToImmobilize"
    class_name: ClassVar[str] = "ToImmobilize"
    class_model_uri: ClassVar[URIRef] = SIO.ToImmobilize


class ToIncreaseTheActivationEnergy(ToChangeTheActivationEnergy):
    """
    to increase the activation energy is to require a larger amount of energy in order to form or break a chemical
    bond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToIncreaseTheActivationEnergy
    class_class_curie: ClassVar[str] = "sio:ToIncreaseTheActivationEnergy"
    class_name: ClassVar[str] = "ToIncreaseTheActivationEnergy"
    class_model_uri: ClassVar[URIRef] = SIO.ToIncreaseTheActivationEnergy


class ToInject(ToModify):
    """
    to inject is the capability to administer a substance into some object through its external barrier.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToInject
    class_class_curie: ClassVar[str] = "sio:ToInject"
    class_name: ClassVar[str] = "ToInject"
    class_model_uri: ClassVar[URIRef] = SIO.ToInject


class ToInfect(ToInject):
    """
    to infect is the capability to administer a disease-causing organism into some object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToInfect
    class_class_curie: ClassVar[str] = "sio:ToInfect"
    class_name: ClassVar[str] = "ToInfect"
    class_model_uri: ClassVar[URIRef] = SIO.ToInfect


class ToMagnify(ToChangeAppearance):
    """
    to magnify is the capability to increase the appearance of the size of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToMagnify
    class_class_curie: ClassVar[str] = "sio:ToMagnify"
    class_name: ClassVar[str] = "ToMagnify"
    class_model_uri: ClassVar[URIRef] = SIO.ToMagnify


class ToModifyConformationOf(ToModify):
    """
    to modify conformation of is to affect the spatial arrangement of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToModifyConformationOf
    class_class_curie: ClassVar[str] = "sio:ToModifyConformationOf"
    class_name: ClassVar[str] = "ToModifyConformationOf"
    class_model_uri: ClassVar[URIRef] = SIO.ToModifyConformationOf


class ToConformationallyActivate(ToModifyConformationOf):
    """
    to conformationally activate is to modify the conformation of an entity in such a way that it becomes activated or
    functional.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToConformationallyActivate
    class_class_curie: ClassVar[str] = "sio:ToConformationallyActivate"
    class_name: ClassVar[str] = "ToConformationallyActivate"
    class_model_uri: ClassVar[URIRef] = SIO.ToConformationallyActivate


class ToConformationallyInhibit(ToModifyConformationOf):
    """
    to conformationally inhibit is to modify the conformation of an entity in such a way that it functionally is
    reduced or inhibited.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToConformationallyInhibit
    class_class_curie: ClassVar[str] = "sio:ToConformationallyInhibit"
    class_name: ClassVar[str] = "ToConformationallyInhibit"
    class_model_uri: ClassVar[URIRef] = SIO.ToConformationallyInhibit


class ToModifyElectronically(ToChangeEnergetically):
    """
    to modify electronically is the capability to change the electronic properties of an object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToModifyElectronically
    class_class_curie: ClassVar[str] = "sio:ToModifyElectronically"
    class_name: ClassVar[str] = "ToModifyElectronically"
    class_model_uri: ClassVar[URIRef] = SIO.ToModifyElectronically


class ToIonize(ToModifyElectronically):
    """
    to ionize is the capability to physically convert an atom or molecule into an ion by adding or removing charged
    particles such as electrons or other ions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToIonize
    class_class_curie: ClassVar[str] = "sio:ToIonize"
    class_name: ClassVar[str] = "ToIonize"
    class_model_uri: ClassVar[URIRef] = SIO.ToIonize


class ToModifyOxidationStateOf(ToModifyElectronically):
    """
    to modify the oxidation state of is to change the number of electrons of a molecule, atom or ion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToModifyOxidationStateOf
    class_class_curie: ClassVar[str] = "sio:ToModifyOxidationStateOf"
    class_name: ClassVar[str] = "ToModifyOxidationStateOf"
    class_model_uri: ClassVar[URIRef] = SIO.ToModifyOxidationStateOf


class ToNegativelyCharge(ToIonize):
    """
    to negatively charge is the capability to add an electron or negatively charged ion to a chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToNegativelyCharge
    class_class_curie: ClassVar[str] = "sio:ToNegativelyCharge"
    class_name: ClassVar[str] = "ToNegativelyCharge"
    class_model_uri: ClassVar[URIRef] = SIO.ToNegativelyCharge


class ToOxidize(ToModifyOxidationStateOf):
    """
    to oxidize is the capability to remove an electron or an increase in oxidation state of a chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToOxidize
    class_class_curie: ClassVar[str] = "sio:ToOxidize"
    class_name: ClassVar[str] = "ToOxidize"
    class_model_uri: ClassVar[URIRef] = SIO.ToOxidize


class ToPassivelyInteractWith(ToInteractWith):
    """
    to passively interact with is the capability to interact with another entity in a way that does not require
    physical contact.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToPassivelyInteractWith
    class_class_curie: ClassVar[str] = "sio:ToPassivelyInteractWith"
    class_name: ClassVar[str] = "ToPassivelyInteractWith"
    class_model_uri: ClassVar[URIRef] = SIO.ToPassivelyInteractWith


class ToBeAMemberOf(ToPassivelyInteractWith):
    """
    to be a member of is the capability to be considered a part of a collection.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBeAMemberOf
    class_class_curie: ClassVar[str] = "sio:ToBeAMemberOf"
    class_name: ClassVar[str] = "ToBeAMemberOf"
    class_model_uri: ClassVar[URIRef] = SIO.ToBeAMemberOf


class ToDescribe(ToPassivelyInteractWith):
    """
    to describe is the capabilty to communicate facts about an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToDescribe
    class_class_curie: ClassVar[str] = "sio:ToDescribe"
    class_name: ClassVar[str] = "ToDescribe"
    class_model_uri: ClassVar[URIRef] = SIO.ToDescribe


class ToCharacterize(ToDescribe):
    """
    to characterize is the capability to classify the attributes or features of an entity against a reference
    classification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToCharacterize
    class_class_curie: ClassVar[str] = "sio:ToCharacterize"
    class_name: ClassVar[str] = "ToCharacterize"
    class_model_uri: ClassVar[URIRef] = SIO.ToCharacterize


class ToObserve(ToPassivelyInteractWith):
    """
    to observe is the capability to watch attentively.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToObserve
    class_class_curie: ClassVar[str] = "sio:ToObserve"
    class_name: ClassVar[str] = "ToObserve"
    class_model_uri: ClassVar[URIRef] = SIO.ToObserve


class ToExamine(ToObserve):
    """
    to examine is the capability to make detailed observation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToExamine
    class_class_curie: ClassVar[str] = "sio:ToExamine"
    class_name: ClassVar[str] = "ToExamine"
    class_model_uri: ClassVar[URIRef] = SIO.ToExamine


class ToCompare(ToExamine):
    """
    to compare is the capability to examine in order to note the similarities or differences among a set of objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToCompare
    class_class_curie: ClassVar[str] = "sio:ToCompare"
    class_name: ClassVar[str] = "ToCompare"
    class_model_uri: ClassVar[URIRef] = SIO.ToCompare


class ToPositivelyCharge(ToIonize):
    """
    to positively charge is the capability to remove an electron or add a  positively charged ion to a chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToPositivelyCharge
    class_class_curie: ClassVar[str] = "sio:ToPositivelyCharge"
    class_name: ClassVar[str] = "ToPositivelyCharge"
    class_model_uri: ClassVar[URIRef] = SIO.ToPositivelyCharge


class ToProduce(ToActivelyInteractWith):
    """
    to produce is the capability to create new objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToProduce
    class_class_curie: ClassVar[str] = "sio:ToProduce"
    class_name: ClassVar[str] = "ToProduce"
    class_model_uri: ClassVar[URIRef] = SIO.ToProduce


class ToRecord(ToActivelyInteractWith):
    """
    to record is the capability to detect and transcribe information in a specified format on some physical medium.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToRecord
    class_class_curie: ClassVar[str] = "sio:ToRecord"
    class_name: ClassVar[str] = "ToRecord"
    class_model_uri: ClassVar[URIRef] = SIO.ToRecord


class ToReduce(ToModifyOxidationStateOf):
    """
    to reduce is the capability to add an electron or an decrease in oxidation state of a chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToReduce
    class_class_curie: ClassVar[str] = "sio:ToReduce"
    class_name: ClassVar[str] = "ToReduce"
    class_model_uri: ClassVar[URIRef] = SIO.ToReduce


class ToReduceEnergy(ToChangeEnergetically):
    """
    to reduce energy is the capability to remove energy from a source.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToReduceEnergy
    class_class_curie: ClassVar[str] = "sio:ToReduceEnergy"
    class_name: ClassVar[str] = "ToReduceEnergy"
    class_model_uri: ClassVar[URIRef] = SIO.ToReduceEnergy


class ToCool(ToReduceEnergy):
    """
    to cool is the capability to decrease the internal kinetic energy of a material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToCool
    class_class_curie: ClassVar[str] = "sio:ToCool"
    class_name: ClassVar[str] = "ToCool"
    class_model_uri: ClassVar[URIRef] = SIO.ToCool


class ToEmit(ToReduceEnergy):
    """
    to emit is the capability to release some physical entity (light, pollution, etc).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToEmit
    class_class_curie: ClassVar[str] = "sio:ToEmit"
    class_name: ClassVar[str] = "ToEmit"
    class_model_uri: ClassVar[URIRef] = SIO.ToEmit


class ToFreeze(ToCool):
    """
    to freeze is the capability to decrease the internal kinetic energy of a material such that it changes state from
    a gas or liquid to a solid.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToFreeze
    class_class_curie: ClassVar[str] = "sio:ToFreeze"
    class_name: ClassVar[str] = "ToFreeze"
    class_model_uri: ClassVar[URIRef] = SIO.ToFreeze


class ToReduceTheActivationEnergy(ToChangeTheActivationEnergy):
    """
    to reduce the activation energy is to require a smaller amount of energy in order to form or break a chemical bond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToReduceTheActivationEnergy
    class_class_curie: ClassVar[str] = "sio:ToReduceTheActivationEnergy"
    class_name: ClassVar[str] = "ToReduceTheActivationEnergy"
    class_model_uri: ClassVar[URIRef] = SIO.ToReduceTheActivationEnergy


class ToRegulate(ToModify):
    """
    to regulate is to control or maintain the rate or speed of an object or process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToRegulate
    class_class_curie: ClassVar[str] = "sio:ToRegulate"
    class_name: ClassVar[str] = "ToRegulate"
    class_model_uri: ClassVar[URIRef] = SIO.ToRegulate


class ToRegulateTheRateOfFormation(ToRegulate):
    """
    to regulate the rate of formation is to modify the rate at which an object is formed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToRegulateTheRateOfFormation
    class_class_curie: ClassVar[str] = "sio:ToRegulateTheRateOfFormation"
    class_name: ClassVar[str] = "ToRegulateTheRateOfFormation"
    class_model_uri: ClassVar[URIRef] = SIO.ToRegulateTheRateOfFormation


class ToDecreaseTheRateOfFormation(ToRegulateTheRateOfFormation):
    """
    to decrease the rate of formation is to regulate the rate of formation in a manner that decreases this rate
    relative to a reference process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToDecreaseTheRateOfFormation
    class_class_curie: ClassVar[str] = "sio:ToDecreaseTheRateOfFormation"
    class_name: ClassVar[str] = "ToDecreaseTheRateOfFormation"
    class_model_uri: ClassVar[URIRef] = SIO.ToDecreaseTheRateOfFormation


class ToIncreaseTheRateOfFormation(ToRegulateTheRateOfFormation):
    """
    to increase the rate of formation is to regulate the rate of formation in a manner that increases this rate
    relative to a reference process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToIncreaseTheRateOfFormation
    class_class_curie: ClassVar[str] = "sio:ToIncreaseTheRateOfFormation"
    class_name: ClassVar[str] = "ToIncreaseTheRateOfFormation"
    class_model_uri: ClassVar[URIRef] = SIO.ToIncreaseTheRateOfFormation


class ToRemoveACovalentBond(ToCovalentlyModify):
    """
    to remove a covalent bond is the capability to covalently modify a chemical entity by removing a covalent bond.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToRemoveACovalentBond
    class_class_curie: ClassVar[str] = "sio:ToRemoveACovalentBond"
    class_name: ClassVar[str] = "ToRemoveACovalentBond"
    class_model_uri: ClassVar[URIRef] = SIO.ToRemoveACovalentBond


class ToRetrieve(ToActivelyInteractWith):
    """
    the capability to retrieve a (digitial/physical/mental) object from a location.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToRetrieve
    class_class_curie: ClassVar[str] = "sio:ToRetrieve"
    class_name: ClassVar[str] = "ToRetrieve"
    class_model_uri: ClassVar[URIRef] = SIO.ToRetrieve


class ToProvide(ToRetrieve):
    """
    to provide is the capability to make available some object to another that requires it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToProvide
    class_class_curie: ClassVar[str] = "sio:ToProvide"
    class_name: ClassVar[str] = "ToProvide"
    class_model_uri: ClassVar[URIRef] = SIO.ToProvide


class ToSeparate(ToModify):
    """
    to separate is the capability to i) distinguish some entities based on some attribute(s) and ii) subsequently
    physically displace them.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToSeparate
    class_class_curie: ClassVar[str] = "sio:ToSeparate"
    class_name: ClassVar[str] = "ToSeparate"
    class_model_uri: ClassVar[URIRef] = SIO.ToSeparate


class ToExtract(ToSeparate):
    """
    to extract is the capability to remove certain entities based on selected attribute(s) while allowing other
    entities to remain.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToExtract
    class_class_curie: ClassVar[str] = "sio:ToExtract"
    class_name: ClassVar[str] = "ToExtract"
    class_model_uri: ClassVar[URIRef] = SIO.ToExtract


class ToFilter(ToSeparate):
    """
    to filter is the capability to retain certain entities based on selected attribute(s) while allowing other
    entities to pass through.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToFilter
    class_class_curie: ClassVar[str] = "sio:ToFilter"
    class_name: ClassVar[str] = "ToFilter"
    class_model_uri: ClassVar[URIRef] = SIO.ToFilter


class ToServeAs(ToActivelyInteractWith):
    """
    to serve as is the capability to act in a manner corresponding to some role.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToServeAs
    class_class_curie: ClassVar[str] = "sio:ToServeAs"
    class_name: ClassVar[str] = "ToServeAs"
    class_model_uri: ClassVar[URIRef] = SIO.ToServeAs


class ToServeAsAHost(ToServeAs):
    """
    to serve as host is the capability to act in a manner that provides hospitality, serves to harbour an organism in
    or on itself.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToServeAsAHost
    class_class_curie: ClassVar[str] = "sio:ToServeAsAHost"
    class_name: ClassVar[str] = "ToServeAsAHost"
    class_model_uri: ClassVar[URIRef] = SIO.ToServeAsAHost


class ToServeAsAPrimerForDNASynthesis(ToServeAs):
    """
    to serve as a primer for DNA synthesis is the capability of a short nucleic acid to bind to the 5' end of single
    strand of DNA template and help initiate DNA replication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToServeAsAPrimerForDNASynthesis
    class_class_curie: ClassVar[str] = "sio:ToServeAsAPrimerForDNASynthesis"
    class_name: ClassVar[str] = "ToServeAsAPrimerForDNASynthesis"
    class_model_uri: ClassVar[URIRef] = SIO.ToServeAsAPrimerForDNASynthesis


class ToServeAsATemplateForMolecularSynthesis(ToServeAs):
    """
    to serve as a template for molecular synthesis is the capability of a chemical entity to provide the necessary
    information or scaffold by which another molecule may be produced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForMolecularSynthesis
    class_class_curie: ClassVar[str] = "sio:ToServeAsATemplateForMolecularSynthesis"
    class_name: ClassVar[str] = "ToServeAsATemplateForMolecularSynthesis"
    class_model_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForMolecularSynthesis


class ToServeAsATemplateForDNASynthesis(ToServeAsATemplateForMolecularSynthesis):
    """
    to serve as a template for DNA synthesis is the capability of a chemical entity to provide the necessary
    information or scaffold by which a DNA molecule may be produced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForDNASynthesis
    class_class_curie: ClassVar[str] = "sio:ToServeAsATemplateForDNASynthesis"
    class_name: ClassVar[str] = "ToServeAsATemplateForDNASynthesis"
    class_model_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForDNASynthesis


class ToServeAsATemplateForProteinSynthesis(ToServeAsATemplateForMolecularSynthesis):
    """
    to serve as a template for protein synthesis is the capability of a chemical entity to provide the necessary
    information or scaffold by which a protein may be produced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForProteinSynthesis
    class_class_curie: ClassVar[str] = "sio:ToServeAsATemplateForProteinSynthesis"
    class_name: ClassVar[str] = "ToServeAsATemplateForProteinSynthesis"
    class_model_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForProteinSynthesis


class ToServeAsATemplateForRNASynthesis(ToServeAsATemplateForMolecularSynthesis):
    """
    to serve as a template for RNA synthesis is the capability of a chemical entity to provide the necessary
    information or scaffold by which an RNA molecule may be produced.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForRNASynthesis
    class_class_curie: ClassVar[str] = "sio:ToServeAsATemplateForRNASynthesis"
    class_name: ClassVar[str] = "ToServeAsATemplateForRNASynthesis"
    class_model_uri: ClassVar[URIRef] = SIO.ToServeAsATemplateForRNASynthesis


class ToStore(ToActivelyInteractWith):
    """
    to store is the capability to place an object into a medium in which it can be retrieved in the future.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToStore
    class_class_curie: ClassVar[str] = "sio:ToStore"
    class_name: ClassVar[str] = "ToStore"
    class_model_uri: ClassVar[URIRef] = SIO.ToStore


class ToSupplyEnergy(ToChangeEnergetically):
    """
    to supply energy is the capability to transfer energy from a source to a sink.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToSupplyEnergy
    class_class_curie: ClassVar[str] = "sio:ToSupplyEnergy"
    class_name: ClassVar[str] = "ToSupplyEnergy"
    class_model_uri: ClassVar[URIRef] = SIO.ToSupplyEnergy


class ToExcite(ToSupplyEnergy):
    """
    to excite is the capability to supply energy to a materila by bombarding it with energetic particles (e.g.,
    photons).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToExcite
    class_class_curie: ClassVar[str] = "sio:ToExcite"
    class_name: ClassVar[str] = "ToExcite"
    class_model_uri: ClassVar[URIRef] = SIO.ToExcite


class ToHeat(ToSupplyEnergy):
    """
    to heat is a capability to increase the internal kinetic energy of a material.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToHeat
    class_class_curie: ClassVar[str] = "sio:ToHeat"
    class_name: ClassVar[str] = "ToHeat"
    class_model_uri: ClassVar[URIRef] = SIO.ToHeat


class ToBoil(ToHeat):
    """
    to boil is the capability to increase the internal kinetic energy of a material such that it changes state from a
    solid or liquid to a gas.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToBoil
    class_class_curie: ClassVar[str] = "sio:ToBoil"
    class_name: ClassVar[str] = "ToBoil"
    class_model_uri: ClassVar[URIRef] = SIO.ToBoil


class ToSupplyElectricity(ToSupplyEnergy):
    """
    to supply electricity is the capability to transfer electricity from a source to a sink.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToSupplyElectricity
    class_class_curie: ClassVar[str] = "sio:ToSupplyElectricity"
    class_name: ClassVar[str] = "ToSupplyElectricity"
    class_model_uri: ClassVar[URIRef] = SIO.ToSupplyElectricity


class ToTestAHypothesis(ToExamine):
    """
    to test a hypothesis is the capability to evaluate the truth value of a proposition based on gathered evidence.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToTestAHypothesis
    class_class_curie: ClassVar[str] = "sio:ToTestAHypothesis"
    class_name: ClassVar[str] = "ToTestAHypothesis"
    class_model_uri: ClassVar[URIRef] = SIO.ToTestAHypothesis


class ToTranslocate(ToInteractWith):
    """
    to translocate is the capability to displace oneself from one location to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToTranslocate
    class_class_curie: ClassVar[str] = "sio:ToTranslocate"
    class_name: ClassVar[str] = "ToTranslocate"
    class_model_uri: ClassVar[URIRef] = SIO.ToTranslocate


class ToTransport(ToActivelyInteractWith):
    """
    to transport is the capability to displace a material from one location to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToTransport
    class_class_curie: ClassVar[str] = "sio:ToTransport"
    class_name: ClassVar[str] = "ToTransport"
    class_model_uri: ClassVar[URIRef] = SIO.ToTransport


class Township(GeopoliticalRegion):
    """
    A township is a rural or sub-urban settlement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Township
    class_class_curie: ClassVar[str] = "sio:Township"
    class_name: ClassVar[str] = "Township"
    class_model_uri: ClassVar[URIRef] = SIO.Township


class ToxicRole(ChemicalSubstanceRole):
    """
    A toxic role is the role of a chemical substance that is poisonous.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToxicRole
    class_class_curie: ClassVar[str] = "sio:ToxicRole"
    class_name: ClassVar[str] = "ToxicRole"
    class_model_uri: ClassVar[URIRef] = SIO.ToxicRole


class PoisonRole(ToxicRole):
    """
    A poison role is the role of a substance that causes some negative disturbance in an organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PoisonRole
    class_class_curie: ClassVar[str] = "sio:PoisonRole"
    class_name: ClassVar[str] = "PoisonRole"
    class_model_uri: ClassVar[URIRef] = SIO.PoisonRole


class Toxicity(ChemicalQuality):
    """
    toxicity is the quality of a chemical substance to cause injury to an organism in a dose dependent manner.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Toxicity
    class_class_curie: ClassVar[str] = "sio:Toxicity"
    class_name: ClassVar[str] = "Toxicity"
    class_model_uri: ClassVar[URIRef] = SIO.Toxicity


class NonToxic(Toxicity):
    """
    non toxic is the quality of a substance having no damaging effect to a system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.NonToxic
    class_class_curie: ClassVar[str] = "sio:NonToxic"
    class_name: ClassVar[str] = "NonToxic"
    class_model_uri: ClassVar[URIRef] = SIO.NonToxic


class Toxic(Toxicity):
    """
    toxic is the quality of a substance imparing the normal functioning of a  system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Toxic
    class_class_curie: ClassVar[str] = "sio:Toxic"
    class_name: ClassVar[str] = "Toxic"
    class_model_uri: ClassVar[URIRef] = SIO.Toxic


class ToxinRole(PoisonRole):
    """
    A toxin role is a toxic role of a chemical substance that is poisonous and is produced by an organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ToxinRole
    class_class_curie: ClassVar[str] = "sio:ToxinRole"
    class_name: ClassVar[str] = "ToxinRole"
    class_model_uri: ClassVar[URIRef] = SIO.ToxinRole


class Trans-regulatoryElement(NucleicAcidPart):
    """
    A trans-regulatory element is a DNA sequence associated with the regulation of a gene located outside the genomic
    region supporting the corresponding structural DNA region of the trans-regulatory element (i.e., a different DNA
    strand or different chromosome).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Trans-regulatoryElement"]
    class_class_curie: ClassVar[str] = "sio:Trans-regulatoryElement"
    class_name: ClassVar[str] = "Trans-regulatoryElement"
    class_model_uri: ClassVar[URIRef] = SIO.Trans-regulatoryElement


class Transcription(Biosynthesis):
    """
    transcription is the process of creating a complementary RNA copy of a sequence of DNA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Transcription
    class_class_curie: ClassVar[str] = "sio:Transcription"
    class_name: ClassVar[str] = "Transcription"
    class_model_uri: ClassVar[URIRef] = SIO.Transcription


class TransferRNAtRNA(Non-proteinCodingRNAncRNA):
    """
    A transfer RNA (tRNA) is an RNA molecule that aids in the translation of a messenger RNA (mRNA) to produce a
    protein product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TransferRNAtRNA
    class_class_curie: ClassVar[str] = "sio:TransferRNAtRNA"
    class_name: ClassVar[str] = "TransferRNAtRNA"
    class_model_uri: ClassVar[URIRef] = SIO.TransferRNAtRNA


class TransferRNAtRNAGene(Non-proteinCodingRNAncRNAGene):
    """
    A transfer RNA (tRNA) gene is a gene that codes for a tRNA used in the translation of a messenger RNA (mRNA) to
    produce a protein product.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TransferRNAtRNAGene
    class_class_curie: ClassVar[str] = "sio:TransferRNAtRNAGene"
    class_name: ClassVar[str] = "TransferRNAtRNAGene"
    class_model_uri: ClassVar[URIRef] = SIO.TransferRNAtRNAGene


class Translation(Biosynthesis):
    """
    translation is the process of producing a polypeptide from a ribonucleic acid by a ribosome.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Translation
    class_class_curie: ClassVar[str] = "sio:Translation"
    class_name: ClassVar[str] = "Translation"
    class_model_uri: ClassVar[URIRef] = SIO.Translation


class Transporting(Interacting):
    """
    transporting is a  process in which one object physically moves another object from one location to another.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Transporting
    class_class_curie: ClassVar[str] = "sio:Transporting"
    class_name: ClassVar[str] = "Transporting"
    class_model_uri: ClassVar[URIRef] = SIO.Transporting


class ChemicalTransport(Transporting):
    """
    chemical transport is the directed movement of a chemical entity by some agent (e.g. transporter).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ChemicalTransport
    class_class_curie: ClassVar[str] = "sio:ChemicalTransport"
    class_name: ClassVar[str] = "ChemicalTransport"
    class_model_uri: ClassVar[URIRef] = SIO.ChemicalTransport


class MembraneTransport(ChemicalTransport):
    """
    membrane transport is the movement of molecules across a membrane.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MembraneTransport
    class_class_curie: ClassVar[str] = "sio:MembraneTransport"
    class_name: ClassVar[str] = "MembraneTransport"
    class_model_uri: ClassVar[URIRef] = SIO.MembraneTransport


class ActiveTransport(MembraneTransport):
    """
    active transport is the movement of a substance across a membrane against its concentration gradient (from low to
    high concentration) and requires chemical energy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ActiveTransport
    class_class_curie: ClassVar[str] = "sio:ActiveTransport"
    class_name: ClassVar[str] = "ActiveTransport"
    class_model_uri: ClassVar[URIRef] = SIO.ActiveTransport


class PassiveTransport(MembraneTransport):
    """
    passive transport is the movement of a substance across a membrane and does not require chemical energy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PassiveTransport
    class_class_curie: ClassVar[str] = "sio:PassiveTransport"
    class_name: ClassVar[str] = "PassiveTransport"
    class_model_uri: ClassVar[URIRef] = SIO.PassiveTransport


class PrimaryActiveTransport(ActiveTransport):
    """
    primary active transport, also called direct active transport, directly uses energy to transport molecules across
    a membrane.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PrimaryActiveTransport
    class_class_curie: ClassVar[str] = "sio:PrimaryActiveTransport"
    class_name: ClassVar[str] = "PrimaryActiveTransport"
    class_model_uri: ClassVar[URIRef] = SIO.PrimaryActiveTransport


class SecondaryActiveTransport(ActiveTransport):
    """
    secondary active transport or co-transport uses electrochemical potential difference created by pumping ions out
    of the cell to transport molecules across a membrane.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SecondaryActiveTransport
    class_class_curie: ClassVar[str] = "sio:SecondaryActiveTransport"
    class_name: ClassVar[str] = "SecondaryActiveTransport"
    class_model_uri: ClassVar[URIRef] = SIO.SecondaryActiveTransport


class AntiportEnabledSecondaryActiveTransport(SecondaryActiveTransport):
    """
    antiport enabled secondary active transport is a secondary active transfort in which both ion and molecule are
    transported in opposite directions simultaneously.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.AntiportEnabledSecondaryActiveTransport
    class_class_curie: ClassVar[str] = "sio:AntiportEnabledSecondaryActiveTransport"
    class_name: ClassVar[str] = "AntiportEnabledSecondaryActiveTransport"
    class_model_uri: ClassVar[URIRef] = SIO.AntiportEnabledSecondaryActiveTransport


class SymportEnabledSecondaryActiveTransport(SecondaryActiveTransport):
    """
    symport enabled secondary active transport is a secondary active transfort in which both ion and molecule are
    transported in the same direction simultaneously.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SymportEnabledSecondaryActiveTransport
    class_class_curie: ClassVar[str] = "sio:SymportEnabledSecondaryActiveTransport"
    class_name: ClassVar[str] = "SymportEnabledSecondaryActiveTransport"
    class_model_uri: ClassVar[URIRef] = SIO.SymportEnabledSecondaryActiveTransport


class TreeDiagram(DirectedAcyclicGraph):
    """
    A tree diagram is a hierarchical network diagram in which a root vertex is connected to one or more other vertices
    through a directed edge, which in turn may be connected to other vertices.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TreeDiagram
    class_class_curie: ClassVar[str] = "sio:TreeDiagram"
    class_name: ClassVar[str] = "TreeDiagram"
    class_model_uri: ClassVar[URIRef] = SIO.TreeDiagram


class Dendrogram(TreeDiagram):
    """
    A dendrogram is a tree diagram used to illustrate the arrangement of the clusters produced by hierarchical
    clustering.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Dendrogram
    class_class_curie: ClassVar[str] = "sio:Dendrogram"
    class_name: ClassVar[str] = "Dendrogram"
    class_model_uri: ClassVar[URIRef] = SIO.Dendrogram


class Treemap(MereologicalChart):
    """
    A treemap is a chart that fully partitions the area into a set of rectangles whose area represents its relative
    value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Treemap
    class_class_curie: ClassVar[str] = "sio:Treemap"
    class_name: ClassVar[str] = "Treemap"
    class_model_uri: ClassVar[URIRef] = SIO.Treemap


class TrendLine(StatisticalGraphLine):
    """
    A trend line is a line, line segment or ray that is part of a statistical graph which indicates a statistical or
    visual direction across categorical or value data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TrendLine
    class_class_curie: ClassVar[str] = "sio:TrendLine"
    class_name: ClassVar[str] = "TrendLine"
    class_model_uri: ClassVar[URIRef] = SIO.TrendLine


class DecreasingLine(TrendLine):
    """
    An decreasing line is a line segment in which the startpoint and endpoint are ordered along one dimension and the
    difference of values in a second dimension is negative.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DecreasingLine
    class_class_curie: ClassVar[str] = "sio:DecreasingLine"
    class_name: ClassVar[str] = "DecreasingLine"
    class_model_uri: ClassVar[URIRef] = SIO.DecreasingLine


class IncreasingLine(TrendLine):
    """
    An increasing line is a line segment in which the startpoint and endpoint are ordered along one dimension and the
    difference of values in a second dimension is positive.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IncreasingLine
    class_class_curie: ClassVar[str] = "sio:IncreasingLine"
    class_name: ClassVar[str] = "IncreasingLine"
    class_model_uri: ClassVar[URIRef] = SIO.IncreasingLine


class PlateauLine(TrendLine):
    """
    An plateau line is a line segment in which the startpoint and endpoint are ordered along one dimension and the
    difference of values in a second dimension is zero.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.PlateauLine
    class_class_curie: ClassVar[str] = "sio:PlateauLine"
    class_name: ClassVar[str] = "PlateauLine"
    class_model_uri: ClassVar[URIRef] = SIO.PlateauLine


class Triangle(Polygon):
    """
    A triangle is a polygon composed of three points and three line segments, in which each point is fully connected
    to another point along through the line segment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Triangle
    class_class_curie: ClassVar[str] = "sio:Triangle"
    class_name: ClassVar[str] = "Triangle"
    class_model_uri: ClassVar[URIRef] = SIO.Triangle


class TripleBond(CovalentBond):
    """
    A triple bond is a covalent bond between a pair of atoms in which three pairs of electrons are shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TripleBond
    class_class_curie: ClassVar[str] = "sio:TripleBond"
    class_name: ClassVar[str] = "TripleBond"
    class_model_uri: ClassVar[URIRef] = SIO.TripleBond


class TruthValue(InformationalQuality):
    """
    truth value is a quality of information that is claimed/verified to be true or false.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TruthValue
    class_class_curie: ClassVar[str] = "sio:TruthValue"
    class_name: ClassVar[str] = "TruthValue"
    class_model_uri: ClassVar[URIRef] = SIO.TruthValue


class False(TruthValue):
    """
    false is a truth value in that indicates that it is not true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.False
    class_class_curie: ClassVar[str] = "sio:False"
    class_name: ClassVar[str] = "False"
    class_model_uri: ClassVar[URIRef] = SIO.False


class True(TruthValue):
    """
    true is a truth value that indicates that it holds under all possible worlds.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.True
    class_class_curie: ClassVar[str] = "sio:True"
    class_name: ClassVar[str] = "True"
    class_model_uri: ClassVar[URIRef] = SIO.True


class TungstenAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TungstenAtom
    class_class_curie: ClassVar[str] = "sio:TungstenAtom"
    class_name: ClassVar[str] = "TungstenAtom"
    class_model_uri: ClassVar[URIRef] = SIO.TungstenAtom


class URL(InformationalEntityIdentifier):
    """
    A Uniform Resource Locator or Universal Resource Locator (URL) is a specific character string that constitutes a
    reference to an Internet resource.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.URL
    class_class_curie: ClassVar[str] = "sio:URL"
    class_name: ClassVar[str] = "URL"
    class_model_uri: ClassVar[URIRef] = SIO.URL


class UncertaintyValue(Quantity):
    """
    The uncertainty value (margin of error) of a measurement is a range of values likely to enclose the true value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UncertaintyValue
    class_class_curie: ClassVar[str] = "sio:UncertaintyValue"
    class_name: ClassVar[str] = "UncertaintyValue"
    class_model_uri: ClassVar[URIRef] = SIO.UncertaintyValue


class Uncharged(ChargeQuality):
    """
    The quality of not having a charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Uncharged
    class_class_curie: ClassVar[str] = "sio:Uncharged"
    class_name: ClassVar[str] = "Uncharged"
    class_model_uri: ClassVar[URIRef] = SIO.Uncharged


class UndergraduateStudentAdvisorRole(StudentAdvisorRole):
    """
    An undergraduate student advisor role is the role of an individual employed at an academic organization that is
    involved in advising undergraduate students.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UndergraduateStudentAdvisorRole
    class_class_curie: ClassVar[str] = "sio:UndergraduateStudentAdvisorRole"
    class_name: ClassVar[str] = "UndergraduateStudentAdvisorRole"
    class_model_uri: ClassVar[URIRef] = SIO.UndergraduateStudentAdvisorRole


class UnicellularOrganism(Cell):
    """
    A unicellular organism is a organism that is composed of a single cell.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnicellularOrganism
    class_class_curie: ClassVar[str] = "sio:UnicellularOrganism"
    class_name: ClassVar[str] = "UnicellularOrganism"
    class_model_uri: ClassVar[URIRef] = SIO.UnicellularOrganism


class E.coli(UnicellularOrganism):
    """
    Escherichia coli (e coli) is a Gram-negative, rod-shaped bacterium that is commonly found in the lower intestine
    of warm-blooded organisms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["E.coli"]
    class_class_curie: ClassVar[str] = "sio:E.coli"
    class_name: ClassVar[str] = "E.coli"
    class_model_uri: ClassVar[URIRef] = SIO.E.coli


class UnigeneCluster(Collection):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnigeneCluster
    class_class_curie: ClassVar[str] = "sio:UnigeneCluster"
    class_name: ClassVar[str] = "UnigeneCluster"
    class_model_uri: ClassVar[URIRef] = SIO.UnigeneCluster


class Union(List):
    """
    A union is a list of all of the values of an attribute for the entities in the defined set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Union
    class_class_curie: ClassVar[str] = "sio:Union"
    class_name: ClassVar[str] = "Union"
    class_model_uri: ClassVar[URIRef] = SIO.Union


class UniqueCell(Cellinformational):
    """
    A unique cell is a cell that contains a unique value in the cellular automaton.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UniqueCell
    class_class_curie: ClassVar[str] = "sio:UniqueCell"
    class_name: ClassVar[str] = "UniqueCell"
    class_model_uri: ClassVar[URIRef] = SIO.UniqueCell


@dataclass
class UniqueIdentifier(Identifier):
    """
    A unique identifier is an identifier that uniquely identifies some thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UniqueIdentifier
    class_class_curie: ClassVar[str] = "sio:UniqueIdentifier"
    class_name: ClassVar[str] = "UniqueIdentifier"
    class_model_uri: ClassVar[URIRef] = SIO.UniqueIdentifier

    isUniqueIdentifierFor: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isUniqueIdentifierFor is not None and not isinstance(self.isUniqueIdentifierFor, Entity):
            self.isUniqueIdentifierFor = Entity(**as_dict(self.isUniqueIdentifierFor))

        super().__post_init__(**kwargs)


@dataclass
class UnitOfMeasurement(Quantity):
    """
    A unit of measurement is a definite magnitude of a physical quantity, defined and adopted by convention and/or by
    law, that is used as a standard for measurement of the same physical quantity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnitOfMeasurement
    class_class_curie: ClassVar[str] = "sio:UnitOfMeasurement"
    class_name: ClassVar[str] = "UnitOfMeasurement"
    class_model_uri: ClassVar[URIRef] = SIO.UnitOfMeasurement

    isUnitOf: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isUnitOf is not None and not isinstance(self.isUnitOf, Entity):
            self.isUnitOf = Entity(**as_dict(self.isUnitOf))

        super().__post_init__(**kwargs)


class University(AcademicOrganization):
    """
    A university is an institution of higher education and research which grants academic degrees in a variety of
    subjects and provides both undergraduate education and postgraduate education.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.University
    class_class_curie: ClassVar[str] = "sio:University"
    class_name: ClassVar[str] = "University"
    class_model_uri: ClassVar[URIRef] = SIO.University


class Unsupported(ExistenceQuality):
    """
    unsupported is an existence quality in which there is no evidence to support the existence of the entity in any
    world (real or hypothetical)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Unsupported
    class_class_curie: ClassVar[str] = "sio:Unsupported"
    class_name: ClassVar[str] = "Unsupported"
    class_model_uri: ClassVar[URIRef] = SIO.Unsupported


class UnunhexiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnunhexiumAtom
    class_class_curie: ClassVar[str] = "sio:UnunhexiumAtom"
    class_name: ClassVar[str] = "UnunhexiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.UnunhexiumAtom


class UnunoctiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnunoctiumAtom
    class_class_curie: ClassVar[str] = "sio:UnunoctiumAtom"
    class_name: ClassVar[str] = "UnunoctiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.UnunoctiumAtom


class UnunpentiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnunpentiumAtom
    class_class_curie: ClassVar[str] = "sio:UnunpentiumAtom"
    class_name: ClassVar[str] = "UnunpentiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.UnunpentiumAtom


class UnunquadiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnunquadiumAtom
    class_class_curie: ClassVar[str] = "sio:UnunquadiumAtom"
    class_name: ClassVar[str] = "UnunquadiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.UnunquadiumAtom


class UnunseptiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnunseptiumAtom
    class_class_curie: ClassVar[str] = "sio:UnunseptiumAtom"
    class_name: ClassVar[str] = "UnunseptiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.UnunseptiumAtom


class UnutriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UnutriumAtom
    class_class_curie: ClassVar[str] = "sio:UnutriumAtom"
    class_name: ClassVar[str] = "UnutriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.UnutriumAtom


class UraniumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UraniumAtom
    class_class_curie: ClassVar[str] = "sio:UraniumAtom"
    class_name: ClassVar[str] = "UraniumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.UraniumAtom


class UserAccount(ComputationalEntity):
    """
    user account allows a user to authenticate to system services and be granted authorization to access them.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.UserAccount
    class_class_curie: ClassVar[str] = "sio:UserAccount"
    class_name: ClassVar[str] = "UserAccount"
    class_model_uri: ClassVar[URIRef] = SIO.UserAccount


class ValidArgument(Argument):
    """
    A valid argument is an argument where the truth of the conclusion is a logical consequence of the premises and
    (consequently) its corresponding conditional is a necessary truth.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ValidArgument
    class_class_curie: ClassVar[str] = "sio:ValidArgument"
    class_name: ClassVar[str] = "ValidArgument"
    class_model_uri: ClassVar[URIRef] = SIO.ValidArgument


class SoundArgument(ValidArgument):
    """
    A sound argument is a valid argument with true premises.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoundArgument
    class_class_curie: ClassVar[str] = "sio:SoundArgument"
    class_name: ClassVar[str] = "SoundArgument"
    class_model_uri: ClassVar[URIRef] = SIO.SoundArgument


class ValidatedGene(Gene):
    """
    An experimentally validated gene is a gene whose existence has been demonstrated through experimental methods.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ValidatedGene
    class_class_curie: ClassVar[str] = "sio:ValidatedGene"
    class_name: ClassVar[str] = "ValidatedGene"
    class_model_uri: ClassVar[URIRef] = SIO.ValidatedGene


class ValueAxis(Axis):
    """
    A value axis is an axis in which the position along the line is partioned into numeric values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ValueAxis
    class_class_curie: ClassVar[str] = "sio:ValueAxis"
    class_name: ClassVar[str] = "ValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.ValueAxis


class BottomValueAxis(ValueAxis):
    """
    A bottom value axis is a value axis that is spatially positioned to the bottom of the plot area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BottomValueAxis
    class_class_curie: ClassVar[str] = "sio:BottomValueAxis"
    class_name: ClassVar[str] = "BottomValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.BottomValueAxis


class CartesianCoordinateAxis(ValueAxis):
    """
    A Cartesian coordinate axis is an axis whose behavior follows that of a Cartesian coordinate system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CartesianCoordinateAxis
    class_class_curie: ClassVar[str] = "sio:CartesianCoordinateAxis"
    class_name: ClassVar[str] = "CartesianCoordinateAxis"
    class_model_uri: ClassVar[URIRef] = SIO.CartesianCoordinateAxis


class LeftValueAxis(ValueAxis):
    """
    A left value axis is a value axis that is spatially positioned to the left of the plot area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LeftValueAxis
    class_class_curie: ClassVar[str] = "sio:LeftValueAxis"
    class_name: ClassVar[str] = "LeftValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.LeftValueAxis


class RightValueAxis(ValueAxis):
    """
    A right value axis is a value axis that is spatially positioned to the right of the plot area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RightValueAxis
    class_class_curie: ClassVar[str] = "sio:RightValueAxis"
    class_name: ClassVar[str] = "RightValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.RightValueAxis


class ScaledValueAxis(ValueAxis):
    """
    A scaled value axis is a value axis in which the value range was subject to a mathematic transformation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ScaledValueAxis
    class_class_curie: ClassVar[str] = "sio:ScaledValueAxis"
    class_name: ClassVar[str] = "ScaledValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.ScaledValueAxis


class LinearValueAxis(ScaledValueAxis):
    """
    A linear value axis is a value axis that corresponds to a scaling factor of 1 of the value range.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LinearValueAxis
    class_class_curie: ClassVar[str] = "sio:LinearValueAxis"
    class_name: ClassVar[str] = "LinearValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.LinearValueAxis


class LogarithmicValueAxis(ScaledValueAxis):
    """
    A logarithmic value axis is a scaled value axis that corresponds to a scaling factor of the logarithm of the value
    range.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LogarithmicValueAxis
    class_class_curie: ClassVar[str] = "sio:LogarithmicValueAxis"
    class_name: ClassVar[str] = "LogarithmicValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.LogarithmicValueAxis


class TopValueAxis(ValueAxis):
    """
    A top value axis is a value axis that is spatially positioned to the top of the plot area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.TopValueAxis
    class_class_curie: ClassVar[str] = "sio:TopValueAxis"
    class_name: ClassVar[str] = "TopValueAxis"
    class_model_uri: ClassVar[URIRef] = SIO.TopValueAxis


class VanadiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VanadiumAtom
    class_class_curie: ClassVar[str] = "sio:VanadiumAtom"
    class_name: ClassVar[str] = "VanadiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.VanadiumAtom


class Variable(MathematicalEntity):
    """
    A variable is a value that may change within the scope of a given problem or set of operations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Variable
    class_class_curie: ClassVar[str] = "sio:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = SIO.Variable


class ControlVariable(Variable):
    """
    A control variable that is believed to alter the dependent or independent variables, but may not actually be the
    focus of the experiment. So that variable will be kept constant or monitored to try to minimise its effect on the
    experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ControlVariable
    class_class_curie: ClassVar[str] = "sio:ControlVariable"
    class_name: ClassVar[str] = "ControlVariable"
    class_model_uri: ClassVar[URIRef] = SIO.ControlVariable


class DependentVariable(Variable):
    """
    A dependent variable is one whose value changes as a consequence of changes in other values in the system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DependentVariable
    class_class_curie: ClassVar[str] = "sio:DependentVariable"
    class_name: ClassVar[str] = "DependentVariable"
    class_model_uri: ClassVar[URIRef] = SIO.DependentVariable


class IndependentVariable(Variable):
    """
    An independent variable is a variable that may take on different values independent of other elements in a system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IndependentVariable
    class_class_curie: ClassVar[str] = "sio:IndependentVariable"
    class_name: ClassVar[str] = "IndependentVariable"
    class_model_uri: ClassVar[URIRef] = SIO.IndependentVariable


class Parameter(IndependentVariable):
    """
    A parameter is variable whose value changes the characteristics of a system or a function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Parameter
    class_class_curie: ClassVar[str] = "sio:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = SIO.Parameter


class DefaultParameter(Parameter):
    """
    A default parameter is a parameter which has a default value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DefaultParameter
    class_class_curie: ClassVar[str] = "sio:DefaultParameter"
    class_name: ClassVar[str] = "DefaultParameter"
    class_model_uri: ClassVar[URIRef] = SIO.DefaultParameter


class VariantRole(ComparativeRole):
    """
    A variant role is a comparative role in which the value of an attribute differs when compared to another entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VariantRole
    class_class_curie: ClassVar[str] = "sio:VariantRole"
    class_name: ClassVar[str] = "VariantRole"
    class_model_uri: ClassVar[URIRef] = SIO.VariantRole


class SequenceVariantRole(VariantRole):
    """
    A sequence variant role is a comparative role in which the composition of characters in a sequence differs when
    compared to another entity of similar type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SequenceVariantRole
    class_class_curie: ClassVar[str] = "sio:SequenceVariantRole"
    class_name: ClassVar[str] = "SequenceVariantRole"
    class_model_uri: ClassVar[URIRef] = SIO.SequenceVariantRole


class DeletionVariantRole(SequenceVariantRole):
    """
    A deletion variant role is the role of an sequence that lacks a sub-sequence relative to the frame of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DeletionVariantRole
    class_class_curie: ClassVar[str] = "sio:DeletionVariantRole"
    class_name: ClassVar[str] = "DeletionVariantRole"
    class_model_uri: ClassVar[URIRef] = SIO.DeletionVariantRole


class InsertionVariantRole(SequenceVariantRole):
    """
    An insertion variant role is the role of an sequence that contains a sub-sequence that is considered to be an
    addition relative to the frame of reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.InsertionVariantRole
    class_class_curie: ClassVar[str] = "sio:InsertionVariantRole"
    class_name: ClassVar[str] = "InsertionVariantRole"
    class_model_uri: ClassVar[URIRef] = SIO.InsertionVariantRole


class Vector(RankNonzeroTensor):
    """
    a vector is a rank 1 tensor that is described by n-dimension of scalars.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Vector
    class_class_curie: ClassVar[str] = "sio:Vector"
    class_name: ClassVar[str] = "Vector"
    class_model_uri: ClassVar[URIRef] = SIO.Vector


class VectorLine(Ray):
    """
    A vector line is a line which that is bounded by a startpoint and extends outwards along one dimension.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VectorLine
    class_class_curie: ClassVar[str] = "sio:VectorLine"
    class_name: ClassVar[str] = "VectorLine"
    class_model_uri: ClassVar[URIRef] = SIO.VectorLine


class SurfaceNormal(VectorLine):
    """
    A surface normal is a vector that is perpendicular to a flat surface.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SurfaceNormal
    class_class_curie: ClassVar[str] = "sio:SurfaceNormal"
    class_name: ClassVar[str] = "SurfaceNormal"
    class_model_uri: ClassVar[URIRef] = SIO.SurfaceNormal


class VectorSpace(MathematicalEntity):
    """
    a vector space is a set of vectors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VectorSpace
    class_class_curie: ClassVar[str] = "sio:VectorSpace"
    class_name: ClassVar[str] = "VectorSpace"
    class_model_uri: ClassVar[URIRef] = SIO.VectorSpace


class Velocity(Speed):
    """
    The rate of change of an object's position and the direction of that change
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Velocity
    class_class_curie: ClassVar[str] = "sio:Velocity"
    class_name: ClassVar[str] = "Velocity"
    class_model_uri: ClassVar[URIRef] = SIO.Velocity


class VennDiagram(Chart):
    """
    A Venn diagram is a chart that illustrates all possible logical relations between a finite collection of sets as
    overlapping circles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VennDiagram
    class_class_curie: ClassVar[str] = "sio:VennDiagram"
    class_name: ClassVar[str] = "VennDiagram"
    class_model_uri: ClassVar[URIRef] = SIO.VennDiagram


class VerbalLanguage(Language):
    """
    A verbal language is a language that uses sounds to communicate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VerbalLanguage
    class_class_curie: ClassVar[str] = "sio:VerbalLanguage"
    class_name: ClassVar[str] = "VerbalLanguage"
    class_model_uri: ClassVar[URIRef] = SIO.VerbalLanguage


class VerbalLanguageEntity(LanguageEntity):
    """
    A verbal language entity is a language entity that is manifested through sound.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VerbalLanguageEntity
    class_class_curie: ClassVar[str] = "sio:VerbalLanguageEntity"
    class_name: ClassVar[str] = "VerbalLanguageEntity"
    class_model_uri: ClassVar[URIRef] = SIO.VerbalLanguageEntity


class Consonant(VerbalLanguageEntity):
    """
    A consonant is a verbal entity of language that is articulated with complete or partial closure of the vocal tract.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Consonant
    class_class_curie: ClassVar[str] = "sio:Consonant"
    class_name: ClassVar[str] = "Consonant"
    class_model_uri: ClassVar[URIRef] = SIO.Consonant


class Syllable(VerbalLanguageEntity):
    """
    A syllable is a verbal entity of language having one vowel sound, with or without surrounding consonants, forming
    the whole or a part of a word.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Syllable
    class_class_curie: ClassVar[str] = "sio:Syllable"
    class_name: ClassVar[str] = "Syllable"
    class_model_uri: ClassVar[URIRef] = SIO.Syllable


class VersionLabel(Identifier):
    """
    A version label is a label for a particular form or variation of an earlier or original type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VersionLabel
    class_class_curie: ClassVar[str] = "sio:VersionLabel"
    class_name: ClassVar[str] = "VersionLabel"
    class_model_uri: ClassVar[URIRef] = SIO.VersionLabel


class DocumentVersion(VersionLabel):
    """
    A document version is a version of a work in some sequence of derivative works.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.DocumentVersion
    class_class_curie: ClassVar[str] = "sio:DocumentVersion"
    class_name: ClassVar[str] = "DocumentVersion"
    class_model_uri: ClassVar[URIRef] = SIO.DocumentVersion


class SoftwareVersionLabel(VersionLabel):
    """
    A software version label is a version label for a piece of software.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoftwareVersionLabel
    class_class_curie: ClassVar[str] = "sio:SoftwareVersionLabel"
    class_name: ClassVar[str] = "SoftwareVersionLabel"
    class_model_uri: ClassVar[URIRef] = SIO.SoftwareVersionLabel


class MajorVersionNumber(SoftwareVersionLabel):
    """
    A major version number is a version of a software that exhibits a significant change in functionalilty from a
    prior version.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MajorVersionNumber
    class_class_curie: ClassVar[str] = "sio:MajorVersionNumber"
    class_name: ClassVar[str] = "MajorVersionNumber"
    class_model_uri: ClassVar[URIRef] = SIO.MajorVersionNumber


class MinorVersionNumber(SoftwareVersionLabel):
    """
    A minor version number is a version of a software that exhibits minor features or significant fix from a prior
    version.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.MinorVersionNumber
    class_class_curie: ClassVar[str] = "sio:MinorVersionNumber"
    class_name: ClassVar[str] = "MinorVersionNumber"
    class_model_uri: ClassVar[URIRef] = SIO.MinorVersionNumber


class RevisionNumber(SoftwareVersionLabel):
    """
    A revision number is a version of a software in which bugs have been fixed from a prior version.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RevisionNumber
    class_class_curie: ClassVar[str] = "sio:RevisionNumber"
    class_name: ClassVar[str] = "RevisionNumber"
    class_model_uri: ClassVar[URIRef] = SIO.RevisionNumber


class VersionedDataset(Dataset):
    """
    a versioned dataset is a dataset with a particular release date or release number.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VersionedDataset
    class_class_curie: ClassVar[str] = "sio:VersionedDataset"
    class_name: ClassVar[str] = "VersionedDataset"
    class_model_uri: ClassVar[URIRef] = SIO.VersionedDataset


class VersionedRecord(Record):
    """
    A versioned record is a record for which there exists another variant based that was derived via modification of
    the facts.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VersionedRecord
    class_class_curie: ClassVar[str] = "sio:VersionedRecord"
    class_name: ClassVar[str] = "VersionedRecord"
    class_model_uri: ClassVar[URIRef] = SIO.VersionedRecord


class VertexNormal(VectorLine):
    """
    A vertext normal is the normalized average of the surface normals of the faces that contain that vertex.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VertexNormal
    class_class_curie: ClassVar[str] = "sio:VertexNormal"
    class_name: ClassVar[str] = "VertexNormal"
    class_model_uri: ClassVar[URIRef] = SIO.VertexNormal


class VerticalBarGraph(BarGraph):
    """
    A vertical bar graph is a bar graph in which the rectangular bars are vertically oriented in space.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VerticalBarGraph
    class_class_curie: ClassVar[str] = "sio:VerticalBarGraph"
    class_name: ClassVar[str] = "VerticalBarGraph"
    class_model_uri: ClassVar[URIRef] = SIO.VerticalBarGraph


class VerticalLine(PositionallyOrientedLine):
    """
    A vertical line is a line that is positionally oriented perpendicular to the horizon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VerticalLine
    class_class_curie: ClassVar[str] = "sio:VerticalLine"
    class_name: ClassVar[str] = "VerticalLine"
    class_model_uri: ClassVar[URIRef] = SIO.VerticalLine


class VeryDissatisfiedQualifier(SatisfactionQualifier):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VeryDissatisfiedQualifier
    class_class_curie: ClassVar[str] = "sio:VeryDissatisfiedQualifier"
    class_name: ClassVar[str] = "VeryDissatisfiedQualifier"
    class_model_uri: ClassVar[URIRef] = SIO.VeryDissatisfiedQualifier


class VeryGoodQuality(QualityDescriptor):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VeryGoodQuality
    class_class_curie: ClassVar[str] = "sio:VeryGoodQuality"
    class_name: ClassVar[str] = "VeryGoodQuality"
    class_model_uri: ClassVar[URIRef] = SIO.VeryGoodQuality


class VeryPoorQuality(QualityDescriptor):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VeryPoorQuality
    class_class_curie: ClassVar[str] = "sio:VeryPoorQuality"
    class_name: ClassVar[str] = "VeryPoorQuality"
    class_model_uri: ClassVar[URIRef] = SIO.VeryPoorQuality


class Viroid(Non-cellularOrganism):
    """
    A viroid is a molecule of RNA that does not code for and is not protected by a protein coat.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Viroid
    class_class_curie: ClassVar[str] = "sio:Viroid"
    class_name: ClassVar[str] = "Viroid"
    class_model_uri: ClassVar[URIRef] = SIO.Viroid


class Virtual(ExistenceQuality):
    """
    virtual is the quality of an entity that exists only in a virtual setting such as a simulation or game environment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Virtual
    class_class_curie: ClassVar[str] = "sio:Virtual"
    class_name: ClassVar[str] = "Virtual"
    class_model_uri: ClassVar[URIRef] = SIO.Virtual


class Virus(Non-cellularOrganism):
    """
    A virus is a non-cellular organism that can replicate only inside the living cells of an organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Virus
    class_class_curie: ClassVar[str] = "sio:Virus"
    class_name: ClassVar[str] = "Virus"
    class_model_uri: ClassVar[URIRef] = SIO.Virus


class VisualLanguageEntity(LanguageEntity):
    """
    A visual language entity is a language entity that is manifested within the spectrum of light and can be
    pereceived and processed by a visual system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VisualLanguageEntity
    class_class_curie: ClassVar[str] = "sio:VisualLanguageEntity"
    class_name: ClassVar[str] = "VisualLanguageEntity"
    class_model_uri: ClassVar[URIRef] = SIO.VisualLanguageEntity


class Vocabulary(FormalSpecification):
    """
    A vocabulary is a collection of terms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Vocabulary
    class_class_curie: ClassVar[str] = "sio:Vocabulary"
    class_name: ClassVar[str] = "Vocabulary"
    class_model_uri: ClassVar[URIRef] = SIO.Vocabulary


class Terminology(Vocabulary):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Terminology
    class_class_curie: ClassVar[str] = "sio:Terminology"
    class_name: ClassVar[str] = "Terminology"
    class_model_uri: ClassVar[URIRef] = SIO.Terminology


class Volume(3DExtentQuantity):
    """
    volume is the quantity of three-dimensional space enclosed by some closed boundary.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Volume
    class_class_curie: ClassVar[str] = "sio:Volume"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = SIO.Volume


class VolumeNumber(Count):
    """
    volume number is a count of a sequence of periodicals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VolumeNumber
    class_class_curie: ClassVar[str] = "sio:VolumeNumber"
    class_name: ClassVar[str] = "VolumeNumber"
    class_model_uri: ClassVar[URIRef] = SIO.VolumeNumber


class Vowel(VerbalLanguageEntity):
    """
    A vowel is a verbal entity of language that is pronounced with an open vocal tract so that there is no build-up of
    air pressure at any point above the glottis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Vowel
    class_class_curie: ClassVar[str] = "sio:Vowel"
    class_name: ClassVar[str] = "Vowel"
    class_model_uri: ClassVar[URIRef] = SIO.Vowel


class Wave(HeterogeneousSubstance):
    """
    A wave is a physical entity that travels through space and time, consist of oscillations or vibrations and may be
    accompanied by the transfer of energy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Wave
    class_class_curie: ClassVar[str] = "sio:Wave"
    class_name: ClassVar[str] = "Wave"
    class_model_uri: ClassVar[URIRef] = SIO.Wave


class SoundWave(Wave):
    """
    A sound wave is a mechanical wave that is an oscillation of pressure transmitted through a solid, liquid, or gas,
    composed of frequencies within the range of hearing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SoundWave
    class_class_curie: ClassVar[str] = "sio:SoundWave"
    class_name: ClassVar[str] = "SoundWave"
    class_model_uri: ClassVar[URIRef] = SIO.SoundWave


class Weak(Intensity):
    """
    weak is a qualitative intensity value that is more intense than none, but less intense than mild.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Weak
    class_class_curie: ClassVar[str] = "sio:Weak"
    class_name: ClassVar[str] = "Weak"
    class_model_uri: ClassVar[URIRef] = SIO.Weak


class WeakChemicalSalt(ChemicalSalt):
    """
    a weak chemical salt is a chemical salt composed of weak eletrolytes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WeakChemicalSalt
    class_class_curie: ClassVar[str] = "sio:WeakChemicalSalt"
    class_name: ClassVar[str] = "WeakChemicalSalt"
    class_model_uri: ClassVar[URIRef] = SIO.WeakChemicalSalt


class WeakSubmolecularComponent(SubmolecularEntity):
    """
    A weak submolecular component is a submolecular component that weakly connects submolecular components.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WeakSubmolecularComponent
    class_class_curie: ClassVar[str] = "sio:WeakSubmolecularComponent"
    class_name: ClassVar[str] = "WeakSubmolecularComponent"
    class_model_uri: ClassVar[URIRef] = SIO.WeakSubmolecularComponent


class BasePair(WeakSubmolecularComponent):
    """
    A base pair is a weak molecular interaction composed of hydrogen bonds between nucleobases.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BasePair
    class_class_curie: ClassVar[str] = "sio:BasePair"
    class_name: ClassVar[str] = "BasePair"
    class_model_uri: ClassVar[URIRef] = SIO.BasePair


class BaseStack(WeakSubmolecularComponent):
    """
    A base stack is a stabilizing interaction of DNA and RNA between spatially adjacent nucleotides and possibly
    involving London dispersion, hydrophobic and electrostatic forces.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.BaseStack
    class_class_curie: ClassVar[str] = "sio:BaseStack"
    class_name: ClassVar[str] = "BaseStack"
    class_model_uri: ClassVar[URIRef] = SIO.BaseStack


class Dipole-dipoleInteraction(WeakSubmolecularComponent):
    """
    A dipole-dipole interaction is a weak submolecular interaction between strongly electronegative atoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Dipole-dipoleInteraction"]
    class_class_curie: ClassVar[str] = "sio:Dipole-dipoleInteraction"
    class_name: ClassVar[str] = "Dipole-dipoleInteraction"
    class_model_uri: ClassVar[URIRef] = SIO.Dipole-dipoleInteraction


class HydrogenBond(WeakSubmolecularComponent):
    """
    A hydrogen bond is a weak submolecular interaction formed between a hydrogen atom and a electronegative atom.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.HydrogenBond
    class_class_curie: ClassVar[str] = "sio:HydrogenBond"
    class_name: ClassVar[str] = "HydrogenBond"
    class_model_uri: ClassVar[URIRef] = SIO.HydrogenBond


class IonicInteraction(WeakSubmolecularComponent):
    """
    An ionic interaction is a weak submolecular interaction between a charged submolecules.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.IonicInteraction
    class_class_curie: ClassVar[str] = "sio:IonicInteraction"
    class_name: ClassVar[str] = "IonicInteraction"
    class_model_uri: ClassVar[URIRef] = SIO.IonicInteraction


class CationPiInteraction(IonicInteraction):
    """
    A cation pi interaction is an ionic interaction between the localized negative charge of π orbital electrons,
    located above and below the plane of an aromatic ring, and a positive charge.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.CationPiInteraction
    class_class_curie: ClassVar[str] = "sio:CationPiInteraction"
    class_name: ClassVar[str] = "CationPiInteraction"
    class_model_uri: ClassVar[URIRef] = SIO.CationPiInteraction


class LowBarrierHydrogenBond(HydrogenBond):
    """
    A low barrier hydrogen bond is a shorter, stronger hydrogen bond that is formed between both heteroatoms.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.LowBarrierHydrogenBond
    class_class_curie: ClassVar[str] = "sio:LowBarrierHydrogenBond"
    class_name: ClassVar[str] = "LowBarrierHydrogenBond"
    class_model_uri: ClassVar[URIRef] = SIO.LowBarrierHydrogenBond


class VanDerWaalsInteraction(WeakSubmolecularComponent):
    """
    van der Waals' interaction is an a weak submolecular interaction between an instantaneous dipole and induced
    dipole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.VanDerWaalsInteraction
    class_class_curie: ClassVar[str] = "sio:VanDerWaalsInteraction"
    class_name: ClassVar[str] = "VanDerWaalsInteraction"
    class_model_uri: ClassVar[URIRef] = SIO.VanDerWaalsInteraction


class WebPage(Document):
    """
    A web page is a document that is published according to World Wide Web standards.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WebPage
    class_class_curie: ClassVar[str] = "sio:WebPage"
    class_name: ClassVar[str] = "WebPage"
    class_model_uri: ClassVar[URIRef] = SIO.WebPage


class WebService(SoftwareApplication):
    """
    A web service is a software application that can be accessed over a network, such as the Internet, and executed on
    a remote system hosting the requested services.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WebService
    class_class_curie: ClassVar[str] = "sio:WebService"
    class_name: ClassVar[str] = "WebService"
    class_model_uri: ClassVar[URIRef] = SIO.WebService


class RESTWebService(WebService):
    """
    a REST web service is a web service that provides functionality according to the Representational State Transfer
    (REST) specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.RESTWebService
    class_class_curie: ClassVar[str] = "sio:RESTWebService"
    class_name: ClassVar[str] = "RESTWebService"
    class_model_uri: ClassVar[URIRef] = SIO.RESTWebService


class SOAPWebService(WebService):
    """
    a SOAP web service is a web service that implements Simple Object Access Protocol (SOAP).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SOAPWebService
    class_class_curie: ClassVar[str] = "sio:SOAPWebService"
    class_name: ClassVar[str] = "SOAPWebService"
    class_model_uri: ClassVar[URIRef] = SIO.SOAPWebService


class SemanticWebService(WebService):
    """
    a semantic web service is a web service that provides a formal, machine understanble description of its
    functionality.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SemanticWebService
    class_class_curie: ClassVar[str] = "sio:SemanticWebService"
    class_name: ClassVar[str] = "SemanticWebService"
    class_model_uri: ClassVar[URIRef] = SIO.SemanticWebService


class SADISemanticWebService(SemanticWebService):
    """
    a SADI semantic web service is a semantic web service that follows the SADI specification
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SADISemanticWebService
    class_class_curie: ClassVar[str] = "sio:SADISemanticWebService"
    class_name: ClassVar[str] = "SADISemanticWebService"
    class_model_uri: ClassVar[URIRef] = SIO.SADISemanticWebService


class WebServiceInvocation(SofwareExecution):
    """
    A web service invocation involves the execution of a web service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WebServiceInvocation
    class_class_curie: ClassVar[str] = "sio:WebServiceInvocation"
    class_name: ClassVar[str] = "WebServiceInvocation"
    class_model_uri: ClassVar[URIRef] = SIO.WebServiceInvocation


class SADIWebServiceInvocation(WebServiceInvocation):
    """
    A SADI web service invocation is the excution of a SADI web service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.SADIWebServiceInvocation
    class_class_curie: ClassVar[str] = "sio:SADIWebServiceInvocation"
    class_name: ClassVar[str] = "SADIWebServiceInvocation"
    class_model_uri: ClassVar[URIRef] = SIO.SADIWebServiceInvocation


class Website(CollectionOfDocuments):
    """
    A website is a collection of documents published on the World Wide Web.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Website
    class_class_curie: ClassVar[str] = "sio:Website"
    class_name: ClassVar[str] = "Website"
    class_model_uri: ClassVar[URIRef] = SIO.Website


class Week(TimeInterval):
    """
    A week is a period of 7 consecutive days.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Week
    class_class_curie: ClassVar[str] = "sio:Week"
    class_name: ClassVar[str] = "Week"
    class_model_uri: ClassVar[URIRef] = SIO.Week


class Width(1DExtentQuantity):
    """
    width is the shorter dimensional extent perpendicular to a 2D projection of the object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Width
    class_class_curie: ClassVar[str] = "sio:Width"
    class_name: ClassVar[str] = "Width"
    class_model_uri: ClassVar[URIRef] = SIO.Width


class Wonder(Surprise):
    """
    wonder is an emotion of perceiving something very rare or unexpected, but not threatening.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Wonder
    class_class_curie: ClassVar[str] = "sio:Wonder"
    class_name: ClassVar[str] = "Wonder"
    class_model_uri: ClassVar[URIRef] = SIO.Wonder


class Word(LanguageEntity):
    """
    A word is the smallest free form (an item that may be expressed in isolation with semantic or pragmatic content)
    in a language.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Word
    class_class_curie: ClassVar[str] = "sio:Word"
    class_name: ClassVar[str] = "Word"
    class_model_uri: ClassVar[URIRef] = SIO.Word


class WordEndPosition(TextSpanEndPosition):
    """
    word end position is the position of the last character in a word as an offset from the first character of the
    text in which it is found.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WordEndPosition
    class_class_curie: ClassVar[str] = "sio:WordEndPosition"
    class_name: ClassVar[str] = "WordEndPosition"
    class_model_uri: ClassVar[URIRef] = SIO.WordEndPosition


class WordStartPosition(TextSpanStartPosition):
    """
    The position of the first character in a word as an offset from the first character of the text in which it is
    found.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WordStartPosition
    class_class_curie: ClassVar[str] = "sio:WordStartPosition"
    class_name: ClassVar[str] = "WordStartPosition"
    class_model_uri: ClassVar[URIRef] = SIO.WordStartPosition


class WordTree(TextualChart):
    """
    A word tree is a chart that links phrases with contexts through a tree-like branching structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WordTree
    class_class_curie: ClassVar[str] = "sio:WordTree"
    class_name: ClassVar[str] = "WordTree"
    class_model_uri: ClassVar[URIRef] = SIO.WordTree


class WorkPhoneNumber(TelephoneNumber):
    """
    a work phone number is the number to connect to an phone at a place of work.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WorkPhoneNumber
    class_class_curie: ClassVar[str] = "sio:WorkPhoneNumber"
    class_name: ClassVar[str] = "WorkPhoneNumber"
    class_model_uri: ClassVar[URIRef] = SIO.WorkPhoneNumber


class Workflow(Algorithm):
    """
    A workflow is an algorithm that is is a depiction of a sequence of operations to achieve one or more objectives.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Workflow
    class_class_curie: ClassVar[str] = "sio:Workflow"
    class_name: ClassVar[str] = "Workflow"
    class_model_uri: ClassVar[URIRef] = SIO.Workflow


class Worm(MulticellularOrganism):
    """
    A worm is a non-arthropod invertebrate animal that typically have a long cylindrical tube-like body and no legs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Worm
    class_class_curie: ClassVar[str] = "sio:Worm"
    class_name: ClassVar[str] = "Worm"
    class_model_uri: ClassVar[URIRef] = SIO.Worm


class Worry(Apprehension):
    """
    worry is the emotion characterized by concer over a real or imaginary issue.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Worry
    class_class_curie: ClassVar[str] = "sio:Worry"
    class_name: ClassVar[str] = "Worry"
    class_model_uri: ClassVar[URIRef] = SIO.Worry


class Regret(Worry):
    """
    regret is a feeling of sadness, repentance, or disappointment over something that has happened or been done.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Regret
    class_class_curie: ClassVar[str] = "sio:Regret"
    class_name: ClassVar[str] = "Regret"
    class_model_uri: ClassVar[URIRef] = SIO.Regret


class Remorse(Regret):
    """
    remorse is an emotion of personal regret felt by a person after he or she has committed an act which they deem to
    be shameful, hurtful, or violent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Remorse
    class_class_curie: ClassVar[str] = "sio:Remorse"
    class_name: ClassVar[str] = "Remorse"
    class_model_uri: ClassVar[URIRef] = SIO.Remorse


class Written(TextQuality):
    """
    written is the quality of information that is embodied as visual glyphs in some material form.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Written
    class_class_curie: ClassVar[str] = "sio:Written"
    class_name: ClassVar[str] = "Written"
    class_model_uri: ClassVar[URIRef] = SIO.Written


class Draft(Written):
    """
    draft is the quality of text that has not yet complete.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Draft
    class_class_curie: ClassVar[str] = "sio:Draft"
    class_name: ClassVar[str] = "Draft"
    class_model_uri: ClassVar[URIRef] = SIO.Draft


class Finalized(Written):
    """
    finalized is the quality of a textual entity that is in its final form.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Finalized
    class_class_curie: ClassVar[str] = "sio:Finalized"
    class_name: ClassVar[str] = "Finalized"
    class_model_uri: ClassVar[URIRef] = SIO.Finalized


class Reviewed(Written):
    """
    reviewed is the quality of a textual entity that has been examined and commented on by another party.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Reviewed
    class_class_curie: ClassVar[str] = "sio:Reviewed"
    class_name: ClassVar[str] = "Reviewed"
    class_model_uri: ClassVar[URIRef] = SIO.Reviewed


class EditorReviewed(Reviewed):
    """
    editor reviewed is the quality of a textual entity that has been examined and commented on by an editor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.EditorReviewed
    class_class_curie: ClassVar[str] = "sio:EditorReviewed"
    class_name: ClassVar[str] = "EditorReviewed"
    class_model_uri: ClassVar[URIRef] = SIO.EditorReviewed


class Peer-reviewed(Reviewed):
    """
    peer-reviewed is the quality of a textual entity that has been examined and commented by a peer expert reviewer.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Peer-reviewed"]
    class_class_curie: ClassVar[str] = "sio:Peer-reviewed"
    class_name: ClassVar[str] = "Peer-reviewed"
    class_model_uri: ClassVar[URIRef] = SIO.Peer-reviewed


class WrittenLanguage(Language):
    """
    written language is a language that is communicated through a writing system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.WrittenLanguage
    class_class_curie: ClassVar[str] = "sio:WrittenLanguage"
    class_name: ClassVar[str] = "WrittenLanguage"
    class_model_uri: ClassVar[URIRef] = SIO.WrittenLanguage


class X-axis(CartesianCoordinateAxis):
    """
    An x-axis is a Cartesian coordinate axis that is aligned with the horizon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["X-axis"]
    class_class_curie: ClassVar[str] = "sio:X-axis"
    class_name: ClassVar[str] = "X-axis"
    class_model_uri: ClassVar[URIRef] = SIO.X-axis


class XCartesianCoordinate(CartesianCoordinate):
    """
    An x cartesian coordinate is the coordinate of an object onto the x-axis of a cartesian coordinate system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.XCartesianCoordinate
    class_class_curie: ClassVar[str] = "sio:XCartesianCoordinate"
    class_name: ClassVar[str] = "XCartesianCoordinate"
    class_model_uri: ClassVar[URIRef] = SIO.XCartesianCoordinate


class XenonAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.XenonAtom
    class_class_curie: ClassVar[str] = "sio:XenonAtom"
    class_name: ClassVar[str] = "XenonAtom"
    class_model_uri: ClassVar[URIRef] = SIO.XenonAtom


class Y-axis(CartesianCoordinateAxis):
    """
    A y-axis is a Cartesian coordinate axis that is spatially oriented perpendicular to the x-axis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Y-axis"]
    class_class_curie: ClassVar[str] = "sio:Y-axis"
    class_name: ClassVar[str] = "Y-axis"
    class_model_uri: ClassVar[URIRef] = SIO.Y-axis


class YCartesianCoordinate(CartesianCoordinate):
    """
    An y cartesian coordinate is the coordinate of an object onto the y-axis of a cartesian coordinate system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.YCartesianCoordinate
    class_class_curie: ClassVar[str] = "sio:YCartesianCoordinate"
    class_name: ClassVar[str] = "YCartesianCoordinate"
    class_model_uri: ClassVar[URIRef] = SIO.YCartesianCoordinate


class Year(TimeInterval):
    """
    A year is a period of time taken by a planet to make one revolution around the sun.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Year
    class_class_curie: ClassVar[str] = "sio:Year"
    class_name: ClassVar[str] = "Year"
    class_model_uri: ClassVar[URIRef] = SIO.Year


class YtterbiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.YtterbiumAtom
    class_class_curie: ClassVar[str] = "sio:YtterbiumAtom"
    class_name: ClassVar[str] = "YtterbiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.YtterbiumAtom


class YttriumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.YttriumAtom
    class_class_curie: ClassVar[str] = "sio:YttriumAtom"
    class_name: ClassVar[str] = "YttriumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.YttriumAtom


class Z-axis(CartesianCoordinateAxis):
    """
    A z-axis is a Cartesian coordinate axis that is spatially oriented normal to the plane formed by the x- and y-axes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["Z-axis"]
    class_class_curie: ClassVar[str] = "sio:Z-axis"
    class_name: ClassVar[str] = "Z-axis"
    class_model_uri: ClassVar[URIRef] = SIO.Z-axis


class ZCartesianCoordinate(CartesianCoordinate):
    """
    A z cartesian coordinate is the coordinate of an object onto the z-axis of a cartesian coordinate system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ZCartesianCoordinate
    class_class_curie: ClassVar[str] = "sio:ZCartesianCoordinate"
    class_name: ClassVar[str] = "ZCartesianCoordinate"
    class_model_uri: ClassVar[URIRef] = SIO.ZCartesianCoordinate


class ZincAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ZincAtom
    class_class_curie: ClassVar[str] = "sio:ZincAtom"
    class_name: ClassVar[str] = "ZincAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ZincAtom


class ZirconiumAtom(Atom):
    """
    None
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.ZirconiumAtom
    class_class_curie: ClassVar[str] = "sio:ZirconiumAtom"
    class_name: ClassVar[str] = "ZirconiumAtom"
    class_model_uri: ClassVar[URIRef] = SIO.ZirconiumAtom


class Zygosity(BiologicalQuality):
    """
    zygosity is the quality pertaining to the allelic complement of a biological system at a single locus on the DNA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Zygosity
    class_class_curie: ClassVar[str] = "sio:Zygosity"
    class_name: ClassVar[str] = "Zygosity"
    class_model_uri: ClassVar[URIRef] = SIO.Zygosity


class Hemizygous(Zygosity):
    """
    hemizygous is the quality of a biological organism in which, based on the ploidy of the organism, there is half
    the number of alleles than normal at a given locus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Hemizygous
    class_class_curie: ClassVar[str] = "sio:Hemizygous"
    class_name: ClassVar[str] = "Hemizygous"
    class_model_uri: ClassVar[URIRef] = SIO.Hemizygous


class Heterozygous(Zygosity):
    """
    homozygous is the quality of a biological organism in which there are two different alleles at a given locus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Heterozygous
    class_class_curie: ClassVar[str] = "sio:Heterozygous"
    class_name: ClassVar[str] = "Heterozygous"
    class_model_uri: ClassVar[URIRef] = SIO.Heterozygous


class Homozygous(Zygosity):
    """
    homozygous is the quality of a biological organism in which there are two identical alleles at a given locus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Homozygous
    class_class_curie: ClassVar[str] = "sio:Homozygous"
    class_name: ClassVar[str] = "Homozygous"
    class_model_uri: ClassVar[URIRef] = SIO.Homozygous


class Nullizygous(Zygosity):
    """
    nullizygous is the quality of a biological organism in which there are no allelles at a given locus.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO.Nullizygous
    class_class_curie: ClassVar[str] = "sio:Nullizygous"
    class_name: ClassVar[str] = "Nullizygous"
    class_model_uri: ClassVar[URIRef] = SIO.Nullizygous


# Enumerations


# Slots

