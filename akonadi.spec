#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi
Version  : 18.12.3
Release  : 11
URL      : https://download.kde.org/stable/applications/18.12.3/src/akonadi-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/akonadi-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/akonadi-18.12.3.tar.xz.sig
Summary  : PIM layer, which provides an asynchronous API to access all kind of PIM data
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: akonadi-bin = %{version}-%{release}
Requires: akonadi-data = %{version}-%{release}
Requires: akonadi-lib = %{version}-%{release}
Requires: akonadi-license = %{version}-%{release}
Requires: akonadi-locales = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : libxml2-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(sqlite3)
BuildRequires : qtbase-dev mesa-dev
Patch1: 0001-Fix-a-regression-when-updating-attributes.patch
Patch2: 0002-Fix-collection-detaching-at-the-wrong-time-in-attrib.patch

%description
Akonadi
========
What is Akonadi?
------------------
Akonadi is a PIM layer, which provides an asynchronous API to access all kind
of PIM data (e.g. mails, contacts, events, todos etc.).

%package bin
Summary: bin components for the akonadi package.
Group: Binaries
Requires: akonadi-data = %{version}-%{release}
Requires: akonadi-license = %{version}-%{release}

%description bin
bin components for the akonadi package.


%package data
Summary: data components for the akonadi package.
Group: Data

%description data
data components for the akonadi package.


%package dev
Summary: dev components for the akonadi package.
Group: Development
Requires: akonadi-lib = %{version}-%{release}
Requires: akonadi-bin = %{version}-%{release}
Requires: akonadi-data = %{version}-%{release}
Provides: akonadi-devel = %{version}-%{release}
Requires: akonadi = %{version}-%{release}

%description dev
dev components for the akonadi package.


%package lib
Summary: lib components for the akonadi package.
Group: Libraries
Requires: akonadi-data = %{version}-%{release}
Requires: akonadi-license = %{version}-%{release}

%description lib
lib components for the akonadi package.


%package license
Summary: license components for the akonadi package.
Group: Default

%description license
license components for the akonadi package.


%package locales
Summary: locales components for the akonadi package.
Group: Default

%description locales
locales components for the akonadi package.


