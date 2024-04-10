const ar = {

  currentlanguage: 'English',
  logout: 'خروج',

  buttons: {
    exportExcel: 'تصدير كملف إكسل'
  }, 

  pages: {
    addTransaction: {
      tabs: {
        addTransaction: 'حركة جديدة',
        addCustomer: 'زبون جديد',
        customerNamePlaceholder: 'اسم الزبون',
      },
      breadcrumb: {
        home: "الرئيسية",
        new: "جديدة",
      },
      addCustomerErrorMessage: 'هذا الاسم موجود مسبقاً !!',
      documentTitle: "حركة جديدة",
      add: "إضافة",
      displayType: {
        debit: 'قرضة',
        credit: 'دفعة',
      }
    },

    home: {
      documentTitle: "الرئيسية",
      orderBy: "ترتيب حسب",
      orderOptions: {
        az: "اسم الزبون تصاعدياً",
        za: "اسم الزبون تنازلياً",
        gs: "الرصيد من الأكبر الى الأصغر",
        sg: "الرصيد من الأصغر الى الأكبر",
        on: "آخر حركة من الأقدم الى الأحدث",
        no: "آخر حركة من الأحدث الى الأقدم",
      },
      showBtn: {
        show: "إظهار",
        hide: "إخفاء",
        closedAccount: "الحسابات المرّصدة",
      },
      search: {
        placeholder: "تصفية",
        noResults: "لا يوجد نتائج",
      },
    },

    ledger: {
      home: "الرئيسية",
      tableHeader: {
        amount: "المبلغ",
        net: "الرصيد",
        date: "التاريخ",
        user: "المستخدم",
      },
      btns: {
        debit: 'اضافة قرضة',
        credit: 'اضافة دفعة',
      }
    },

    transactions: {
      breadcrumb: {
        home: "الرئيسية",
        transactions: "آخر الحركات",
      },
      tableHeader: {
        amount: "المبلغ",
        net: "الرصيد",
        customer: "الزبون",
        date: "التاريخ",
        user: "المستخدم",
        options: "الخيارات",
      },
      tableMessage: {
        of: "من",
        recordsFound: "حركة",
      },
      getMore: "مشاهدة المزيد",
    },
  },

  components: {
    customerCard: {
      contextMenu: {
        ledger: "كشف الحساب",
        addDebit: "اضافة قرضة",
        addCredit: "اضافة دفعة",
      },
    },

    report: {
      net: "الرصيد",
      transactionsCount: 'عدد الحركات',
      customersCount: 'عدد الزبائن',
      totalDebit: "مجموع المدين",
      totalCredit: "مجموع الدائن",
    },

    searchInput: {
      placeholder: "البحث",
      notExistsMessage: "غير موجود سابقاً، هل تريد اضافته؟؟؟",
      add: "اضافة",
    },
  },
};

export default ar;
