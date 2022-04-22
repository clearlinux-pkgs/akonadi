#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi
Version  : 22.04.0
Release  : 62
URL      : https://download.kde.org/stable/release-service/22.04.0/src/akonadi-22.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.0/src/akonadi-22.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.0/src/akonadi-22.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT
Requires: akonadi-bin = %{version}-%{release}
Requires: akonadi-data = %{version}-%{release}
Requires: akonadi-lib = %{version}-%{release}
Requires: akonadi-license = %{version}-%{release}
Requires: akonadi-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kitemviews-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : kxmlgui-dev
BuildRequires : libxml2-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(sqlite3)
BuildRequires : xz-dev

%description
This is a sliglty adjusted version of the QSQLITE driver. Install this driver
somewhere in the QT_PLUGIN_PATH and use it in akonadi by setting the driver
to QSQLITE3.

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
%setup -q -n akonadi-22.04.0
cd %{_builddir}/akonadi-22.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650662015
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1650662015
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi
cp %{_builddir}/akonadi-22.04.0/.krazy.license %{buildroot}/usr/share/package-licenses/akonadi/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
cp %{_builddir}/akonadi-22.04.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/akonadi-22.04.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/akonadi-22.04.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/akonadi-22.04.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/akonadi-22.04.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/akonadi-22.04.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/akonadi-22.04.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/akonadi-22.04.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/akonadi/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/akonadi-22.04.0/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/akonadi-22.04.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadi/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/akonadi-22.04.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/akonadi/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/akonadi-22.04.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/akonadi/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
cp %{_builddir}/akonadi-22.04.0/README.md.license %{buildroot}/usr/share/package-licenses/akonadi/cadc9e08cb956c041f87922de84b9206d9bbffb2
cp %{_builddir}/akonadi-22.04.0/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
cp %{_builddir}/akonadi-22.04.0/src/.krazy.license %{buildroot}/usr/share/package-licenses/akonadi/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
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
/usr/share/kf5/akonadi/akonadi-xml.xsd
/usr/share/kf5/akonadi/kcfg2dbus.xsl
/usr/share/kf5/akonadi_knut_resource/knut-template.xml
/usr/share/mime-packages/akonadi-mime.xml
/usr/share/qlogging-categories5/akonadi.categories
/usr/share/qlogging-categories5/akonadi.renamecategories
/usr/share/xdg/akonadi/mysql-global-mobile.conf
/usr/share/xdg/akonadi/mysql-global.conf

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Akonadi/akonadi/private/akonadiprivate_export.h
/usr/include/KF5/Akonadi/akonadi/private/capabilities_p.h
/usr/include/KF5/Akonadi/akonadi/private/compressionstream_p.h
/usr/include/KF5/Akonadi/akonadi/private/dbus_p.h
/usr/include/KF5/Akonadi/akonadi/private/externalpartstorage_p.h
/usr/include/KF5/Akonadi/akonadi/private/imapparser_p.h
/usr/include/KF5/Akonadi/akonadi/private/imapset_p.h
/usr/include/KF5/Akonadi/akonadi/private/instance_p.h
/usr/include/KF5/Akonadi/akonadi/private/protocol_exception_p.h
/usr/include/KF5/Akonadi/akonadi/private/protocol_gen.h
/usr/include/KF5/Akonadi/akonadi/private/protocol_p.h
/usr/include/KF5/Akonadi/akonadi/private/scope_p.h
/usr/include/KF5/Akonadi/akonadi/private/standarddirs_p.h
/usr/include/KF5/Akonadi/akonadi/private/tristate_p.h
/usr/include/KF5/AkonadiAgentBase/Akonadi/AccountsIntegration
/usr/include/KF5/AkonadiAgentBase/Akonadi/AgentBase
/usr/include/KF5/AkonadiAgentBase/Akonadi/AgentSearchInterface
/usr/include/KF5/AkonadiAgentBase/Akonadi/PreprocessorBase
/usr/include/KF5/AkonadiAgentBase/Akonadi/ResourceBase
/usr/include/KF5/AkonadiAgentBase/Akonadi/ResourceSettings
/usr/include/KF5/AkonadiAgentBase/Akonadi/TransportResourceBase
/usr/include/KF5/AkonadiAgentBase/akonadi/accountsintegration.h
/usr/include/KF5/AkonadiAgentBase/akonadi/agentbase.h
/usr/include/KF5/AkonadiAgentBase/akonadi/agentsearchinterface.h
/usr/include/KF5/AkonadiAgentBase/akonadi/akonadiagentbase_export.h
/usr/include/KF5/AkonadiAgentBase/akonadi/preprocessorbase.h
/usr/include/KF5/AkonadiAgentBase/akonadi/resourcebase.h
/usr/include/KF5/AkonadiAgentBase/akonadi/resourcebasesettings.h
/usr/include/KF5/AkonadiAgentBase/akonadi/resourcesettings.h
/usr/include/KF5/AkonadiAgentBase/akonadi/transportresourcebase.h
/usr/include/KF5/AkonadiCore/Akonadi/AbstractDifferencesReporter
/usr/include/KF5/AkonadiCore/Akonadi/AgentConfigurationBase
/usr/include/KF5/AkonadiCore/Akonadi/AgentConfigurationFactoryBase
/usr/include/KF5/AkonadiCore/Akonadi/AgentFilterProxyModel
/usr/include/KF5/AkonadiCore/Akonadi/AgentInstance
/usr/include/KF5/AkonadiCore/Akonadi/AgentInstanceCreateJob
/usr/include/KF5/AkonadiCore/Akonadi/AgentInstanceModel
/usr/include/KF5/AkonadiCore/Akonadi/AgentManager
/usr/include/KF5/AkonadiCore/Akonadi/AgentType
/usr/include/KF5/AkonadiCore/Akonadi/AgentTypeModel
/usr/include/KF5/AkonadiCore/Akonadi/Attribute
/usr/include/KF5/AkonadiCore/Akonadi/AttributeFactory
/usr/include/KF5/AkonadiCore/Akonadi/CachePolicy
/usr/include/KF5/AkonadiCore/Akonadi/ChangeNotification
/usr/include/KF5/AkonadiCore/Akonadi/ChangeRecorder
/usr/include/KF5/AkonadiCore/Akonadi/Collection
/usr/include/KF5/AkonadiCore/Akonadi/CollectionAttributesSynchronizationJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionColorAttribute
/usr/include/KF5/AkonadiCore/Akonadi/CollectionCopyJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionCreateJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionDeleteJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionFetchJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionFetchScope
/usr/include/KF5/AkonadiCore/Akonadi/CollectionFilterProxyModel
/usr/include/KF5/AkonadiCore/Akonadi/CollectionIdentificationAttribute
/usr/include/KF5/AkonadiCore/Akonadi/CollectionModifyJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionMoveJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionPathResolver
/usr/include/KF5/AkonadiCore/Akonadi/CollectionQuotaAttribute
/usr/include/KF5/AkonadiCore/Akonadi/CollectionStatistics
/usr/include/KF5/AkonadiCore/Akonadi/CollectionStatisticsJob
/usr/include/KF5/AkonadiCore/Akonadi/CollectionUtils
/usr/include/KF5/AkonadiCore/Akonadi/Control
/usr/include/KF5/AkonadiCore/Akonadi/DifferencesAlgorithmInterface
/usr/include/KF5/AkonadiCore/Akonadi/EntityAnnotationsAttribute
/usr/include/KF5/AkonadiCore/Akonadi/EntityDeletedAttribute
/usr/include/KF5/AkonadiCore/Akonadi/EntityDisplayAttribute
/usr/include/KF5/AkonadiCore/Akonadi/EntityHiddenAttribute
/usr/include/KF5/AkonadiCore/Akonadi/EntityMimeTypeFilterModel
/usr/include/KF5/AkonadiCore/Akonadi/EntityOrderProxyModel
/usr/include/KF5/AkonadiCore/Akonadi/EntityRightsFilterModel
/usr/include/KF5/AkonadiCore/Akonadi/EntityTreeModel
/usr/include/KF5/AkonadiCore/Akonadi/ExceptionBase
/usr/include/KF5/AkonadiCore/Akonadi/FavoriteCollectionAttribute
/usr/include/KF5/AkonadiCore/Akonadi/FavoriteCollectionsModel
/usr/include/KF5/AkonadiCore/Akonadi/GidExtractorInterface
/usr/include/KF5/AkonadiCore/Akonadi/IndexPolicyAttribute
/usr/include/KF5/AkonadiCore/Akonadi/Item
/usr/include/KF5/AkonadiCore/Akonadi/ItemCopyJob
/usr/include/KF5/AkonadiCore/Akonadi/ItemCreateJob
/usr/include/KF5/AkonadiCore/Akonadi/ItemDeleteJob
/usr/include/KF5/AkonadiCore/Akonadi/ItemFetchJob
/usr/include/KF5/AkonadiCore/Akonadi/ItemFetchScope
/usr/include/KF5/AkonadiCore/Akonadi/ItemModifyJob
/usr/include/KF5/AkonadiCore/Akonadi/ItemMonitor
/usr/include/KF5/AkonadiCore/Akonadi/ItemMoveJob
/usr/include/KF5/AkonadiCore/Akonadi/ItemSearchJob
/usr/include/KF5/AkonadiCore/Akonadi/ItemSerializerPlugin
/usr/include/KF5/AkonadiCore/Akonadi/ItemSync
/usr/include/KF5/AkonadiCore/Akonadi/Job
/usr/include/KF5/AkonadiCore/Akonadi/LinkJob
/usr/include/KF5/AkonadiCore/Akonadi/MimeTypeChecker
/usr/include/KF5/AkonadiCore/Akonadi/Monitor
/usr/include/KF5/AkonadiCore/Akonadi/NotificationSubscriber
/usr/include/KF5/AkonadiCore/Akonadi/PartFetcher
/usr/include/KF5/AkonadiCore/Akonadi/PersistentSearchAttribute
/usr/include/KF5/AkonadiCore/Akonadi/RecursiveCollectionFilterProxyModel
/usr/include/KF5/AkonadiCore/Akonadi/RecursiveItemFetchJob
/usr/include/KF5/AkonadiCore/Akonadi/Relation
/usr/include/KF5/AkonadiCore/Akonadi/RelationCreateJob
/usr/include/KF5/AkonadiCore/Akonadi/RelationDeleteJob
/usr/include/KF5/AkonadiCore/Akonadi/RelationFetchJob
/usr/include/KF5/AkonadiCore/Akonadi/ResourceSynchronizationJob
/usr/include/KF5/AkonadiCore/Akonadi/SearchCreateJob
/usr/include/KF5/AkonadiCore/Akonadi/SearchQuery
/usr/include/KF5/AkonadiCore/Akonadi/SelectionProxyModel
/usr/include/KF5/AkonadiCore/Akonadi/ServerManager
/usr/include/KF5/AkonadiCore/Akonadi/Session
/usr/include/KF5/AkonadiCore/Akonadi/SpecialCollectionAttribute
/usr/include/KF5/AkonadiCore/Akonadi/SpecialCollections
/usr/include/KF5/AkonadiCore/Akonadi/SpecialCollectionsDiscoveryJob
/usr/include/KF5/AkonadiCore/Akonadi/SpecialCollectionsRequestJob
/usr/include/KF5/AkonadiCore/Akonadi/StatisticsProxyModel
/usr/include/KF5/AkonadiCore/Akonadi/Supertrait
/usr/include/KF5/AkonadiCore/Akonadi/Tag
/usr/include/KF5/AkonadiCore/Akonadi/TagAttribute
/usr/include/KF5/AkonadiCore/Akonadi/TagCreateJob
/usr/include/KF5/AkonadiCore/Akonadi/TagDeleteJob
/usr/include/KF5/AkonadiCore/Akonadi/TagFetchJob
/usr/include/KF5/AkonadiCore/Akonadi/TagFetchScope
/usr/include/KF5/AkonadiCore/Akonadi/TagModel
/usr/include/KF5/AkonadiCore/Akonadi/TagModifyJob
/usr/include/KF5/AkonadiCore/Akonadi/TransactionJobs
/usr/include/KF5/AkonadiCore/Akonadi/TransactionSequence
/usr/include/KF5/AkonadiCore/Akonadi/TrashFilterProxyModel
/usr/include/KF5/AkonadiCore/Akonadi/TrashJob
/usr/include/KF5/AkonadiCore/Akonadi/TrashRestoreJob
/usr/include/KF5/AkonadiCore/Akonadi/TrashSettings
/usr/include/KF5/AkonadiCore/Akonadi/UnlinkJob
/usr/include/KF5/AkonadiCore/Akonadi/VectorHelper
/usr/include/KF5/AkonadiCore/akonadi/abstractdifferencesreporter.h
/usr/include/KF5/AkonadiCore/akonadi/abstractsearchplugin.h
/usr/include/KF5/AkonadiCore/akonadi/agentconfigurationbase.h
/usr/include/KF5/AkonadiCore/akonadi/agentconfigurationfactorybase.h
/usr/include/KF5/AkonadiCore/akonadi/agentfilterproxymodel.h
/usr/include/KF5/AkonadiCore/akonadi/agentinstance.h
/usr/include/KF5/AkonadiCore/akonadi/agentinstancecreatejob.h
/usr/include/KF5/AkonadiCore/akonadi/agentinstancemodel.h
/usr/include/KF5/AkonadiCore/akonadi/agentmanager.h
/usr/include/KF5/AkonadiCore/akonadi/agenttype.h
/usr/include/KF5/AkonadiCore/akonadi/agenttypemodel.h
/usr/include/KF5/AkonadiCore/akonadi/akonadicore_export.h
/usr/include/KF5/AkonadiCore/akonadi/attribute.h
/usr/include/KF5/AkonadiCore/akonadi/attributefactory.h
/usr/include/KF5/AkonadiCore/akonadi/cachepolicy.h
/usr/include/KF5/AkonadiCore/akonadi/changenotification.h
/usr/include/KF5/AkonadiCore/akonadi/changerecorder.h
/usr/include/KF5/AkonadiCore/akonadi/collection.h
/usr/include/KF5/AkonadiCore/akonadi/collectionattributessynchronizationjob.h
/usr/include/KF5/AkonadiCore/akonadi/collectioncolorattribute.h
/usr/include/KF5/AkonadiCore/akonadi/collectioncopyjob.h
/usr/include/KF5/AkonadiCore/akonadi/collectioncreatejob.h
/usr/include/KF5/AkonadiCore/akonadi/collectiondeletejob.h
/usr/include/KF5/AkonadiCore/akonadi/collectionfetchjob.h
/usr/include/KF5/AkonadiCore/akonadi/collectionfetchscope.h
/usr/include/KF5/AkonadiCore/akonadi/collectionfilterproxymodel.h
/usr/include/KF5/AkonadiCore/akonadi/collectionidentificationattribute.h
/usr/include/KF5/AkonadiCore/akonadi/collectionmodifyjob.h
/usr/include/KF5/AkonadiCore/akonadi/collectionmovejob.h
/usr/include/KF5/AkonadiCore/akonadi/collectionpathresolver.h
/usr/include/KF5/AkonadiCore/akonadi/collectionquotaattribute.h
/usr/include/KF5/AkonadiCore/akonadi/collectionstatistics.h
/usr/include/KF5/AkonadiCore/akonadi/collectionstatisticsjob.h
/usr/include/KF5/AkonadiCore/akonadi/collectionutils.h
/usr/include/KF5/AkonadiCore/akonadi/config-akonadi.h
/usr/include/KF5/AkonadiCore/akonadi/control.h
/usr/include/KF5/AkonadiCore/akonadi/differencesalgorithminterface.h
/usr/include/KF5/AkonadiCore/akonadi/entityannotationsattribute.h
/usr/include/KF5/AkonadiCore/akonadi/entitydeletedattribute.h
/usr/include/KF5/AkonadiCore/akonadi/entitydisplayattribute.h
/usr/include/KF5/AkonadiCore/akonadi/entityhiddenattribute.h
/usr/include/KF5/AkonadiCore/akonadi/entitymimetypefiltermodel.h
/usr/include/KF5/AkonadiCore/akonadi/entityorderproxymodel.h
/usr/include/KF5/AkonadiCore/akonadi/entityrightsfiltermodel.h
/usr/include/KF5/AkonadiCore/akonadi/entitytreemodel.h
/usr/include/KF5/AkonadiCore/akonadi/exceptionbase.h
/usr/include/KF5/AkonadiCore/akonadi/favoritecollectionattribute.h
/usr/include/KF5/AkonadiCore/akonadi/favoritecollectionsmodel.h
/usr/include/KF5/AkonadiCore/akonadi/gidextractorinterface.h
/usr/include/KF5/AkonadiCore/akonadi/indexpolicyattribute.h
/usr/include/KF5/AkonadiCore/akonadi/item.h
/usr/include/KF5/AkonadiCore/akonadi/itemcopyjob.h
/usr/include/KF5/AkonadiCore/akonadi/itemcreatejob.h
/usr/include/KF5/AkonadiCore/akonadi/itemdeletejob.h
/usr/include/KF5/AkonadiCore/akonadi/itemfetchjob.h
/usr/include/KF5/AkonadiCore/akonadi/itemfetchscope.h
/usr/include/KF5/AkonadiCore/akonadi/itemmodifyjob.h
/usr/include/KF5/AkonadiCore/akonadi/itemmonitor.h
/usr/include/KF5/AkonadiCore/akonadi/itemmovejob.h
/usr/include/KF5/AkonadiCore/akonadi/itempayloadinternals_p.h
/usr/include/KF5/AkonadiCore/akonadi/itemsearchjob.h
/usr/include/KF5/AkonadiCore/akonadi/itemserializerplugin.h
/usr/include/KF5/AkonadiCore/akonadi/itemsync.h
/usr/include/KF5/AkonadiCore/akonadi/job.h
/usr/include/KF5/AkonadiCore/akonadi/linkjob.h
/usr/include/KF5/AkonadiCore/akonadi/mimetypechecker.h
/usr/include/KF5/AkonadiCore/akonadi/monitor.h
/usr/include/KF5/AkonadiCore/akonadi/notificationsubscriber.h
/usr/include/KF5/AkonadiCore/akonadi/partfetcher.h
/usr/include/KF5/AkonadiCore/akonadi/persistentsearchattribute.h
/usr/include/KF5/AkonadiCore/akonadi/qtest_akonadi.h
/usr/include/KF5/AkonadiCore/akonadi/recursivecollectionfilterproxymodel.h
/usr/include/KF5/AkonadiCore/akonadi/recursiveitemfetchjob.h
/usr/include/KF5/AkonadiCore/akonadi/relation.h
/usr/include/KF5/AkonadiCore/akonadi/relationcreatejob.h
/usr/include/KF5/AkonadiCore/akonadi/relationdeletejob.h
/usr/include/KF5/AkonadiCore/akonadi/relationfetchjob.h
/usr/include/KF5/AkonadiCore/akonadi/resourcesynchronizationjob.h
/usr/include/KF5/AkonadiCore/akonadi/searchcreatejob.h
/usr/include/KF5/AkonadiCore/akonadi/searchquery.h
/usr/include/KF5/AkonadiCore/akonadi/selectionproxymodel.h
/usr/include/KF5/AkonadiCore/akonadi/servermanager.h
/usr/include/KF5/AkonadiCore/akonadi/session.h
/usr/include/KF5/AkonadiCore/akonadi/specialcollectionattribute.h
/usr/include/KF5/AkonadiCore/akonadi/specialcollections.h
/usr/include/KF5/AkonadiCore/akonadi/specialcollectionsdiscoveryjob.h
/usr/include/KF5/AkonadiCore/akonadi/specialcollectionsrequestjob.h
/usr/include/KF5/AkonadiCore/akonadi/statisticsproxymodel.h
/usr/include/KF5/AkonadiCore/akonadi/supertrait.h
/usr/include/KF5/AkonadiCore/akonadi/tag.h
/usr/include/KF5/AkonadiCore/akonadi/tagattribute.h
/usr/include/KF5/AkonadiCore/akonadi/tagcreatejob.h
/usr/include/KF5/AkonadiCore/akonadi/tagdeletejob.h
/usr/include/KF5/AkonadiCore/akonadi/tagfetchjob.h
/usr/include/KF5/AkonadiCore/akonadi/tagfetchscope.h
/usr/include/KF5/AkonadiCore/akonadi/tagmodel.h
/usr/include/KF5/AkonadiCore/akonadi/tagmodifyjob.h
/usr/include/KF5/AkonadiCore/akonadi/transactionjobs.h
/usr/include/KF5/AkonadiCore/akonadi/transactionsequence.h
/usr/include/KF5/AkonadiCore/akonadi/trashfilterproxymodel.h
/usr/include/KF5/AkonadiCore/akonadi/trashjob.h
/usr/include/KF5/AkonadiCore/akonadi/trashrestorejob.h
/usr/include/KF5/AkonadiCore/akonadi/trashsettings.h
/usr/include/KF5/AkonadiCore/akonadi/unlinkjob.h
/usr/include/KF5/AkonadiCore/akonadi/vectorhelper.h
/usr/include/KF5/AkonadiWidgets/Akonadi/AgentActionManager
/usr/include/KF5/AkonadiWidgets/Akonadi/AgentConfigurationDialog
/usr/include/KF5/AkonadiWidgets/Akonadi/AgentConfigurationWidget
/usr/include/KF5/AkonadiWidgets/Akonadi/AgentInstanceWidget
/usr/include/KF5/AkonadiWidgets/Akonadi/AgentTypeDialog
/usr/include/KF5/AkonadiWidgets/Akonadi/AgentTypeWidget
/usr/include/KF5/AkonadiWidgets/Akonadi/CollectionComboBox
/usr/include/KF5/AkonadiWidgets/Akonadi/CollectionDialog
/usr/include/KF5/AkonadiWidgets/Akonadi/CollectionMaintenancePage
/usr/include/KF5/AkonadiWidgets/Akonadi/CollectionPropertiesDialog
/usr/include/KF5/AkonadiWidgets/Akonadi/CollectionPropertiesPage
/usr/include/KF5/AkonadiWidgets/Akonadi/CollectionRequester
/usr/include/KF5/AkonadiWidgets/Akonadi/CollectionStatisticsDelegate
/usr/include/KF5/AkonadiWidgets/Akonadi/ControlGui
/usr/include/KF5/AkonadiWidgets/Akonadi/ETMViewStateSaver
/usr/include/KF5/AkonadiWidgets/Akonadi/EntityListView
/usr/include/KF5/AkonadiWidgets/Akonadi/EntityTreeView
/usr/include/KF5/AkonadiWidgets/Akonadi/ManageAccountWidget
/usr/include/KF5/AkonadiWidgets/Akonadi/StandardActionManager
/usr/include/KF5/AkonadiWidgets/Akonadi/SubscriptionDialog
/usr/include/KF5/AkonadiWidgets/Akonadi/TagEditWidget
/usr/include/KF5/AkonadiWidgets/Akonadi/TagManagementDialog
/usr/include/KF5/AkonadiWidgets/Akonadi/TagSelectWidget
/usr/include/KF5/AkonadiWidgets/Akonadi/TagSelectionComboBox
/usr/include/KF5/AkonadiWidgets/Akonadi/TagSelectionDialog
/usr/include/KF5/AkonadiWidgets/Akonadi/TagWidget
/usr/include/KF5/AkonadiWidgets/akonadi/agentactionmanager.h
/usr/include/KF5/AkonadiWidgets/akonadi/agentconfigurationdialog.h
/usr/include/KF5/AkonadiWidgets/akonadi/agentconfigurationwidget.h
/usr/include/KF5/AkonadiWidgets/akonadi/agentinstancewidget.h
/usr/include/KF5/AkonadiWidgets/akonadi/agenttypedialog.h
/usr/include/KF5/AkonadiWidgets/akonadi/agenttypewidget.h
/usr/include/KF5/AkonadiWidgets/akonadi/akonadiwidgets_export.h
/usr/include/KF5/AkonadiWidgets/akonadi/collectioncombobox.h
/usr/include/KF5/AkonadiWidgets/akonadi/collectiondialog.h
/usr/include/KF5/AkonadiWidgets/akonadi/collectionmaintenancepage.h
/usr/include/KF5/AkonadiWidgets/akonadi/collectionpropertiesdialog.h
/usr/include/KF5/AkonadiWidgets/akonadi/collectionpropertiespage.h
/usr/include/KF5/AkonadiWidgets/akonadi/collectionrequester.h
/usr/include/KF5/AkonadiWidgets/akonadi/collectionstatisticsdelegate.h
/usr/include/KF5/AkonadiWidgets/akonadi/controlgui.h
/usr/include/KF5/AkonadiWidgets/akonadi/entitylistview.h
/usr/include/KF5/AkonadiWidgets/akonadi/entitytreeview.h
/usr/include/KF5/AkonadiWidgets/akonadi/etmviewstatesaver.h
/usr/include/KF5/AkonadiWidgets/akonadi/manageaccountwidget.h
/usr/include/KF5/AkonadiWidgets/akonadi/standardactionmanager.h
/usr/include/KF5/AkonadiWidgets/akonadi/subscriptiondialog.h
/usr/include/KF5/AkonadiWidgets/akonadi/tageditwidget.h
/usr/include/KF5/AkonadiWidgets/akonadi/tagmanagementdialog.h
/usr/include/KF5/AkonadiWidgets/akonadi/tagselectioncombobox.h
/usr/include/KF5/AkonadiWidgets/akonadi/tagselectiondialog.h
/usr/include/KF5/AkonadiWidgets/akonadi/tagselectwidget.h
/usr/include/KF5/AkonadiWidgets/akonadi/tagwidget.h
/usr/include/KF5/AkonadiXml/Akonadi/XmlDocument
/usr/include/KF5/AkonadiXml/Akonadi/XmlReader
/usr/include/KF5/AkonadiXml/Akonadi/XmlWriteJob
/usr/include/KF5/AkonadiXml/Akonadi/XmlWriter
/usr/include/KF5/AkonadiXml/akonadi/akonadi-xml_export.h
/usr/include/KF5/AkonadiXml/akonadi/xmldocument.h
/usr/include/KF5/AkonadiXml/akonadi/xmlreader.h
/usr/include/KF5/AkonadiXml/akonadi/xmlwritejob.h
/usr/include/KF5/AkonadiXml/akonadi/xmlwriter.h
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
/usr/lib64/libKF5AkonadiAgentBase.so.5.20.0
/usr/lib64/libKF5AkonadiCore.so.5
/usr/lib64/libKF5AkonadiCore.so.5.20.0
/usr/lib64/libKF5AkonadiPrivate.so.5
/usr/lib64/libKF5AkonadiPrivate.so.5.20.0
/usr/lib64/libKF5AkonadiWidgets.so.5
/usr/lib64/libKF5AkonadiWidgets.so.5.20.0
/usr/lib64/libKF5AkonadiXml.so.5
/usr/lib64/libKF5AkonadiXml.so.5.20.0
/usr/lib64/qt5/plugins/akonadi/akonadi_test_searchplugin.so
/usr/lib64/qt5/plugins/designer/akonadiwidgets.so
/usr/lib64/qt5/plugins/sqldrivers/libqsqlite3.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/akonadi/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/akonadi/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/akonadi/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/akonadi/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/akonadi/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/akonadi/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/akonadi/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadi_knut_resource.lang -f libakonadi5.lang
%defattr(-,root,root,-)