%prep
%setup -q -n akonadi-18.12.3
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555313333
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1555313333
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadi/COPYING.LIB
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/akonadi/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang akonadi_knut_resource
%find_lang libakonadi5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/akonadi2xml
/usr/bin/akonadi_agent_launcher
/usr/bin/akonadi_agent_server
/usr/bin/akonadi_control
/usr/bin/akonadi_knut_resource
/usr/bin/akonadi_rds
/usr/bin/akonadictl
/usr/bin/akonadiselftest
/usr/bin/akonadiserver
/usr/bin/akonaditest
/usr/bin/asapcat

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/agents/knutresource.desktop
/usr/share/config.kcfg/resourcebase.kcfg
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Control.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Search.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.Agent.Status.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.AgentManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.ControlManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.DebugInterface.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.NotificationManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.NotificationSource.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.Preprocessor.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.Resource.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.Server.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.StorageDebugger.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.Tracer.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Akonadi.TracerNotification.xml
/usr/share/dbus-1/services/org.freedesktop.Akonadi.Control.service
/usr/share/icons/hicolor/128x128/apps/akonadi.png
/usr/share/icons/hicolor/16x16/apps/akonadi.png
/usr/share/icons/hicolor/22x22/apps/akonadi.png
/usr/share/icons/hicolor/256x256/apps/akonadi.png
/usr/share/icons/hicolor/32x32/apps/akonadi.png
/usr/share/icons/hicolor/48x48/apps/akonadi.png
/usr/share/icons/hicolor/64x64/apps/akonadi.png
/usr/share/icons/hicolor/scalable/apps/akonadi.svgz
/usr/share/kdevappwizard/templates/akonadiresource.tar.bz2
/usr/share/kdevappwizard/templates/akonadiserializer.tar.bz2
/usr/share/kf5/akonadi/akonadi-xml.xsd
/usr/share/kf5/akonadi/kcfg2dbus.xsl
/usr/share/kf5/akonadi_knut_resource/knut-template.xml
/usr/share/mime-packages/akonadi-mime.xml
/usr/share/xdg/akonadi.categories
/usr/share/xdg/akonadi.renamecategories
/usr/share/xdg/akonadi/mysql-global-mobile.conf
/usr/share/xdg/akonadi/mysql-global.conf

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/AkonadiAgentBase/AgentBase
/usr/include/KF5/AkonadiAgentBase/AgentSearchInterface
/usr/include/KF5/AkonadiAgentBase/PreprocessorBase
/usr/include/KF5/AkonadiAgentBase/ResourceBase
/usr/include/KF5/AkonadiAgentBase/ResourceSettings
/usr/include/KF5/AkonadiAgentBase/TransportResourceBase
/usr/include/KF5/AkonadiAgentBase/agentbase.h
/usr/include/KF5/AkonadiAgentBase/agentsearchinterface.h
/usr/include/KF5/AkonadiAgentBase/akonadiagentbase_export.h
/usr/include/KF5/AkonadiAgentBase/preprocessorbase.h
/usr/include/KF5/AkonadiAgentBase/resourcebase.h
/usr/include/KF5/AkonadiAgentBase/resourcebasesettings.h
/usr/include/KF5/AkonadiAgentBase/resourcesettings.h
/usr/include/KF5/AkonadiAgentBase/transportresourcebase.h
/usr/include/KF5/AkonadiCore/AbstractDifferencesReporter
/usr/include/KF5/AkonadiCore/AgentConfigurationBase
/usr/include/KF5/AkonadiCore/AgentConfigurationFactoryBase
/usr/include/KF5/AkonadiCore/AgentFilterProxyModel
/usr/include/KF5/AkonadiCore/AgentInstance
/usr/include/KF5/AkonadiCore/AgentInstanceCreateJob
/usr/include/KF5/AkonadiCore/AgentInstanceModel
/usr/include/KF5/AkonadiCore/AgentManager
/usr/include/KF5/AkonadiCore/AgentType
/usr/include/KF5/AkonadiCore/AgentTypeModel
/usr/include/KF5/AkonadiCore/Attribute
/usr/include/KF5/AkonadiCore/AttributeFactory
/usr/include/KF5/AkonadiCore/CachePolicy
/usr/include/KF5/AkonadiCore/ChangeNotification
/usr/include/KF5/AkonadiCore/ChangeRecorder
/usr/include/KF5/AkonadiCore/Collection
/usr/include/KF5/AkonadiCore/CollectionAttributesSynchronizationJob
/usr/include/KF5/AkonadiCore/CollectionColorAttribute
/usr/include/KF5/AkonadiCore/CollectionCopyJob
/usr/include/KF5/AkonadiCore/CollectionCreateJob
/usr/include/KF5/AkonadiCore/CollectionDeleteJob
/usr/include/KF5/AkonadiCore/CollectionFetchJob
/usr/include/KF5/AkonadiCore/CollectionFetchScope
/usr/include/KF5/AkonadiCore/CollectionFilterProxyModel
/usr/include/KF5/AkonadiCore/CollectionIdentificationAttribute
/usr/include/KF5/AkonadiCore/CollectionModifyJob
/usr/include/KF5/AkonadiCore/CollectionMoveJob
/usr/include/KF5/AkonadiCore/CollectionPathResolver
/usr/include/KF5/AkonadiCore/CollectionQuotaAttribute
/usr/include/KF5/AkonadiCore/CollectionStatistics
/usr/include/KF5/AkonadiCore/CollectionStatisticsJob
/usr/include/KF5/AkonadiCore/CollectionUtils
/usr/include/KF5/AkonadiCore/Control
/usr/include/KF5/AkonadiCore/DifferencesAlgorithmInterface
/usr/include/KF5/AkonadiCore/EntityAnnotationsAttribute
/usr/include/KF5/AkonadiCore/EntityDeletedAttribute
/usr/include/KF5/AkonadiCore/EntityDisplayAttribute
/usr/include/KF5/AkonadiCore/EntityHiddenAttribute
/usr/include/KF5/AkonadiCore/EntityMimeTypeFilterModel
/usr/include/KF5/AkonadiCore/EntityOrderProxyModel
/usr/include/KF5/AkonadiCore/EntityRightsFilterModel
/usr/include/KF5/AkonadiCore/EntityTreeModel
/usr/include/KF5/AkonadiCore/ExceptionBase
/usr/include/KF5/AkonadiCore/FavoriteCollectionAttribute
/usr/include/KF5/AkonadiCore/FavoriteCollectionsModel
/usr/include/KF5/AkonadiCore/GidExtractorInterface
/usr/include/KF5/AkonadiCore/IndexPolicyAttribute
/usr/include/KF5/AkonadiCore/Item
/usr/include/KF5/AkonadiCore/ItemCopyJob
/usr/include/KF5/AkonadiCore/ItemCreateJob
/usr/include/KF5/AkonadiCore/ItemDeleteJob
/usr/include/KF5/AkonadiCore/ItemFetchJob
/usr/include/KF5/AkonadiCore/ItemFetchScope
/usr/include/KF5/AkonadiCore/ItemModel
/usr/include/KF5/AkonadiCore/ItemModifyJob
/usr/include/KF5/AkonadiCore/ItemMonitor
/usr/include/KF5/AkonadiCore/ItemMoveJob
/usr/include/KF5/AkonadiCore/ItemSearchJob
/usr/include/KF5/AkonadiCore/ItemSerializerPlugin
/usr/include/KF5/AkonadiCore/ItemSync
/usr/include/KF5/AkonadiCore/Job
/usr/include/KF5/AkonadiCore/LinkJob
/usr/include/KF5/AkonadiCore/MimeTypeChecker
/usr/include/KF5/AkonadiCore/Monitor
/usr/include/KF5/AkonadiCore/NewMailNotifierAttribute
/usr/include/KF5/AkonadiCore/NotificationSubscriber
/usr/include/KF5/AkonadiCore/PartFetcher
/usr/include/KF5/AkonadiCore/PersistentSearchAttribute
/usr/include/KF5/AkonadiCore/Pop3ResourceAttribute
/usr/include/KF5/AkonadiCore/QuotaColorProxyModel
/usr/include/KF5/AkonadiCore/RecursiveCollectionFilterProxyModel
/usr/include/KF5/AkonadiCore/RecursiveItemFetchJob
/usr/include/KF5/AkonadiCore/Relation
/usr/include/KF5/AkonadiCore/RelationCreateJob
/usr/include/KF5/AkonadiCore/RelationDeleteJob
/usr/include/KF5/AkonadiCore/RelationFetchJob
/usr/include/KF5/AkonadiCore/ResourceSynchronizationJob
/usr/include/KF5/AkonadiCore/SearchCreateJob
/usr/include/KF5/AkonadiCore/SearchQuery
/usr/include/KF5/AkonadiCore/SelectionProxyModel
/usr/include/KF5/AkonadiCore/ServerManager
/usr/include/KF5/AkonadiCore/Session
/usr/include/KF5/AkonadiCore/SpecialCollectionAttribute
/usr/include/KF5/AkonadiCore/SpecialCollections
/usr/include/KF5/AkonadiCore/SpecialCollectionsDiscoveryJob
/usr/include/KF5/AkonadiCore/SpecialCollectionsRequestJob
/usr/include/KF5/AkonadiCore/StatisticsProxyModel
/usr/include/KF5/AkonadiCore/Supertrait
/usr/include/KF5/AkonadiCore/Tag
/usr/include/KF5/AkonadiCore/TagAttribute
/usr/include/KF5/AkonadiCore/TagCreateJob
/usr/include/KF5/AkonadiCore/TagDeleteJob
/usr/include/KF5/AkonadiCore/TagFetchJob
/usr/include/KF5/AkonadiCore/TagFetchScope
/usr/include/KF5/AkonadiCore/TagModel
/usr/include/KF5/AkonadiCore/TagModifyJob
/usr/include/KF5/AkonadiCore/TransactionJobs
/usr/include/KF5/AkonadiCore/TransactionSequence
/usr/include/KF5/AkonadiCore/TrashFilterProxyModel
/usr/include/KF5/AkonadiCore/TrashJob
/usr/include/KF5/AkonadiCore/TrashRestoreJob
/usr/include/KF5/AkonadiCore/TrashSettings
/usr/include/KF5/AkonadiCore/UnlinkJob
/usr/include/KF5/AkonadiCore/VectorHelper
/usr/include/KF5/AkonadiCore/abstractdifferencesreporter.h
/usr/include/KF5/AkonadiCore/agentconfigurationbase.h
/usr/include/KF5/AkonadiCore/agentconfigurationfactorybase.h
/usr/include/KF5/AkonadiCore/agentfilterproxymodel.h
/usr/include/KF5/AkonadiCore/agentinstance.h
/usr/include/KF5/AkonadiCore/agentinstancecreatejob.h
/usr/include/KF5/AkonadiCore/agentinstancemodel.h
/usr/include/KF5/AkonadiCore/agentmanager.h
/usr/include/KF5/AkonadiCore/agenttype.h
/usr/include/KF5/AkonadiCore/agenttypemodel.h
/usr/include/KF5/AkonadiCore/akonadicore_export.h
/usr/include/KF5/AkonadiCore/attribute.h
/usr/include/KF5/AkonadiCore/attributefactory.h
/usr/include/KF5/AkonadiCore/cachepolicy.h
/usr/include/KF5/AkonadiCore/changenotification.h
/usr/include/KF5/AkonadiCore/changerecorder.h
/usr/include/KF5/AkonadiCore/collection.h
/usr/include/KF5/AkonadiCore/collectionattributessynchronizationjob.h
/usr/include/KF5/AkonadiCore/collectioncolorattribute.h
/usr/include/KF5/AkonadiCore/collectioncopyjob.h
/usr/include/KF5/AkonadiCore/collectioncreatejob.h
/usr/include/KF5/AkonadiCore/collectiondeletejob.h
/usr/include/KF5/AkonadiCore/collectionfetchjob.h
/usr/include/KF5/AkonadiCore/collectionfetchscope.h
/usr/include/KF5/AkonadiCore/collectionfilterproxymodel.h
/usr/include/KF5/AkonadiCore/collectionidentificationattribute.h
/usr/include/KF5/AkonadiCore/collectionmodifyjob.h
/usr/include/KF5/AkonadiCore/collectionmovejob.h
/usr/include/KF5/AkonadiCore/collectionpathresolver.h
/usr/include/KF5/AkonadiCore/collectionquotaattribute.h
/usr/include/KF5/AkonadiCore/collectionstatistics.h
/usr/include/KF5/AkonadiCore/collectionstatisticsjob.h
/usr/include/KF5/AkonadiCore/collectionutils.h
/usr/include/KF5/AkonadiCore/control.h
/usr/include/KF5/AkonadiCore/differencesalgorithminterface.h
/usr/include/KF5/AkonadiCore/entityannotationsattribute.h
/usr/include/KF5/AkonadiCore/entitydeletedattribute.h
/usr/include/KF5/AkonadiCore/entitydisplayattribute.h
/usr/include/KF5/AkonadiCore/entityhiddenattribute.h
/usr/include/KF5/AkonadiCore/entitymimetypefiltermodel.h
/usr/include/KF5/AkonadiCore/entityorderproxymodel.h
/usr/include/KF5/AkonadiCore/entityrightsfiltermodel.h
/usr/include/KF5/AkonadiCore/entitytreemodel.h
/usr/include/KF5/AkonadiCore/exceptionbase.h
/usr/include/KF5/AkonadiCore/favoritecollectionattribute.h
/usr/include/KF5/AkonadiCore/favoritecollectionsmodel.h
/usr/include/KF5/AkonadiCore/gidextractorinterface.h
/usr/include/KF5/AkonadiCore/indexpolicyattribute.h
/usr/include/KF5/AkonadiCore/item.h
/usr/include/KF5/AkonadiCore/itemcopyjob.h
/usr/include/KF5/AkonadiCore/itemcreatejob.h
/usr/include/KF5/AkonadiCore/itemdeletejob.h
/usr/include/KF5/AkonadiCore/itemfetchjob.h
/usr/include/KF5/AkonadiCore/itemfetchscope.h
/usr/include/KF5/AkonadiCore/itemmodel.h
/usr/include/KF5/AkonadiCore/itemmodifyjob.h
/usr/include/KF5/AkonadiCore/itemmonitor.h
/usr/include/KF5/AkonadiCore/itemmovejob.h
/usr/include/KF5/AkonadiCore/itempayloadinternals_p.h
/usr/include/KF5/AkonadiCore/itemsearchjob.h
/usr/include/KF5/AkonadiCore/itemserializerplugin.h
/usr/include/KF5/AkonadiCore/itemsync.h
/usr/include/KF5/AkonadiCore/job.h
/usr/include/KF5/AkonadiCore/linkjob.h
/usr/include/KF5/AkonadiCore/mimetypechecker.h
/usr/include/KF5/AkonadiCore/monitor.h
/usr/include/KF5/AkonadiCore/newmailnotifierattribute.h
/usr/include/KF5/AkonadiCore/notificationsubscriber.h
/usr/include/KF5/AkonadiCore/partfetcher.h
/usr/include/KF5/AkonadiCore/persistentsearchattribute.h
/usr/include/KF5/AkonadiCore/pop3resourceattribute.h
/usr/include/KF5/AkonadiCore/qtest_akonadi.h
/usr/include/KF5/AkonadiCore/quotacolorproxymodel.h
/usr/include/KF5/AkonadiCore/recursivecollectionfilterproxymodel.h
/usr/include/KF5/AkonadiCore/recursiveitemfetchjob.h
/usr/include/KF5/AkonadiCore/relation.h
/usr/include/KF5/AkonadiCore/relationcreatejob.h
/usr/include/KF5/AkonadiCore/relationdeletejob.h
/usr/include/KF5/AkonadiCore/relationfetchjob.h
/usr/include/KF5/AkonadiCore/resourcesynchronizationjob.h
/usr/include/KF5/AkonadiCore/searchcreatejob.h
/usr/include/KF5/AkonadiCore/searchquery.h
/usr/include/KF5/AkonadiCore/selectionproxymodel.h
/usr/include/KF5/AkonadiCore/servermanager.h
/usr/include/KF5/AkonadiCore/session.h
/usr/include/KF5/AkonadiCore/specialcollectionattribute.h
/usr/include/KF5/AkonadiCore/specialcollections.h
/usr/include/KF5/AkonadiCore/specialcollectionsdiscoveryjob.h
/usr/include/KF5/AkonadiCore/specialcollectionsrequestjob.h
/usr/include/KF5/AkonadiCore/statisticsproxymodel.h
/usr/include/KF5/AkonadiCore/supertrait.h
/usr/include/KF5/AkonadiCore/tag.h
/usr/include/KF5/AkonadiCore/tagattribute.h
/usr/include/KF5/AkonadiCore/tagcreatejob.h
/usr/include/KF5/AkonadiCore/tagdeletejob.h
/usr/include/KF5/AkonadiCore/tagfetchjob.h
/usr/include/KF5/AkonadiCore/tagfetchscope.h
/usr/include/KF5/AkonadiCore/tagmodel.h
/usr/include/KF5/AkonadiCore/tagmodifyjob.h
/usr/include/KF5/AkonadiCore/transactionjobs.h
/usr/include/KF5/AkonadiCore/transactionsequence.h
/usr/include/KF5/AkonadiCore/trashfilterproxymodel.h
/usr/include/KF5/AkonadiCore/trashjob.h
/usr/include/KF5/AkonadiCore/trashrestorejob.h
/usr/include/KF5/AkonadiCore/trashsettings.h
/usr/include/KF5/AkonadiCore/unlinkjob.h
/usr/include/KF5/AkonadiCore/vectorhelper.h
/usr/include/KF5/AkonadiWidgets/AgentActionManager
/usr/include/KF5/AkonadiWidgets/AgentConfigurationDialog
/usr/include/KF5/AkonadiWidgets/AgentConfigurationWidget
/usr/include/KF5/AkonadiWidgets/AgentInstanceWidget
/usr/include/KF5/AkonadiWidgets/AgentTypeDialog
/usr/include/KF5/AkonadiWidgets/AgentTypeWidget
/usr/include/KF5/AkonadiWidgets/CollectionComboBox
/usr/include/KF5/AkonadiWidgets/CollectionDialog
/usr/include/KF5/AkonadiWidgets/CollectionMaintenancePage
/usr/include/KF5/AkonadiWidgets/CollectionPropertiesDialog
/usr/include/KF5/AkonadiWidgets/CollectionPropertiesPage
/usr/include/KF5/AkonadiWidgets/CollectionRequester
/usr/include/KF5/AkonadiWidgets/CollectionStatisticsDelegate
/usr/include/KF5/AkonadiWidgets/CollectionView
/usr/include/KF5/AkonadiWidgets/ControlGui
/usr/include/KF5/AkonadiWidgets/ETMViewStateSaver
/usr/include/KF5/AkonadiWidgets/EntityListView
/usr/include/KF5/AkonadiWidgets/EntityTreeView
/usr/include/KF5/AkonadiWidgets/ItemView
/usr/include/KF5/AkonadiWidgets/ManageAccountWidget
/usr/include/KF5/AkonadiWidgets/RenameFavoriteDialog
/usr/include/KF5/AkonadiWidgets/StandardActionManager
/usr/include/KF5/AkonadiWidgets/SubscriptionDialog
/usr/include/KF5/AkonadiWidgets/TagEditWidget
/usr/include/KF5/AkonadiWidgets/TagManagementDialog
/usr/include/KF5/AkonadiWidgets/TagSelectWidget
/usr/include/KF5/AkonadiWidgets/TagSelectionDialog
/usr/include/KF5/AkonadiWidgets/TagWidget
/usr/include/KF5/AkonadiWidgets/agentactionmanager.h
/usr/include/KF5/AkonadiWidgets/agentconfigurationdialog.h
/usr/include/KF5/AkonadiWidgets/agentconfigurationwidget.h
/usr/include/KF5/AkonadiWidgets/agentinstancewidget.h
/usr/include/KF5/AkonadiWidgets/agenttypedialog.h
/usr/include/KF5/AkonadiWidgets/agenttypewidget.h
/usr/include/KF5/AkonadiWidgets/akonadiwidgets_export.h
/usr/include/KF5/AkonadiWidgets/collectioncombobox.h
/usr/include/KF5/AkonadiWidgets/collectiondialog.h
/usr/include/KF5/AkonadiWidgets/collectionmaintenancepage.h
/usr/include/KF5/AkonadiWidgets/collectionpropertiesdialog.h
/usr/include/KF5/AkonadiWidgets/collectionpropertiespage.h
/usr/include/KF5/AkonadiWidgets/collectionrequester.h
/usr/include/KF5/AkonadiWidgets/collectionstatisticsdelegate.h
/usr/include/KF5/AkonadiWidgets/collectionview.h
/usr/include/KF5/AkonadiWidgets/controlgui.h
/usr/include/KF5/AkonadiWidgets/entitylistview.h
/usr/include/KF5/AkonadiWidgets/entitytreeview.h
/usr/include/KF5/AkonadiWidgets/etmviewstatesaver.h
/usr/include/KF5/AkonadiWidgets/itemview.h
/usr/include/KF5/AkonadiWidgets/manageaccountwidget.h
/usr/include/KF5/AkonadiWidgets/renamefavoritedialog.h
/usr/include/KF5/AkonadiWidgets/standardactionmanager.h
/usr/include/KF5/AkonadiWidgets/subscriptiondialog.h
/usr/include/KF5/AkonadiWidgets/tageditwidget.h
/usr/include/KF5/AkonadiWidgets/tagmanagementdialog.h
/usr/include/KF5/AkonadiWidgets/tagselectiondialog.h
/usr/include/KF5/AkonadiWidgets/tagselectwidget.h
/usr/include/KF5/AkonadiWidgets/tagwidget.h
/usr/include/KF5/AkonadiXml/XmlDocument
/usr/include/KF5/AkonadiXml/XmlReader
/usr/include/KF5/AkonadiXml/XmlWriteJob
/usr/include/KF5/AkonadiXml/XmlWriter
/usr/include/KF5/AkonadiXml/akonadi-xml_export.h
/usr/include/KF5/AkonadiXml/xmldocument.h
/usr/include/KF5/AkonadiXml/xmlreader.h
/usr/include/KF5/AkonadiXml/xmlwritejob.h
/usr/include/KF5/AkonadiXml/xmlwriter.h
/usr/include/KF5/akonadi/abstractsearchplugin.h
/usr/include/KF5/akonadi/private/akonadiprivate_export.h
/usr/include/KF5/akonadi/private/capabilities_p.h
/usr/include/KF5/akonadi/private/dbus_p.h
/usr/include/KF5/akonadi/private/externalpartstorage_p.h
/usr/include/KF5/akonadi/private/imapparser_p.h
/usr/include/KF5/akonadi/private/imapset_p.h
/usr/include/KF5/akonadi/private/instance_p.h
/usr/include/KF5/akonadi/private/protocol_exception_p.h
/usr/include/KF5/akonadi/private/protocol_gen.h
/usr/include/KF5/akonadi/private/protocol_p.h
/usr/include/KF5/akonadi/private/scope_p.h
/usr/include/KF5/akonadi/private/standarddirs_p.h
/usr/include/KF5/akonadi/private/tristate_p.h
/usr/include/KF5/akonadi_version.h
/usr/lib64/cmake/KF5Akonadi/KF5AkonadiConfig.cmake
/usr/lib64/cmake/KF5Akonadi/KF5AkonadiConfigVersion.cmake
/usr/lib64/cmake/KF5Akonadi/KF5AkonadiMacros.cmake
/usr/lib64/cmake/KF5Akonadi/KF5AkonadiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Akonadi/KF5AkonadiTargets.cmake
/usr/lib64/libKF5AkonadiAgentBase.so
/usr/lib64/libKF5AkonadiCore.so
/usr/lib64/libKF5AkonadiPrivate.so
/usr/lib64/libKF5AkonadiWidgets.so
/usr/lib64/libKF5AkonadiXml.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiAgentBase.pri
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiCore.pri
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiWidgets.pri
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiXml.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiAgentBase.so.5
/usr/lib64/libKF5AkonadiAgentBase.so.5.10.3
/usr/lib64/libKF5AkonadiCore.so.5
/usr/lib64/libKF5AkonadiCore.so.5.10.3
/usr/lib64/libKF5AkonadiPrivate.so.5
/usr/lib64/libKF5AkonadiPrivate.so.5.10.3
/usr/lib64/libKF5AkonadiWidgets.so.5
/usr/lib64/libKF5AkonadiWidgets.so.5.10.3
/usr/lib64/libKF5AkonadiXml.so.5
/usr/lib64/libKF5AkonadiXml.so.5.10.3
/usr/lib64/qt5/plugins/akonadi/akonadi_test_searchplugin.so
/usr/lib64/qt5/plugins/designer/akonadi5widgets.so
/usr/lib64/qt5/plugins/sqldrivers/libqsqlite3.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi/COPYING.LIB
/usr/share/package-licenses/akonadi/cmake_modules_COPYING-CMAKE-SCRIPTS

%files locales -f akonadi_knut_resource.lang -f libakonadi5.lang
%defattr(-,root,root,-)

