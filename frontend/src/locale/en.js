const en = {

  currentlanguage: 'العربية',
  logout: 'Logout',

  buttons: {
    exportExcel: 'Export as excel'
  }, 

  pages: {

    addTransaction: {
      tabs: {
        addTransaction: 'Add Transaction',
        addCustomer: 'Add Customer',
        customerNamePlaceholder: 'Customer Name',
      },
      breadcrumb: {
        home: 'Home',
        new: 'New',
      },
      addCustomerErrorMessage: 'User already does exist',
      documentTitle: 'New Transaction',
      add: 'Add',
      displayType: {
        debit: 'debit',
        credit: 'credit',
      }
    },

    home: {
      documentTitle: 'Home',
      orderBy: 'Order By',
      orderOptions: {
        az: 'Customer A-Z',
        za: 'Customer Z-A',
        gs: 'Net Great-Small',
        sg: 'Net Small-Great',
        on: 'Date Older-Newer',
        no: 'Date Newer-Older',
      },
      showBtn: {
        show: 'Show',
        hide: 'Hide',
        closedAccount: 'Closed Accounts'
      },
      search: {
        placeholder: 'Filter',
        noResults: 'No Results'
      }
    },

    ledger: {
      home: "Home",
      tableHeader: {
        amount: 'Amount',
        net: 'Net',
        date: 'Date',
        user: 'User',
      },
      btns: {
        debit: 'Add Debit',
        credit: 'Add Credit',
      }
    },

    transactions: {
      breadcrumb: {
        home: 'Home',
        transactions: 'Transactions'
      },
      tableHeader: {
        amount: 'Amount',
        net: 'Net',
        customer: 'Customer',
        date: 'Date',
        user: 'User',
        options: 'Options',
      },
      tableMessage: {
        of: 'of',
        recordsFound: 'records found',
      },
      getMore: 'Get more',
    }

  },

  components: {

    customerCard: {
      contextMenu: {
        ledger: 'Ledger',
        addDebit: 'Add Debit',
        addCredit: 'Add Credit',
      }
    },

    report: {
      net: 'Net',
      transactionsCount: 'Transactions',
      customersCount: 'Customers',
      totalDebit: 'Debit',
      totalCredit: 'Credit',
    },
    
    searchInput: {
      placeholder: 'Search',
      notExistsMessage: 'does not exists, would you like to add him?',
      add: 'Add',
    }

  }
};

export default en;
